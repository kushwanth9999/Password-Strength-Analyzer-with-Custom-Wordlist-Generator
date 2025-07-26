from analyzer import PasswordStrengthAnalyzer
from generator import WordlistGenerator

def main():
    print("\n🔐 Password Strength Analyzer & Wordlist Generator")

    name = input("Enter your name (optional): ")
    dob = input("Enter DOB (e.g., 1999 or 12081999): ")
    pet = input("Enter pet name (optional): ")

    generator = WordlistGenerator(name=name, dob=dob, pet=pet)
    wordlist = generator.generate_wordlist()
    generator.export_wordlist()

    print(f"\n✅ Wordlist generated with {len(wordlist)} entries. Saved as wordlist.txt")

    analyzer = PasswordStrengthAnalyzer()

    while True:
        pwd = input("\n🔎 Enter password to analyze (or 'q' to quit): ")
        if pwd.lower() == 'q':
            break
        strength, feedback = analyzer.analyze_password(pwd)
        print(f"Strength: {strength:.1f}%")
        for f in feedback:
            print(" -", f)

if __name__ == "__main__":
    main()