"""Unit tests for the LLM module"""
import unittest
from src.llm import LLMClient


class TestLLMClient(unittest.TestCase):
    def setUp(self):
        self.config = {
            'model': {
                'name': 'gemini-1.5-flash',
                'temperature': 0.7,
                'max_tokens': 2000
            }
        }
        self.client = LLMClient(self.config)
    
    def test_initialization(self):
        """Test LLM client initialization"""
        self.assertEqual(self.client.model_name, 'gemini-1.5-flash')
        self.assertEqual(self.client.temperature, 0.7)
        self.assertEqual(self.client.max_tokens, 2000)
    
    def test_mock_generation(self):
        """Test mock generation returns content"""
        prompt = "Test prompt"
        result = self.client.generate(prompt)
        
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
    
    def test_cost_tracking(self):
        """Test that cost tracking works"""
        prompt = "Test prompt with some content"
        
        # Generate content
        self.client.generate(prompt)
        
        # Get cost summary
        cost = self.client.get_cost_summary()
        
        self.assertIn('input_tokens', cost)
        self.assertIn('output_tokens', cost)
        self.assertIn('total_tokens', cost)
        self.assertIn('estimated_cost_usd', cost)
        
        # Should have tracked some tokens
        self.assertGreater(cost['input_tokens'], 0)
        self.assertGreater(cost['output_tokens'], 0)
    
    def test_cost_calculation(self):
        """Test cost calculation accuracy"""
        # Gemini Flash pricing (as of implementation)
        # Input: $0.000075 per 1K tokens
        # Output: $0.0003 per 1K tokens
        
        prompt = "x" * 1000  # ~250 tokens
        self.client.generate(prompt)
        
        cost = self.client.get_cost_summary()
        
        # Cost should be greater than 0
        self.assertGreater(cost['estimated_cost_usd'], 0)
        
        # Cost should be reasonable (not negative, not absurdly high)
        self.assertLess(cost['estimated_cost_usd'], 1.0)  # Should be much less than $1


if __name__ == '__main__':
    unittest.main()
