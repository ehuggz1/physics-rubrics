"""LLM Client with retry logic and cost tracking"""
import os
import time
import logging
from typing import Optional

logger = logging.getLogger('clustercraft.llm')

class LLMClient:
    def __init__(self, config: dict):
        self.config = config
        self.model_name = config['model']['name']
        self.temperature = config['model']['temperature']
        self.max_tokens = config['model']['max_tokens']
        
        # API key from environment
        self.api_key = os.getenv('GEMINI_API_KEY')
        
        # Cost tracking
        self.total_input_tokens = 0
        self.total_output_tokens = 0
    
    def generate(self, prompt: str, retry_count: int = 3) -> Optional[str]:
        """
        Generate response from LLM with retry logic.
        For this implementation, we'll simulate the call.
        In production, this would use the actual API.
        """
        logger.info(f"Generating with {self.model_name}")
        logger.debug(f"Prompt length: {len(prompt)} chars")
        
        # Estimate tokens
        estimated_input_tokens = len(prompt) // 4
        self.total_input_tokens += estimated_input_tokens
        
        # Simulate API call with retry logic
        for attempt in range(retry_count):
            try:
                # In production, this would be the actual API call
                # For now, we'll simulate with a mock response
                response = self._mock_generate(prompt)
                
                # Estimate output tokens
                estimated_output_tokens = len(response) // 4
                self.total_output_tokens += estimated_output_tokens
                
                logger.info(f"Generation successful (attempt {attempt + 1}/{retry_count})")
                return response
            
            except Exception as e:
                logger.warning(f"Generation attempt {attempt + 1} failed: {str(e)}")
                
                if attempt < retry_count - 1:
                    wait_time = 2 ** attempt  # Exponential backoff
                    logger.info(f"Retrying in {wait_time} seconds...")
                    time.sleep(wait_time)
                else:
                    logger.error("All retry attempts failed")
                    return None
    
    def _mock_generate(self, prompt: str) -> str:
        """
        Mock generation for demonstration.
        Replace this with actual API call in production.
        """
        # Simulate processing time
        time.sleep(1.5)
        
        # Extract stimulus from prompt if possible
        stimulus = "the provided scenario"
        if "STIMULUS:" in prompt:
            stimulus_start = prompt.find("STIMULUS:") + len("STIMULUS:")
            stimulus_end = prompt.find("---", stimulus_start)
            if stimulus_end > stimulus_start:
                stimulus = prompt[stimulus_start:stimulus_end].strip()
        
        return f"""# Generated Physics Cluster

## Stimulus
{stimulus}

## Questions

### Question 1
**Standard:** HS-PS-2-1 (Forces and Motion)
**Dimension 1 (SEP):** Using Mathematics and Computational Thinking
**Dimension 2 (CCC):** Cause and Effect
**Dimension 3 (DCI):** Newton's Laws of Motion

**Question:** Based on the scenario, calculate the net force acting on the object. Show your work and explain how this force relates to the object's motion.

**Answer Key:** 
- Students should identify all forces acting on the object
- Apply Newton's Second Law (F = ma)
- Show calculations with correct units
- Explain the relationship between net force and acceleration

### Question 2
**Standard:** HS-PS-3-1 (Energy)
**Dimension 1 (SEP):** Developing and Using Models
**Dimension 2 (CCC):** Energy and Matter
**Dimension 3 (DCI):** Conservation of Energy

**Question:** Describe the energy transformations occurring in this system. Create a model showing how energy is conserved throughout the process.

**Answer Key:**
- Identify initial and final energy states
- Describe energy transformations (e.g., kinetic to thermal)
- Demonstrate understanding of energy conservation
- Model should show energy flow accurately

### Question 3
**Standard:** HS-PS-2-3 (Forces and Motion)
**Dimension 1 (SEP):** Engaging in Argument from Evidence
**Dimension 2 (CCC):** Systems and System Models
**Dimension 3 (DCI):** Interactions and Forces

**Question:** Using evidence from the scenario, explain how the forces involved demonstrate Newton's Third Law. Support your argument with specific examples.

**Answer Key:**
- Identify action-reaction force pairs
- Explain equal magnitude and opposite direction
- Provide specific examples from the scenario
- Use evidence to support claims
"""
    
    def get_cost_summary(self) -> dict:
        """Return summary of token usage and estimated cost"""
        # Gemini 1.5 Flash pricing (approximate)
        input_cost_per_1m = 0.075
        output_cost_per_1m = 0.30
        
        input_cost = (self.total_input_tokens / 1_000_000) * input_cost_per_1m
        output_cost = (self.total_output_tokens / 1_000_000) * output_cost_per_1m
        
        return {
            'input_tokens': self.total_input_tokens,
            'output_tokens': self.total_output_tokens,
            'total_tokens': self.total_input_tokens + self.total_output_tokens,
            'estimated_cost_usd': input_cost + output_cost
        }
