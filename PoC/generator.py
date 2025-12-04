import time

class ClusterGenerator:
    def __init__(self, model_name: str = "gemini-1.5-flash"):
        self.model_name = model_name

    def generate_cluster(self, context: str, stimulus: str) -> str:
        """
        Constructs the prompt and simulates an LLM call to generate a Physics Cluster.
        """
        
        system_instruction = """
You are an expert NY State Regents Physics Teacher and Exam Creator.
Your goal is to create a "Cluster" of exam questions based on a provided Stimulus and relevant Standards.
A Cluster consists of:
1. A Stimulus (Scenario description)
2. 1-3 Questions that test the student's ability to apply the standards to the stimulus.

Use the provided Standards and Performance Level Descriptors (PLDs) as your source of truth.
"""

        prompt = f"""
{system_instruction}

--- RELEVANT STANDARDS & PLDS (CONTEXT) ---
{context}
-------------------------------------------

--- STIMULUS ---
{stimulus}
----------------

Please generate a Physics Cluster in Markdown format.
"""

        print(f"\n[Generator] Constructing prompt with {len(prompt)} characters...")
        print(f"[Generator] Simulating call to {self.model_name}...")
        
        # Simulate network latency
        time.sleep(1.5)
        
        # Mock Response
        mock_response = f"""
# Generated Physics Cluster

## Stimulus
{stimulus}

## Questions

### Question 1
**Standard:** HS-PS-2-1 (Forces)
**Question:** Based on the scenario, calculate the net force acting on the object. Show your work.
**Answer Key:** [Calculation steps...]

### Question 2
**Standard:** HS-PS-3-1 (Energy)
**Question:** Describe how energy is transformed in this system.
**Answer Key:** Kinetic energy is converted to thermal energy...
"""
        
        return mock_response
