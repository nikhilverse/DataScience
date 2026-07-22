import time
import random

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing speed tests are a great way to improve your typing skills.",
    "Practice makes perfect when it comes to typing.",
    "Focus on accuracy first, then speed.",
    "Regular practice is key to improving your typing speed."
]

def typing_speed_test():
    sentence = random.choice(sentences)
    print("Type the following sentence :")
    print(sentence)
    print("\nPress Enter when you are ready to start!!")
    input()
    start_time = time.time()
    user_input = input("Start typing:")
    end_time = time.time()
    time_taken = end_time - start_time
    print(f"\nTime Taken: {time_taken:.2f} seconds")
    print(f"Characters Typed: {len(user_input)}")
    words_typed = len(user_input.split())
    print(f"Words Typed: {words_typed}")
    print(f"Typing Speed: {words_typed / (time_taken / 60):.2f} words per minute")
typing_speed_test()
