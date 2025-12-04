"""Validation module for generated clusters"""
import re
import logging
from typing import Dict, List

logger = logging.getLogger('clustercraft.validator')

class ClusterValidator:
    """Validates generated Physics Clusters against requirements"""
    
    def __init__(self):
        self.validation_results = []
    
    def validate_cluster(self, cluster_content: str, focus_standard: str, ancillary_standards: List[str]) -> Dict:
        """
        Validate a generated cluster against requirements.
        
        Args:
            cluster_content: The generated cluster markdown
            focus_standard: The focus standard that should be present
            ancillary_standards: List of ancillary standards
        
        Returns:
            Dict with validation results
        """
        self.validation_results = []
        all_standards = [focus_standard] + ancillary_standards
        
        # Run all validation checks
        self._check_has_stimulus(cluster_content)
        self._check_has_questions(cluster_content)
        self._check_has_answer_keys(cluster_content)
        self._check_standards_referenced(cluster_content, all_standards)
        self._check_focus_standard_used(cluster_content, focus_standard)
        self._check_dimensions_covered(cluster_content)
        
        # Calculate overall validation status
        errors = [r for r in self.validation_results if r['level'] == 'ERROR']
        warnings = [r for r in self.validation_results if r['level'] == 'WARNING']
        
        is_valid = len(errors) == 0
        
        return {
            'valid': is_valid,
            'errors': errors,
            'warnings': warnings,
            'all_checks': self.validation_results,
            'summary': f"{len(errors)} errors, {len(warnings)} warnings"
        }
    
    def _add_result(self, level: str, check: str, message: str, passed: bool):
        """Add a validation result"""
        self.validation_results.append({
            'level': level,
            'check': check,
            'message': message,
            'passed': passed
        })
    
    def _check_has_stimulus(self, content: str):
        """Check if cluster has a stimulus section"""
        has_stimulus = bool(re.search(r'##\s*Stimulus', content, re.IGNORECASE))
        
        if has_stimulus:
            self._add_result('INFO', 'Stimulus Section', 'Stimulus section found', True)
        else:
            self._add_result('ERROR', 'Stimulus Section', 'Missing stimulus section', False)
    
    def _check_has_questions(self, content: str):
        """Check if cluster has questions"""
        # Look for question headers (### Question)
        questions = re.findall(r'###\s*Question\s*\d+', content, re.IGNORECASE)
        num_questions = len(questions)
        
        if num_questions >= 1 and num_questions <= 3:
            self._add_result('INFO', 'Question Count', f'Found {num_questions} questions (valid range: 1-3)', True)
        elif num_questions == 0:
            self._add_result('ERROR', 'Question Count', 'No questions found', False)
        else:
            self._add_result('WARNING', 'Question Count', f'Found {num_questions} questions (recommended: 1-3)', True)
    
    def _check_has_answer_keys(self, content: str):
        """Check if questions have answer keys"""
        # Look for answer key sections
        answer_keys = re.findall(r'\*\*Answer Key\*\*', content, re.IGNORECASE)
        questions = re.findall(r'###\s*Question\s*\d+', content, re.IGNORECASE)
        
        num_answer_keys = len(answer_keys)
        num_questions = len(questions)
        
        if num_answer_keys == num_questions and num_questions > 0:
            self._add_result('INFO', 'Answer Keys', f'All {num_questions} questions have answer keys', True)
        elif num_answer_keys < num_questions:
            self._add_result('ERROR', 'Answer Keys', f'Only {num_answer_keys}/{num_questions} questions have answer keys', False)
        elif num_questions == 0:
            self._add_result('WARNING', 'Answer Keys', 'No questions to validate answer keys for', True)
    
    def _check_standards_referenced(self, content: str, standards: List[str]):
        """Check if standards are referenced in the cluster"""
        found_standards = []
        missing_standards = []
        
        for standard in standards:
            # Normalize standard for search (handle both HS-PS-2-1 and HS-PS2-1 formats)
            normalized = re.sub(r'([A-Z])-(\d)', r'\1\2', standard)
            
            # Search for either format
            if re.search(standard, content, re.IGNORECASE) or re.search(normalized, content, re.IGNORECASE):
                found_standards.append(standard)
            else:
                missing_standards.append(standard)
        
        if len(found_standards) == len(standards):
            self._add_result('INFO', 'Standards Referenced', f'All {len(standards)} standards referenced', True)
        else:
            self._add_result('WARNING', 'Standards Referenced', 
                           f'{len(found_standards)}/{len(standards)} standards referenced. Missing: {", ".join(missing_standards)}', 
                           True)
    
    def _check_focus_standard_used(self, content: str, focus_standard: str):
        """Check if the focus standard is used in at least one question"""
        # Normalize for search
        normalized = re.sub(r'([A-Z])-(\d)', r'\1\2', focus_standard)
        
        # Look for the focus standard in question sections
        question_sections = re.split(r'###\s*Question\s*\d+', content, flags=re.IGNORECASE)
        
        focus_used = False
        for section in question_sections[1:]:  # Skip first split (before first question)
            if re.search(focus_standard, section, re.IGNORECASE) or re.search(normalized, section, re.IGNORECASE):
                focus_used = True
                break
        
        if focus_used:
            self._add_result('INFO', 'Focus Standard', f'Focus standard {focus_standard} used in questions', True)
        else:
            self._add_result('ERROR', 'Focus Standard', f'Focus standard {focus_standard} not found in any question', False)
    
    def _check_dimensions_covered(self, content: str):
        """Check if three-dimensional framework is referenced"""
        # Look for dimension indicators
        has_sep = bool(re.search(r'Dimension 1|SEP|Science.*Engineering.*Practice', content, re.IGNORECASE))
        has_ccc = bool(re.search(r'Dimension 2|CCC|Cross.*Cutting.*Concept', content, re.IGNORECASE))
        has_dci = bool(re.search(r'Dimension 3|DCI|Disciplinary.*Core.*Idea', content, re.IGNORECASE))
        
        dimensions_found = sum([has_sep, has_ccc, has_dci])
        
        if dimensions_found == 3:
            self._add_result('INFO', 'Three Dimensions', 'All three dimensions referenced', True)
        elif dimensions_found >= 1:
            missing = []
            if not has_sep: missing.append('SEP')
            if not has_ccc: missing.append('CCC')
            if not has_dci: missing.append('DCI')
            self._add_result('WARNING', 'Three Dimensions', 
                           f'Only {dimensions_found}/3 dimensions found. Missing: {", ".join(missing)}', 
                           True)
        else:
            self._add_result('WARNING', 'Three Dimensions', 'No dimension indicators found', True)
