from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from PIL import Image
from textblob import TextBlob
import io
import base64
import speech_recognition as sr
from deep_translator import GoogleTranslator

app = FastAPI()

# Function to convert an image to grayscale
def convert_to_grayscale(image: Image.Image) -> Image.Image:
    return image.convert('L')  # Convert image to grayscale

@app.get("/", response_class=HTMLResponse)
async def get_upload_page():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Upload Image, Text, or Audio</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #e0e5ec;
                margin: 0;
                padding: 0;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
            }
            h1 {
                color: #333;
                font-size: 2.5em;
            }
            form {
                background-color: #fff;
                padding: 20px;
                border-radius: 12px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                margin-bottom: 20px;
                width: 100%;
                max-width: 450px;
                transition: all 0.3s ease;
            }
            form:hover {
                box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
            }
            input, textarea, button {
                width: calc(100% - 20px);
                padding: 12px;
                margin: 10px 0;
                border-radius: 8px;
                border: 1px solid #ccc;
                font-size: 16px;
                outline: none;
                transition: border-color 0.3s;
            }
            input:focus, textarea:focus {
                border-color:  #210c8c;
            }
            button {
                background-color: #210c8c;
                color: white;
                cursor: pointer;
                border: none;
                transition: background-color 0.3s, transform 0.3s;
            }
            button:hover {
                background-color: #210c8c;
                transform: translateY(-2px);
            }
            .container {
                text-align: center;
            }
            .link {
                text-decoration: none;
                color: #2020a5;
                font-weight: bold;
                transition: color 0.3s;
            }
            .link:hover {
                color:  #210c8c;
            }
            @media (max-width: 600px) {
                form {
                    width: 90%;
                }
                h1 {
                    font-size: 2em;
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Upload Image, Text, or Audio</h1>
            <form action="/upload/image/" method="post" enctype="multipart/form-data">
                <h2>Image Upload</h2>
                <input type="file" name="file" accept="image/jpeg, image/png" required>
                <button type="submit">Upload Image</button>
            </form>
            <form action="/upload/text/" method="post">
                <h2>Text Input</h2>
                <textarea name="text" rows="4" cols="50" required placeholder="Enter your text here..."></textarea>
                <button type="submit">Correct Text</button>
            </form>
            <form action="/upload/audio/" method="post" enctype="multipart/form-data">
                <h2>Audio Upload</h2>
                <input type="file" name="file" accept="audio/mpeg, audio/wav" required>
                <button type="submit">Upload Audio</button>
            </form>
        </div>
    </body>
    </html>
    """

# The other endpoint functions (upload_image, upload_text, and upload_audio) remain the same as before.
