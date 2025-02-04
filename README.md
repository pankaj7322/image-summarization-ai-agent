# Image Summarization AI Agent

This is an AI-powered image summarization tool that allows users to upload an image, and it will generate a caption describing the content of the image. The system uses a fine-tuned Vision-Transformer (ViT) model combined with GPT-2 for generating natural language descriptions of images.

## Features

- Upload an image (JPG, PNG, JPEG)
- Automatically generate captions describing the content of the image
- Built using Streamlit for the interface and Hugging Face models for image captioning

## Technologies Used

- **Streamlit**: For creating the interactive web app
- **Transformers (Hugging Face)**: For the image captioning model (`nlpconnect/vit-gpt2-image-captioning`)
- **PIL (Pillow)**: For image processing
- **Requests**: For making HTTP requests (if necessary)

## Installation

### Requirements
- Python 3.7+
- `pip`

### Steps to Run the Project Locally

1. Clone this repository:
    ```bash
    git clone (https://github.com/pankaj7322/image-summarization-ai-agent)
    cd image-summarization-ai-agent
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

5. Once the app starts, open the provided URL (typically `http://localhost:8501`) to access the image summarization interface.

## Usage

1. Upload an image in JPG, PNG, or JPEG format.
2. The model will automatically generate a caption describing the content of the image and display it below the uploaded image.


## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Open a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Hugging Face Transformers and Model Zoo for the pre-trained models
- Streamlit for making web applications simple to build
- The authors of ViT and GPT-2 for their excellent work on the models used in this project
