from zxcvbn import zxcvbn

class PasswordStrengthAnalyzer:
    def analyze_password(self, password):
        result = zxcvbn(password)
        score = result['score']
        feedback = result['feedback']
        suggestions = feedback.get('suggestions', [])
        warning = feedback.get('warning', '')

        strength_percent = (score / 4) * 100
        feedback_msgs = suggestions.copy()
        if warning:
            feedback_msgs.insert(0, warning)
        return strength_percent, feedback_msgs