import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class ConstructionPromptImprover:
    def __init__(self):
        """Initialize the prompt improver with OpenAI."""
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable is not set")
            
        openai.api_key = api_key
        
        # System prompt that guides the LLM
        self.system_prompt = """You are a specialized construction claims expert. 
        Your task is to improve informal construction claim prompts into well-structured, 
        legally-sound queries. Focus on:
        1. Proper construction terminology
        2. Relevant contractual context
        3. Required documentation references
        4. Clear causation and impact analysis
        5. Legal and technical precision
        
        Maintain the original intent while adding necessary context and structure."""

    def improve_prompt(self, raw_prompt: str) -> str:
        """
        Improve a raw construction claim prompt using the OpenAI API.
        
        Args:
            raw_prompt (str): The original, unstructured prompt
            
        Returns:
            str: The improved, structured prompt
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",  # Using GPT-4 for better understanding of construction context
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": f"Please improve this construction claim prompt: {raw_prompt}"}
                ],
                temperature=0.7,
                max_tokens=500
            )
            
            return response['choices'][0]['message']['content'].strip()
            
        except Exception as e:
            return f"Error improving prompt: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Test cases
    test_prompts = [
        "eot due to material delay. how to justify?",
        "client not paying for variation works",
        "weather delay claim help"
    ]
    
    improver = ConstructionPromptImprover()
    
    print("Testing prompt improver with example cases:\n")
    for prompt in test_prompts:
        print(f"Original prompt: {prompt}")
        improved = improver.improve_prompt(prompt)
        print(f"Improved prompt: {improved}\n")