translations = {
    "hello": "வணக்கம்",
    "good morning": "காலை வணக்கம்",
    "thank you": "நன்றி",
    "how are you": "நீங்கள் எப்படி இருக்கிறீர்கள்?"
}

text = input("Enter English text: ").lower()

if text in translations:
    print("Tamil:", translations[text])
else:
    print("Translation not found")