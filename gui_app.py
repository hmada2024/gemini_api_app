# gui_app.py ملف
import tkinter as tk
from tkinter import ttk

# إعداد التطبيق الرئيسي
root = tk.Tk()
root.title("Gemini API Demo")
root.geometry("500x400")

# إعداد الأنماط
style = ttk.Style()
style.theme_use("clam")  # اختيار الثيم
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

# دالة لإرسال الرسائل
def send_message():
    message = user_input.get()
    if not message.strip():
        response_text.configure(state="normal")
        response_text.delete("1.0", tk.END)
        response_text.insert(tk.END, "Error: Message cannot be empty.")
        response_text.configure(state="disabled")
        return
    
    # من المفترض هنا أن يتم استدعاء دالة send_message من API الخاص بك
    # هذا مجرد مثال، يجب تعديل هذا الجزء ليتناسب مع كود API الخاص بك
    response = "استجابة وهمية من النموذج"  # هذا مجرد مثال، ضع الكود الخاص بك هنا
    
    response_text.configure(state="normal")
    response_text.delete("1.0", tk.END)
    response_text.insert(tk.END, response)
    response_text.configure(state="disabled")

# زر الإرسال
send_button = ttk.Button(main_frame, text="إرسال", command=send_message)
send_button.pack(pady=10)

# بدء التطبيق
root.mainloop()
