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

# بدء جلسة دردشة جديدة
chat_session = model.start_chat(
    history=[]
)

# دالة لإرسال الرسائل والحصول على استجابة
def send_message(message):
    if not message.strip():
        return "Error: Message cannot be empty."
    
    try:
        response = chat_session.send_message(message)
        return response.text
    except Exception as error:
        return f"An error occurred: {error}"

# إعداد التطبيق الرئيسي
root = tk.Tk()
root.title("Gemini API Demo")
root.geometry("500x400")

# إعداد الأنماط
style = ttk.Style()
style.theme_use("clam")
style.configure("TFrame", background="#282C34")
style.configure("TLabel", background="#282C34", foreground="#ABB2BF", font=("Helvetica", 12))
style.configure("TButton", background="#61AFEF", foreground="#282C34", font=("Helvetica", 12))
style.map("TButton", background=[("active", "#61AFEF")])

# إنشاء إطار رئيسي
main_frame = ttk.Frame(root, padding="20")
main_frame.pack(fill="both", expand=True)

# تسمية الترحيب
welcome_label = ttk.Label(main_frame, text="مرحبًا بك في تطبيق Gemini API", font=("Helvetica", 16, "bold"))
welcome_label.pack(pady=10)

# إدخال المستخدم
input_label = ttk.Label(main_frame, text="أدخل رسالتك:")
input_label.pack(pady=5)
user_input = tk.Entry(main_frame, width=50)
user_input.pack(pady=5)

# استجابة النموذج
response_label = ttk.Label(main_frame, text="استجابة النموذج:")
response_label.pack(pady=5)
response_text = tk.Text(main_frame, width=50, height=10, wrap="word", state="disabled")
response_text.pack(pady=5)

# دالة لإرسال الرسالة وعرض الاستجابة
def on_send_message():
    message = user_input.get()
    response = send_message(message)
    response_text.configure(state="normal")
    response_text.delete("1.0", tk.END)
    response_text.insert(tk.END, response)
    response_text.configure(state="disabled")

# زر الإرسال
send_button = ttk.Button(main_frame, text="إرسال", command=on_send_message)
send_button.pack(pady=10)

# بدء التطبيق
root.mainloop()
