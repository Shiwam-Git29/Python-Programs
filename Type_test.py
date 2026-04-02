#PROJECT 3 :- Typing Test   

import time     #time modeule used for time related functions
import random   #random module used for generating random numbers


sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a great programming language.",
    "Typing speed tests can be fun and challenging.",
    "Practice makes perfect when it comes to typing.",
]
def measure_accuraccy(user_input, sentence):
    correct_chars = sum(1 for u, s in zip(user_input, sentence) if u == s)
    total_chars = len(sentence)
    accuracy = (correct_chars / total_chars) * 100 if total_chars > 0 else 0
    return accuracy





def typing_test():
    sentence = random.choice(sentences)  # Select a random sentence
    print("Type the following sentence:")
    print(sentence)
    input("Press Enter when you're ready...")
    start_time = time.time()      # Messure Start the timer
    user_input = input("\nStart typing: \n")  # Get user input
    end_time = time.time()    # Measure End the timer
    time_taken = end_time - start_time  # Calculate time taken
    time_taken_in_minutes = time_taken / 60  # Convert time to minutes
    word_count = len(sentence.split(" "))  # Count the number of words in the sentence
    
    print("results:")
    print(f"Time taken: {time_taken_in_minutes:.2f} minutes")
   
    print(f"Number of words in sentence: {word_count}")
    print(f"Words per minute: {word_count / time_taken_in_minutes if time_taken_in_minutes > 0 else 0:.2f}")
    Accuracy = measure_accuraccy(user_input, sentence)
    print(f"Accuracy: {Accuracy:.2f}%")
    

typing_test()





