import argparse
import os
import sys

# Ensure we can import from the current directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from context_loader import ContextLoader
from generator import ClusterGenerator

def main():
    parser = argparse.ArgumentParser(description="Physics Cluster Generator PoC")
    parser.add_argument("--topic", required=True, help="Topic to search for standards (e.g., 'Forces', 'Energy')")
    parser.add_argument("--stimulus", required=True, help="Description of the stimulus/scenario")
    
    args = parser.parse_args()
    
    # Determine the root of the repo (assuming this script is in /PoC)
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    print(f"--- Physics Cluster Generator PoC ---")
    print(f"Topic: {args.topic}")
    print(f"Stimulus: {args.stimulus}")
    print(f"Repo Root: {repo_root}")
    print("-" * 30)
    
    # 1. Load Context
    print("\n[1] Searching for relevant Standards and PLDs...")
    loader = ContextLoader(repo_root)
    context = loader.get_context_for_topic(args.topic)
    
    context_len = len(context)
    print(f"    Found context length: {context_len} chars")
    if context_len < 100:
        print(f"    WARNING: Low context found. Content: {context}")
    
    # 2. Generate Cluster
    print("\n[2] Generating Cluster...")
    generator = ClusterGenerator()
    result = generator.generate_cluster(context, args.stimulus)
    
    # 3. Output
    print("\n" + "="*30)
    print("       GENERATED OUTPUT       ")
    print("="*30)
    print(result)
    print("="*30)
    
    # 4. Cost Summary (Simulated)
    print("\n[Cost Analysis]")
    print(f"Context Loaded: ~{context_len // 4} tokens")
    print("Vector DB Cost: $0.00 (Not used)")
    print("Orchestration Overhead: Low (Single pass)")

if __name__ == "__main__":
    main()
