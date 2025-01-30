# src/task_automation/generative_ai.py
from transformers import pipeline

class TaskAutomation:
    def __init__(self):
        self.generator = pipeline("text-generation", model="gpt2")

    def generate_code(self, prompt):
        """Generate code or scripts using a generative AI model."""
        response = self.generator(prompt, max_length=100, num_return_sequences=1)
        return response[0]['generated_text']

# Example usage
if __name__ == "__main__":
    automator = TaskAutomation()
    code = automator.generate_code("Write a Python function to calculate factorial.")
    print("Generated Code:", code)
