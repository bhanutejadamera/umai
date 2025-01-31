# src/umai_framework.py
from src.multimodal_integration.multimodal_agent import MultiModalAgent
from src.distributed_execution.spark_executor import SparkExecutor
from src.optimization_engine.optimizer import Optimizer
from src.task_automation.generative_ai import TaskAutomation

class UMAI:
    def __init__(self):
        self.multimodal_agent = MultiModalAgent()
        self.spark_executor = SparkExecutor()
        self.optimizer = Optimizer()
        self.task_automator = TaskAutomation()

    def run(self):
        print("Running UMAI...")
        # Example workflow
        text_output = self.multimodal_agent.process_text("Explain AI.")
        print("Text Output:", text_output)

        optimization_result = self.optimizer.optimize()
        print("Optimization Result:", optimization_result)

        generated_code = self.task_automator.generate_code("Write a Python function to calculate factorial.")
        print("Generated Code:", generated_code)

# Example usage
if __name__ == "__main__":
    umai = UMAI()
    umai.run()