def firstRecurring(givenString):
	"""
	Return the first recurring character in a string that is passed in

	e.g.    ABCA    - should return A
			BCABA   - should return B
			ABC     - should return null


	Both of the loops do the same thing however, one uses a list, the
	other a dictionary
	"""
	charArr = []
	charDict = {}



	# loop through the string
	for char in givenString:
		# for each letter, check if the letter is already in the list 
		# and return it if it is
		if char in charArr:
			return char
		
		# otherwise add that letter to the list
		charArr.append(char)


	for char in givenString:
		if char in charDict:
			return char
		charDict[char] = 1

if __name__ == "__main__":
	print(firstRecurring('DBCBA'))