"""Orchestrator - Manages the workflow"""
import logging
import os
from typing import Dict
from jinja2 import Environment, FileSystemLoader
from search import ContextSearcher
from llm import LLMClient
from validator import ClusterValidator

logger = logging.getLogger('clustercraft.orchestrator')

class ClusterOrchestrator:
    def __init__(self, config: dict):
        self.config = config
        self.searcher = ContextSearcher(config)
        self.llm = LLMClient(config)
        self.validator = ClusterValidator()
        
        # Setup Jinja2 template environment
        template_dir = os.path.join(os.path.dirname(__file__), '..', 'templates')
        self.jinja_env = Environment(loader=FileSystemLoader(template_dir))
        
        # Load system instruction
        with open(os.path.join(template_dir, 'system_instruction.md'), 'r') as f:
            self.system_instruction = f.read()
    
    def _build_prompt(self, context: str, stimulus: str, focus_standard: str, ancillary_standards: list) -> str:
        """Build the prompt for cluster generation using Jinja2 templates"""
        template = self.jinja_env.get_template('cluster_prompt.j2')
        
        return template.render(
            system_instruction=self.system_instruction,
            context=context,
            stimulus=stimulus,
            focus_standard=focus_standard,
            ancillary_standards=ancillary_standards
        )
    
    def generate_cluster(self, focus_standard: str, ancillary_standards: list, stimulus: str, dry_run: bool = False) -> Dict:
        """
        Main workflow: Search -> Build Prompt -> Generate -> Return
        
        Args:
            focus_standard: Primary Performance Expectation Standard (e.g., "HS-PS-2-1")
            ancillary_standards: List of additional standards to include
            stimulus: Scenario description
            dry_run: If True, return prompt without calling LLM
        
        Returns:
            Dict with generated cluster and metadata
        """
        logger.info(f"Starting cluster generation for focus standard: {focus_standard}")
        
        # Combine all standards for search
        all_standards = [focus_standard] + ancillary_standards
        
        # Step 1: Search and load context
        logger.info("Step 1: Searching for relevant documents...")
        context_data = self.searcher.get_context_for_standards(all_standards)
        
        logger.info(f"Found {context_data['file_count']} documents")
        logger.info(f"Context size: {context_data['char_count']} chars (~{context_data['estimated_tokens']} tokens)")
        
        # Step 2: Build prompt
        logger.info("Step 2: Building prompt...")
        prompt = self._build_prompt(
            context_data['context'], 
            stimulus, 
            focus_standard, 
            ancillary_standards
        )
        
        if dry_run:
            logger.info("Dry run mode - skipping LLM call")
            return {
                'success': True,
                'dry_run': True,
                'prompt': prompt,
                'prompt_length': len(prompt),
                'context_metadata': context_data,
                'focus_standard': focus_standard,
                'ancillary_standards': ancillary_standards
            }
        
        # Step 3: Generate
        logger.info("Step 3: Generating cluster...")
        generated_content = self.llm.generate(prompt)
        
        if generated_content is None:
            logger.error("Generation failed")
            return {
                'success': False,
                'error': 'LLM generation failed after retries'
            }
        
        # Step 4: Return results
        logger.info("Generation complete")
        
        # Step 5: Validate generated cluster
        logger.info("Step 4: Validating generated cluster...")
        validation_result = self.validator.validate_cluster(
            generated_content, 
            focus_standard, 
            ancillary_standards
        )
        
        # Log validation results
        if validation_result['valid']:
            logger.info("Validation passed")
        else:
            logger.warning(f"Validation issues found: {validation_result['summary']}")
        
        for check in validation_result['all_checks']:
            if check['level'] == 'ERROR':
                logger.error(f"  [X] {check['check']}: {check['message']}")
            elif check['level'] == 'WARNING':
                logger.warning(f"  [!] {check['check']}: {check['message']}")
            else:
                logger.debug(f"  [OK] {check['check']}: {check['message']}")
        
        return {
            'success': True,
            'cluster': generated_content,
            'context_metadata': context_data,
            'cost_summary': self.llm.get_cost_summary(),
            'focus_standard': focus_standard,
            'ancillary_standards': ancillary_standards,
            'validation': validation_result
        }
