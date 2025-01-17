import streamlit as st
import requests
from PIL import Image
from transformers import GPT2TokenizerFast, ViTImageProcessor, VisionEncoderDecoderModel

# Load the fine-tuned image captioning model and corresponding tokenizer and image processor
model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = GPT2TokenizerFast.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
image_processor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

# Function to generate caption from image
def generate_caption(image):
    # Process the image for the model
    pixel_values = image_processor(image, return_tensors="pt").pixel_values
    
    # Autoregressively generate caption (uses greedy decoding by default)
    generated_ids = model.generate(pixel_values)
    
    # Decode generated tokens to text
    generated_text = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    
    return generated_text

# Streamlit interface
def image_summarization_agent():
    st.title("Image Summarization AI Agent")
    
    # Upload image
    uploaded_image = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])
    
    if uploaded_image is not None:
        # Open the uploaded image using PIL
        image = Image.open(uploaded_image)
        
        # Display the uploaded image
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        # Generate the caption for the image
        caption = generate_caption(image)
        
        # Display the generated caption
        st.subheader("Generated Caption:")
        st.write(caption)

# Run the Streamlit app
if __name__ == "__main__":
    image_summarization_agent()
