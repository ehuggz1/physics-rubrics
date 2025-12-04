import os
import glob
from typing import List, Dict

class ContextLoader:
    def __init__(self, base_path: str):
        self.base_path = base_path
        self.standards_dir = os.path.join(base_path, "Physics Teaching Standards")
        self.pld_dir = os.path.join(base_path, "Performance Level Descriptors")

    def search_documents(self, keywords: List[str]) -> List[str]:
        """
        Scans the standards and PLD directories for files matching the keywords.
        Returns a list of file paths.
        """
        found_files = []
        
        # Simple keyword matching in filenames for this PoC
        # In a real "Search-First" approach, this could use a local search index or grep
        
        search_dirs = [self.standards_dir, self.pld_dir]
        
        for directory in search_dirs:
            if not os.path.exists(directory):
                continue
                
            for root, _, files in os.walk(directory):
                for file in files:
                    full_path = os.path.join(root, file)
                    # Check if any keyword is in the full path (case-insensitive)
                    if any(k.lower() in full_path.lower() for k in keywords):
                        found_files.append(full_path)
        
        return list(set(found_files)) # Deduplicate

    def load_context(self, file_paths: List[str]) -> str:
        """
        Reads the content of the specified files.
        For this PoC, we'll assume text-based reading. 
        Note: Real PDF reading would require pypdf or similar.
        We will return a placeholder for binary files if we can't read them easily in standard lib.
        """
        context_parts = []
        
        for path in file_paths:
            filename = os.path.basename(path)
            try:
                # Try reading as text first
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    context_parts.append(f"--- START DOCUMENT: {filename} ---\n{content}\n--- END DOCUMENT: {filename} ---")
            except Exception as e:
                context_parts.append(f"--- ERROR READING: {filename} ({str(e)}) ---")
                
        return "\n\n".join(context_parts)

    def get_context_for_topic(self, topic: str) -> str:
        """
        High-level helper to get full context string for a topic.
        """
        files = self.search_documents([topic])
        if not files:
            return f"No documents found for topic: {topic}"
        
        return self.load_context(files)
