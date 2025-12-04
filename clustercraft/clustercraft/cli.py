"""ClusterCraft CLI - Cost-Effective Physics Question Generator"""
import argparse
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils import load_config, setup_logging, ensure_dir, generate_output_filename
from orchestrator import ClusterOrchestrator

def main():
    parser = argparse.ArgumentParser(
        description="ClusterCraft: Cost-Effective Physics Question Generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  clustercraft --focus-standard "HS-PS-2-1" --stimulus "A car braking on wet pavement"
  clustercraft --focus-standard "HS-PS-3-1" --ancillary-standards "HS-PS-3-2,HS-PS-2-1" --stimulus "A roller coaster"
  clustercraft --focus-standard "HS-PS-4-1" --stimulus-file "./stimuli/sound_waves.md" --dry-run
        """
    )
    
    parser.add_argument(
        '--focus-standard',
        required=True,
        help='Primary Performance Expectation Standard (e.g., "HS-PS-2-1")'
    )
    
    parser.add_argument(
        '--ancillary-standards',
        help='Comma-separated list of additional standards (e.g., "HS-PS-3-1,HS-PS-2-2")'
    )
    
    parser.add_argument(
        '--stimulus',
        help='Description of the stimulus/scenario (use this OR --stimulus-file)'
    )
    
    parser.add_argument(
        '--stimulus-file',
        help='Path to markdown file containing the stimulus (use this OR --stimulus)'
    )
    
    parser.add_argument(
        '--output',
        help='Output directory (default: from config)'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show prompt without calling LLM'
    )
    
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Enable verbose logging'
    )
    
    parser.add_argument(
        '--config',
        default='config/settings.yaml',
        help='Path to configuration file'
    )
    
    args = parser.parse_args()
    
    # Validate stimulus input
    if not args.stimulus and not args.stimulus_file:
        parser.error("Either --stimulus or --stimulus-file must be provided")
    
    if args.stimulus and args.stimulus_file:
        parser.error("Cannot specify both --stimulus and --stimulus-file")
    
    # Load configuration
    try:
        config = load_config(args.config)
    except Exception as e:
        print(f"Error loading configuration: {e}")
        sys.exit(1)
    
    # Override log level if verbose
    if args.verbose:
        config['logging']['level'] = 'DEBUG'
    
    # Setup logging
    logger = setup_logging(config)
    
    # Load stimulus from file if specified (after logger is initialized)
    if args.stimulus_file:
        try:
            with open(args.stimulus_file, 'r', encoding='utf-8') as f:
                stimulus = f.read()
            logger.info(f"Loaded stimulus from file: {args.stimulus_file}")
        except Exception as e:
            logger.error(f"Error reading stimulus file: {e}")
            sys.exit(1)
    else:
        stimulus = args.stimulus
    
    logger.info("=" * 50)
    logger.info("ClusterCraft: Physics Question Generator")
    logger.info("=" * 50)
    logger.info(f"Focus Standard: {args.focus_standard}")
    
    # Parse ancillary standards
    ancillary_standards = []
    if args.ancillary_standards:
        ancillary_standards = [s.strip() for s in args.ancillary_standards.split(',')]
        logger.info(f"Ancillary Standards: {', '.join(ancillary_standards)}")
    
    if args.stimulus_file:
        logger.info(f"Stimulus Source: File ({args.stimulus_file})")
        logger.info(f"Stimulus Length: {len(stimulus)} characters")
    else:
        logger.info(f"Stimulus: {stimulus}")
    
    logger.info(f"Dry Run: {args.dry_run}")
    
    # Create orchestrator
    orchestrator = ClusterOrchestrator(config)
    
    # Generate cluster
    result = orchestrator.generate_cluster(
        focus_standard=args.focus_standard,
        ancillary_standards=ancillary_standards,
        stimulus=stimulus,
        dry_run=args.dry_run
    )
    
    # Handle dry run
    if args.dry_run:
        print("\n" + "=" * 50)
        print("DRY RUN - PROMPT PREVIEW")
        print("=" * 50)
        print(f"\nPrompt Length: {result['prompt_length']} chars")
        print(f"Context Files: {result['context_metadata']['file_count']}")
        print(f"Estimated Tokens: {result['context_metadata']['estimated_tokens']}")
        print("\n--- PROMPT ---")
        print(result['prompt'][:2000])  # Show first 2000 chars
        print("\n... (truncated)")
        return
    
    # Handle generation failure
    if not result['success']:
        logger.error(f"Generation failed: {result.get('error', 'Unknown error')}")
        sys.exit(1)
    
    # Save output
    output_dir = args.output or config['output']['dir']
    ensure_dir(output_dir)
    
    output_file = generate_output_filename(args.focus_standard, output_dir)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result['cluster'])
    
    logger.info(f"Cluster saved to: {output_file}")
    
    # Print summary
    print("\n" + "=" * 50)
    print("GENERATION COMPLETE")
    print("=" * 50)
    print(f"\nOutput File: {output_file}")
    print(f"\nContext Metadata:")
    print(f"  Files Found: {result['context_metadata']['file_count']}")
    print(f"  Files: {', '.join(result['context_metadata']['files'][:5])}")
    if result['context_metadata']['file_count'] > 5:
        print(f"  ... and {result['context_metadata']['file_count'] - 5} more")
    
    print(f"\nCost Summary:")
    cost = result['cost_summary']
    print(f"  Input Tokens: {cost['input_tokens']:,}")
    print(f"  Output Tokens: {cost['output_tokens']:,}")
    print(f"  Total Tokens: {cost['total_tokens']:,}")
    print(f"  Estimated Cost: ${cost['estimated_cost_usd']:.4f}")
    
    # Print validation results
    if 'validation' in result:
        validation = result['validation']
        print(f"\nValidation:")
        if validation['valid']:
            print(f"  Status: [PASSED]")
        else:
            print(f"  Status: [ISSUES FOUND]")
        print(f"  Summary: {validation['summary']}")
        
        if validation['errors']:
            print(f"\n  Errors:")
            for error in validation['errors']:
                print(f"    [X] {error['check']}: {error['message']}")
        
        if validation['warnings']:
            print(f"\n  Warnings:")
            for warning in validation['warnings']:
                print(f"    [!] {warning['check']}: {warning['message']}")
    
    print("\n" + "=" * 50)

if __name__ == "__main__":
    main()
