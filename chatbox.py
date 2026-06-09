faq = {
    "hi": "Hello! How can I help you?",
    "what is ai": "AI stands for Artificial Intelligence.",
    "what is python": "Python is a programming language.",
    "bye": "Goodbye!"
}

question = input("Ask a question: ").lower()

if question in faq:
    print(faq[question])
else:
    print("Sorry, I don't know the answer.")