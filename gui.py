import tkinter as tk
from tkinter import messagebox
from analyzer import PasswordStrengthAnalyzer
from generator import WordlistGenerator

class PasswordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Strength Analyzer & Wordlist Generator")
        self.root.geometry("550x600")

        tk.Label(root, text="🔑 Enter Password:").pack()
        self.password_entry = tk.Entry(root, show="*", width=40)
        self.password_entry.pack()

        tk.Button(root, text="Check Strength", command=self.check_strength).pack(pady=10)

        self.result_label = tk.Label(root, text="", fg="blue", justify="left")
        self.result_label.pack()

        tk.Label(root, text="\nCustom Wordlist Inputs").pack()
        self.name_entry = self._input_field("Name")
        self.dob_entry = self._input_field("DOB (e.g. 1999)")
        self.pet_entry = self._input_field("Pet Name")

        tk.Button(root, text="Generate Sample Wordlist", command=self.generate_wordlist).pack(pady=10)

        self.wordlist_label = tk.Label(root, text="", fg="green", justify="left")
        self.wordlist_label.pack()

    def _input_field(self, label_text):
        tk.Label(self.root, text=label_text).pack()
        entry = tk.Entry(self.root, width=40)
        entry.pack()
        return entry

    def check_strength(self):
        pwd = self.password_entry.get()
        if not pwd:
            return messagebox.showwarning("Input Error", "Please enter a password.")
        analyzer = PasswordStrengthAnalyzer()
        strength, feedback = analyzer.analyze_password(pwd)
        verdict = "Weak" if strength < 50 else "Moderate" if strength < 80 else "Strong"
        result_text = f"Strength: {strength:.1f}% ({verdict})\n" + "\n".join(feedback)
        self.result_label.config(text=result_text)

    def generate_wordlist(self):
        name = self.name_entry.get()
        dob = self.dob_entry.get()
        pet = self.pet_entry.get()
        generator = WordlistGenerator(name=name, dob=dob, pet=pet)
        sample = generator.generate_wordlist()[:15]
        self.wordlist_label.config(text="Sample Wordlist:\n" + "\n".join(sample))

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordApp(root)
    root.mainloop()