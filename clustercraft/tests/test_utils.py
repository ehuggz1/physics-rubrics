"""Unit tests for the utils module"""
import unittest
import os
import tempfile
import shutil
from src.utils import load_config, ensure_dir, generate_output_filename


class TestUtils(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for test files
        self.test_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        # Clean up temporary directory
        shutil.rmtree(self.test_dir)
    
    def test_load_config(self):
        """Test loading a YAML configuration file"""
        config_path = os.path.join(self.test_dir, 'test_config.yaml')
        
        # Create a test config file
        with open(config_path, 'w') as f:
            f.write("""
data:
  base_path: "."
  standards_dir: "Physics Teaching Standards"
  pld_dir: "Performance Level Descriptors"

model:
  name: "gemini-1.5-flash"
  temperature: 0.7
  max_tokens: 2000

search:
  file_extensions:
    - ".mhtml"
    - ".html"
    - ".pdf"
  enable_cache: true
  cache_dir: ".cache"

output:
  dir: "output"
  format: "markdown"

logging:
  level: "INFO"
  file: "ag-simplified.log"
            """)
        
        config = load_config(config_path)
        
        self.assertEqual(config['model']['name'], 'gemini-1.5-flash')
        self.assertEqual(config['model']['temperature'], 0.7)
        self.assertTrue(config['search']['enable_cache'])
    
    def test_ensure_dir_creates_directory(self):
        """Test that ensure_dir creates a directory if it doesn't exist"""
        new_dir = os.path.join(self.test_dir, 'new_directory')
        
        self.assertFalse(os.path.exists(new_dir))
        
        ensure_dir(new_dir)
        
        self.assertTrue(os.path.exists(new_dir))
        self.assertTrue(os.path.isdir(new_dir))
    
    def test_ensure_dir_existing_directory(self):
        """Test that ensure_dir doesn't fail on existing directory"""
        existing_dir = os.path.join(self.test_dir, 'existing')
        os.makedirs(existing_dir)
        
        # Should not raise an error
        ensure_dir(existing_dir)
        
        self.assertTrue(os.path.exists(existing_dir))
    
    def test_generate_output_filename(self):
        """Test output filename generation"""
        output_dir = self.test_dir
        
        # Test with standard code
        filename = generate_output_filename("HS-PS-2-1", output_dir)
        
        self.assertTrue(filename.startswith(output_dir))
        self.assertTrue('hs-ps-2-1' in filename.lower())
        self.assertTrue(filename.endswith('.md'))
    
    def test_generate_output_filename_format(self):
        """Test that output filename has correct format"""
        output_dir = self.test_dir
        
        filename = generate_output_filename("HS-PS-3-1", output_dir)
        basename = os.path.basename(filename)
        
        # Should be in format: cluster_hs-ps-3-1_YYYYMMDD_HHMMSS.md
        self.assertTrue(basename.startswith('cluster_'))
        self.assertTrue(basename.endswith('.md'))
        
        # Extract parts
        parts = basename.replace('.md', '').split('_')
        self.assertEqual(parts[0], 'cluster')
        self.assertEqual(parts[1], 'hs-ps-3-1')
        # parts[2] should be date (YYYYMMDD)
        self.assertEqual(len(parts[2]), 8)
        # parts[3] should be time (HHMMSS)
        self.assertEqual(len(parts[3]), 6)


if __name__ == '__main__':
    unittest.main()
