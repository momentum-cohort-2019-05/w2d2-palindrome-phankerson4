user_enter_text = str(input("Enter some text (can be a phrase, sentence, or multiple sentences ) "))
"""Accepts user input of text strings"""
all_letters = "abcdefghijklmnopqrstuvwxyz"
"""Create a variable that contains all the letters of the alphabet"""
user_enter_text = user_enter_text.lower()
""""Returns lowercased string from text input by user"""
found_letters = []
backward_letters = []
"""Create empty variables"""

for character in user_enter_text:
    if character in all_letters:
        found_letters.append(character)
        backward_letters.append(character)
backward_letters.reverse()
    
if found_letters == backward_letters:
    print(user_enter_text + " is a palidrome!")
else:
    print(user_enter_text + " is not a palidrome!")
        

