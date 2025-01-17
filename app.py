import streamlit as st
import cv2
import numpy as np
import tensorflow as tf
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
from PIL import Image

model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
processor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("gpt2")

def load_and_process_image(image):
    inputs = processor(images=image,return_tensors="pt")
    return inputs

def generate_caption(image):
    inputs = load_and_process_image(image)

    output_ids = model.generate(**inputs, max_length=16, num_beams=4, no_repeat_ngram_size = 2)

    caption = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    return caption


