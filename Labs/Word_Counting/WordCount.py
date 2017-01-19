def words(words):
  a = words.split()
  split_words = []
  for word in a:
    try:
      x = int(word)
      split_words.append(x)
    except:
      split_words.append(word)

  words_dict = {word: split_words.count(word) for word in split_words}

  return words_dict
a=words("hey there people of earth a we have or rather we are people from planet earth b")
print(words(a))