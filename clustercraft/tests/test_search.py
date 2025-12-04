"""Unit tests for AG-Simplified"""
import unittest
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from search import ContextSearcher
from utils import load_config

class TestContextSearcher(unittest.TestCase):
    def setUp(self):
        """Setup test configuration"""
        self.config = {
            'data': {
                'base_path': '..',
                'standards_dir': 'Physics Teaching Standards',
                'pld_dir': 'Performance Level Descriptors'
            },
            'search': {
                'enable_cache': False,
                'cache_dir': '.cache'
            }
        }
        self.searcher = ContextSearcher(self.config)
    
    def test_search_documents_forces(self):
        """Test searching for Forces documents"""
        files = self.searcher.search_documents(['Forces'])
        self.assertGreater(len(files), 0, "Should find at least one Forces document")
    
    def test_search_documents_energy(self):
        """Test searching for Energy documents"""
        files = self.searcher.search_documents(['Energy'])
        self.assertGreater(len(files), 0, "Should find at least one Energy document")
    
    def test_get_context(self):
        """Test getting full context"""
        context_data = self.searcher.get_context('Forces')
        
        self.assertIn('context', context_data)
        self.assertIn('file_count', context_data)
        self.assertGreater(context_data['file_count'], 0)
        self.assertGreater(context_data['char_count'], 0)

if __name__ == '__main__':
    unittest.main()
