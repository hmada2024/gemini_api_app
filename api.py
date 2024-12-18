# api.py ملف
import os
import google.generativeai as genai
import tkinter as tk
from tkinter import ttk

# تكوين مكتبة genai باستخدام مفتاح API
api_key = 'AIzaSyD81bpZqeJjOJWqlkY2e4lgrYuhzL8a8r4'
genai.configure(api_key=api_key)

# إعدادات توليد النموذج
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# إنشاء نموذج التوليد
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
    generation_config=generation_config,
)

# Start chat session
chat_session = model.start_chat(history=[])

# Function to send messages and get responses
def send_message(message):
    if not message.strip():
        return "Error: Message cannot be empty."
    
    try:
        response = chat_session.send_message(message)
        return response.text
    except Exception as error:
        return f"An error occurred: {error}"