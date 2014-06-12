

WORD_TYPES = {
	'verb': ['go', 'goes', 'guess', 'kill', 'kills', 'hit', 'hits', 'eats', 'eat', 'throw', 'chuck', 'shoot'],
	'direction': ['north', 'south', 'east', 'west'],
	'noun': ['bear', 'princess', 'hammer', 'door', 'pod', 'gothon', 'bomb', 'escape pod', 'armory', 'gun'],
	'stop': ['in', 'the', 'of', 'a', 'to', 'by', 'with']
	}

VOCABULARY =  {word: word_type for word_type, words in WORD_TYPES.items() for word in words}

def scan(stuff):
	words = stuff.split()
	val = []
	for word in words:
		if word in VOCABULARY:
			val.append((VOCABULARY[word], word))
		else:
			try:
				number = int(word)
				val.append(('number', number))
			except ValueError:
				val.append(('error', word))
	
	
	# returns a list of tuple pairs of word type and word		
	return val