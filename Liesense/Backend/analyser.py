import random

# Simple NLP-based logic (upgrade later with OpenAI)

def analyze_text(text):
    suspicious_words = ["maybe", "I think", "not sure", "probably", "idk"]
    
    score = 80
    
    for word in suspicious_words:
        if word in text.lower():
            score -= 10

    # random variation to simulate AI
    score += random.randint(-10, 10)

    return max(0, min(100, score))


def analyze_voice(audio_path=None):
    # Placeholder for voice analysis
    return random.randint(30, 90)