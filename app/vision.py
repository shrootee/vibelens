from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# Load model once at startup
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_description(image: Image.Image):
    """
    Takes a PIL Image and returns a caption string.
    """
    inputs = processor(image, return_tensors="pt")
    output = model.generate(**inputs)
    caption = processor.decode(output[0], skip_special_tokens=True)
    return caption