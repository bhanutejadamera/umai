# src/multimodal_integration/multimodal_agent.py
import torch
from transformers import CLIPProcessor, CLIPModel
from transformers import pipeline

class MultiModalAgent:
    def __init__(self):
        # Load pre-trained CLIP model for vision-language tasks
        self.clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
        self.clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

        # Load a pre-trained NLP model for text-based tasks
        self.nlp_model = pipeline("text-generation", model="gpt2")

    def process_text(self, text):
        """Generate text using a pre-trained NLP model."""
        return self.nlp_model(text, max_length=50, num_return_sequences=1)[0]['generated_text']

    def process_image_text(self, image, text):
        """Compare an image and text using CLIP."""
        inputs = self.clip_processor(text=text, images=image, return_tensors="pt", padding=True)
        outputs = self.clip_model(**inputs)
        logits_per_image = outputs.logits_per_image  # Image-text similarity score
        return logits_per_image

# Example usage
if __name__ == "__main__":
    agent = MultiModalAgent()
    text_output = agent.process_text("Explain the concept of AI.")
    print("Generated Text:", text_output)
