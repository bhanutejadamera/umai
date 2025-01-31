# tests/test_multimodal_agent.py
import unittest
from src.multimodal_integration.multimodal_agent import MultiModalAgent

class TestMultiModalAgent(unittest.TestCase):
    def test_process_text(self):
        """Test the process_text method of MultiModalAgent."""
        agent = MultiModalAgent()
        result = agent.process_text("Hello, world!")
        self.assertIsInstance(result, str)  # Check if the result is a string

if __name__ == "__main__":
    unittest.main()