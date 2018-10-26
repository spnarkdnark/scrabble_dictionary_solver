scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                              for letter in letters.split()}

def load_words(filename):
	"""Load dictionary into a list and return list"""
	with open(filename) as fobj:
		lines = fobj.readlines()
	return [line.strip() for line in lines]
	
def calc_word_value(word):
	"""Calculate the value of the word entered into function
	using imported constant mapping LETTER_SCORES"""
	score = 0
	for letter in word.upper():
		if letter in LETTER_SCORES.keys():
			score += LETTER_SCORES[letter]
	return score

def max_word_value(dictionary):
	"""Calculate the word with the max value, can receive a list
	of words as arg, if none provided uses default DICTIONARY"""
	best_value = 0
	best_word = ''
	for word in dictionary:
		value = calc_word_value(word)
		if value > best_value:
			best_word = word
			best_value = value
	return [best_word,best_value]

def main():
	"""Run the main program"""
	print("Importing dictionary...")
	dictionary_list = load_words('dictionary.txt')
	print("Searching a list of " + str(len(dictionary_list)) + " words...")
	best = max_word_value(dictionary_list)
	print("The best word is " + best[0] + " with a score of " + str(best[1]) + "!")
	
main()
