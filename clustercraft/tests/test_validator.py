"""Unit tests for the validator module"""
import unittest
from src.validator import ClusterValidator


class TestClusterValidator(unittest.TestCase):
    def setUp(self):
        self.validator = ClusterValidator()
    
    def test_valid_cluster(self):
        """Test validation of a properly formatted cluster"""
        cluster = """
# Generated Physics Cluster

## Stimulus
A car braking on wet pavement.

## Questions

### Question 1
**Standard:** HS-PS-2-1
**Dimension 1 (SEP):** Using Mathematics
**Dimension 2 (CCC):** Cause and Effect
**Dimension 3 (DCI):** Newton's Laws

**Question:** Calculate the net force.

**Answer Key:**
- Apply F=ma
- Show work

### Question 2
**Standard:** HS-PS-3-1
**Dimension 1 (SEP):** Developing Models
**Dimension 2 (CCC):** Energy and Matter
**Dimension 3 (DCI):** Conservation of Energy

**Question:** Describe energy transformations.

**Answer Key:**
- Identify energy states
- Show conservation
        """
        
        result = self.validator.validate_cluster(cluster, "HS-PS-2-1", ["HS-PS-3-1"])
        
        self.assertTrue(result['valid'])
        self.assertEqual(len(result['errors']), 0)
    
    def test_missing_stimulus(self):
        """Test detection of missing stimulus section"""
        cluster = """
## Questions

### Question 1
**Question:** Test question
**Answer Key:** Test answer
        """
        
        result = self.validator.validate_cluster(cluster, "HS-PS-2-1", [])
        
        self.assertFalse(result['valid'])
        self.assertTrue(any(e['check'] == 'Stimulus Section' for e in result['errors']))
    
    def test_missing_questions(self):
        """Test detection of missing questions"""
        cluster = """
## Stimulus
Test stimulus
        """
        
        result = self.validator.validate_cluster(cluster, "HS-PS-2-1", [])
        
        self.assertFalse(result['valid'])
        self.assertTrue(any(e['check'] == 'Question Count' for e in result['errors']))
    
    def test_missing_answer_keys(self):
        """Test detection of missing answer keys"""
        cluster = """
## Stimulus
Test stimulus

### Question 1
**Question:** Test question
        """
        
        result = self.validator.validate_cluster(cluster, "HS-PS-2-1", [])
        
        self.assertFalse(result['valid'])
        self.assertTrue(any(e['check'] == 'Answer Keys' for e in result['errors']))
    
    def test_focus_standard_not_used(self):
        """Test detection when focus standard is not used"""
        cluster = """
## Stimulus
Test stimulus

### Question 1
**Standard:** HS-PS-3-1
**Question:** Test question
**Answer Key:** Test answer
        """
        
        result = self.validator.validate_cluster(cluster, "HS-PS-2-1", ["HS-PS-3-1"])
        
        self.assertFalse(result['valid'])
        self.assertTrue(any(e['check'] == 'Focus Standard' for e in result['errors']))
    
    def test_standard_normalization(self):
        """Test that standard code normalization works (HS-PS-2-1 vs HS-PS2-1)"""
        cluster = """
## Stimulus
Test stimulus

### Question 1
**Standard:** HS-PS2-1
**Question:** Test question
**Answer Key:** Test answer
        """
        
        result = self.validator.validate_cluster(cluster, "HS-PS-2-1", [])
        
        # Should find the standard even though format differs
        found_standards = [c for c in result['all_checks'] if c['check'] == 'Focus Standard']
        self.assertTrue(found_standards[0]['passed'])
    
    def test_question_count_warning(self):
        """Test warning for unusual question count"""
        cluster = """
## Stimulus
Test stimulus

### Question 1
**Question:** Q1
**Answer Key:** A1

### Question 2
**Question:** Q2
**Answer Key:** A2

### Question 3
**Question:** Q3
**Answer Key:** A3

### Question 4
**Question:** Q4
**Answer Key:** A4
        """
        
        result = self.validator.validate_cluster(cluster, "HS-PS-2-1", [])
        
        # Should have warning about 4 questions (recommended is 1-3)
        self.assertTrue(any(w['check'] == 'Question Count' for w in result['warnings']))
    
    def test_dimensions_coverage(self):
        """Test detection of three-dimensional framework"""
        cluster_with_dimensions = """
## Stimulus
Test

### Question 1
**Dimension 1 (SEP):** Using Mathematics
**Dimension 2 (CCC):** Cause and Effect
**Dimension 3 (DCI):** Newton's Laws
**Question:** Test
**Answer Key:** Test
        """
        
        result = self.validator.validate_cluster(cluster_with_dimensions, "HS-PS-2-1", [])
        
        # Should find all three dimensions
        dimension_checks = [c for c in result['all_checks'] if c['check'] == 'Three Dimensions']
        self.assertTrue(dimension_checks[0]['passed'])


if __name__ == '__main__':
    unittest.main()
