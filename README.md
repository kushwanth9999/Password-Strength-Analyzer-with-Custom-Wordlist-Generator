# 🔐 Password Strength Analyzer with Custom Wordlist Generator

A Python-based tool to analyze password strength and generate custom wordlists tailored for penetration testing and cybersecurity practice.

## 🚀 Features

- **Password Strength Analysis** using [zxcvbn](https://github.com/dropbox/zxcvbn)
- **Custom Wordlist Generator** based on user inputs (Name, DOB, Pet)
- **Leetspeak Conversion** + Common Patterns + Year Suffixing
- **GUI Interface** built with `tkinter`
- No export required – wordlist samples shown directly in the app

---

## 🧰 Tools & Technologies

- Python 3.x
- [zxcvbn](https://pypi.org/project/zxcvbn/)
- Tkinter
- Random, String, Datetime

---

## 🖥️ Interface

### 💡 GUI Preview
- Input password and get feedback + verdict
- Enter personal keywords (like name, DOB) to generate sample wordlist suggestions

### 📦 CLI Mode
```bash
python main.py
```
Provides text-based password analysis and wordlist generation.

---

## 📁 Project Structure

```
📦 PasswordTool
├── analyzer.py         # zxcvbn-based password analyzer
├── generator.py        # Custom + leetspeak wordlist generator
├── main.py             # CLI interface
├── gui.py              # Tkinter GUI interface
└── README.md           # Project documentation
```

---

## 🔧 Installation

1. **Clone the repo**:
```bash
git clone https://github.com/your-username/password-strength-analyzer.git
cd password-strength-analyzer
```

2. **Install dependencies**:
```bash
pip install zxcvbn
```

3. **Run the GUI**:
```bash
python gui.py
```

---

## ✅ Sample Wordlist Output (GUI)

Example suggestions:
```
john1999
j0hn2023
fluffy2025
123456
welcome
Test@2025
...
```

---

## 🧪 Use Cases

- Password hygiene education
- Cybersecurity training
- Wordlist crafting for ethical hacking
- Practicing brute-force scenarios with customized lists

---

## 🧑‍💻 Author

**Kushwanth P**  
Built during my internship at **Elevate Labs**  
GitHub: [kushwanth9999](https://github.com/kushwanth9999)

---

## 📜 License

This project is open-source and free to use under the MIT License.