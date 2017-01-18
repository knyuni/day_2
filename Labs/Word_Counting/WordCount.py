
# loop thro the list conting and saving the out 

def words(words):
	a = words.split()
	split_words = []

	for word in b:
		try:
            x2 = int(x)
            split_words.append(x2)
        except:
            split_words.append(x)

    words_dict = {x: split_words.count(x) for x in split_words}

    return words_dict

print(words("hey there people of earth a we have or rather we are people from planet earth b 1 3 5 6 6"))