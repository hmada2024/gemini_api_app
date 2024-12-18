import tkinter as tk
from tkinter import ttk
from api import send_message

class GeminiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gemini API Demo")
        self.root.geometry("800x600")

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TFrame", background="#282C34")
        self.style.configure("TLabel", background="#282C34", foreground="#ABB2BF", font=("Helvetica", 12))
        self.style.configure("TButton", background="#61AFEF", foreground="#282C34", font=("Helvetica", 12))
        self.style.map("TButton", background=[("active", "#61AFEF")])

        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(fill="both", expand=True)

        self.welcome_label = ttk.Label(self.main_frame, text="مرحبًا بك في تطبيق Gemini API", font=("Helvetica", 16, "bold"))
        self.welcome_label.pack(pady=10)

        self.input_label = ttk.Label(self.main_frame, text="أدخل رسالتك:")
        self.input_label.pack(pady=5)
        self.user_input = tk.Text(self.main_frame, width=60, height=10, wrap="word")
        self.user_input.pack(pady=5)

        self.response_label = ttk.Label(self.main_frame, text="استجابة النموذج:")
        self.response_label.pack(pady=5)
        self.response_text = tk.Text(self.main_frame, width=60, height=10, wrap="word", state="disabled")
        self.response_text.pack(pady=5)

        self.send_button = ttk.Button(self.main_frame, text="إرسال", command=self.on_send_message)
        self.send_button.pack(pady=10)

        self.user_input.bind("<3>", lambda e: self.paste_content())

    def on_send_message(self):
        message = self.user_input.get("1.0", tk.END).strip()
        response = send_message(message)
        self.response_text.configure(state="normal")
        self.response_text.delete("1.0", tk.END)
        self.response_text.insert(tk.END, response)
        self.response_text.configure(state="disabled")
        self.response_text.tag_add("green", "1.0", tk.END)
        self.response_text.tag_config("green", foreground="green")

    def paste_content(self):
        try:
            content = self.root.clipboard_get()
            self.user_input.insert(tk.END, content)
        except tk.TclError:
            pass

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = GeminiApp(root)
    app.run()