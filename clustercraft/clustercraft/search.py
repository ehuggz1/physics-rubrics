"""Enhanced Context Search and Loading with Caching"""
import os
import hashlib
import pickle
import logging
from typing import List, Dict, Optional

logger = logging.getLogger('clustercraft.search')

class ContextSearcher:
    def __init__(self, config: dict):
        self.config = config
        self.base_path = config['data']['base_path']
        self.standards_dir = os.path.join(self.base_path, config['data']['standards_dir'])
        self.pld_dir = os.path.join(self.base_path, config['data']['pld_dir'])
        
        self.enable_cache = config['search']['enable_cache']
        self.cache_dir = config['search']['cache_dir']
        
        if self.enable_cache:
            os.makedirs(self.cache_dir, exist_ok=True)
    
    def _normalize_standard_code(self, standard: str) -> list:
        """
        Normalize standard code to handle different formats.
        E.g., "HS-PS-2-1" -> ["HS-PS-2-1", "HS-PS2-1"]
        """
        normalized = [standard]
        
        # Handle format: HS-PS-2-1 -> HS-PS2-1 (remove hyphen between letters and first digit only)
        import re
        # Match pattern like "HS-PS-2-1" and create "HS-PS2-1"
        if re.match(r'^HS-[A-Z]+-\d+-\d+$', standard):
            # Remove only the hyphen between letters and the first digit
            # HS-PS-2-1 -> HS-PS2-1
            no_hyphen = re.sub(r'([A-Z])-(\d)', r'\1\2', standard)
            normalized.append(no_hyphen)
        
        return normalized
    
    def search_documents(self, keywords: List[str]) -> List[str]:
        """
        Search for documents matching keywords in their path.
        Returns list of file paths.
        """
        logger.info(f"Searching for documents with keywords: {keywords}")
        
        # Normalize all keywords (especially standard codes)
        expanded_keywords = []
        for keyword in keywords:
            expanded_keywords.extend(self._normalize_standard_code(keyword))
        
        logger.debug(f"Expanded keywords: {expanded_keywords}")
        found_files = []
        
        search_dirs = [self.standards_dir, self.pld_dir]
        
        for directory in search_dirs:
            if not os.path.exists(directory):
                logger.warning(f"Directory not found: {directory}")
                continue
            
            for root, _, files in os.walk(directory):
                for file in files:
                    full_path = os.path.join(root, file)
                    # Check if any expanded keyword is in the full path
                    if any(k.lower() in full_path.lower() for k in expanded_keywords):
                        found_files.append(full_path)
        
        logger.info(f"Found {len(found_files)} documents")
        return list(set(found_files))  # Deduplicate
    
    def _get_cache_key(self, file_path: str) -> str:
        """Generate cache key for a file"""
        # Use file path + modification time as cache key
        mtime = os.path.getmtime(file_path)
        key_string = f"{file_path}_{mtime}"
        return hashlib.md5(key_string.encode()).hexdigest()
    
    def _load_from_cache(self, cache_key: str) -> Optional[str]:
        """Load content from cache if available"""
        cache_file = os.path.join(self.cache_dir, f"{cache_key}.pkl")
        
        if os.path.exists(cache_file):
            logger.debug(f"Loading from cache: {cache_key}")
            with open(cache_file, 'rb') as f:
                return pickle.load(f)
        
        return None
    
    def _save_to_cache(self, cache_key: str, content: str):
        """Save content to cache"""
        cache_file = os.path.join(self.cache_dir, f"{cache_key}.pkl")
        
        with open(cache_file, 'wb') as f:
            pickle.dump(content, f)
        
        logger.debug(f"Saved to cache: {cache_key}")
    
    def load_documents(self, file_paths: List[str]) -> str:
        """
        Load content from specified files with caching support.
        Returns concatenated content with metadata.
        """
        context_parts = []
        
        for path in file_paths:
            filename = os.path.basename(path)
            relative_path = os.path.relpath(path, self.base_path)
            
            # Try cache first
            content = None
            if self.enable_cache:
                cache_key = self._get_cache_key(path)
                content = self._load_from_cache(cache_key)
            
            # Load from file if not cached
            if content is None:
                try:
                    logger.debug(f"Reading file: {filename}")
                    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    # Save to cache
                    if self.enable_cache:
                        self._save_to_cache(cache_key, content)
                
                except Exception as e:
                    logger.error(f"Error reading {filename}: {str(e)}")
                    content = f"[ERROR: Could not read file - {str(e)}]"
            
            # Add metadata and content
            context_parts.append(
                f"--- DOCUMENT: {filename} ---\n"
                f"Source: {relative_path}\n"
                f"---\n{content}\n"
                f"--- END DOCUMENT ---"
            )
        
        return "\n\n".join(context_parts)
    
    def get_context(self, topic: str) -> Dict[str, any]:
        """
        High-level method to get context for a topic.
        Returns dict with context string and metadata.
        """
        files = self.search_documents([topic])
        
        if not files:
            logger.warning(f"No documents found for topic: {topic}")
            return {
                'context': f"No documents found for topic: {topic}",
                'file_count': 0,
                'files': [],
                'char_count': 0,
                'estimated_tokens': 0
            }
        
        context = self.load_documents(files)
        
        return {
            'context': context,
            'file_count': len(files),
            'files': [os.path.basename(f) for f in files],
            'char_count': len(context),
            'estimated_tokens': len(context) // 4
        }
    
    def get_context_for_standards(self, standards: list) -> Dict[str, any]:
        """
        High-level method to get context for specific standards.
        Uses standard codes for more targeted search.
        
        Args:
            standards: List of standard codes (e.g., ["HS-PS-2-1", "HS-PS-3-1"])
        
        Returns:
            Dict with context string and metadata
        """
        files = self.search_documents(standards)
        
        if not files:
            logger.warning(f"No documents found for standards: {', '.join(standards)}")
            return {
                'context': f"No documents found for standards: {', '.join(standards)}",
                'file_count': 0,
                'files': [],
                'char_count': 0,
                'estimated_tokens': 0
            }
        
        context = self.load_documents(files)
        
        return {
            'context': context,
            'file_count': len(files),
            'files': [os.path.basename(f) for f in files],
            'char_count': len(context),
            'estimated_tokens': len(context) // 4,
            'standards': standards
        }
