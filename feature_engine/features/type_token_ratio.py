"""
file: type_token_ratio.py
---
Defines a feature that outputs the word type-token ratio.
"""

from features.word_count import *
  
"""
function: get_word_TTR
@param text: The message for which we are calculating the word type-token ratio.
Recall that the type-token ratio is equal to (# of unique words) / (# of total words).
The output of this function should be a number (specifically, a float).
Example: “Please, oh please can I go to the ball?” → 8 / 9 → 0.889
"""
def get_word_TTR(text):
	
	word_list = text.split()
	unique_list = []
	duplicate_list = []

	for word in word_list:
		if word not in unique_list:
			unique_list.append(word)
		else:
			duplicate_list.append(word)
		
	
	print(duplicate_list)
	print(unique_list)
		

	return ((len(word_list) - len(duplicate_list))/len(word_list))