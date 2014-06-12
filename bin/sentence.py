class ParserError(Exception):
	pass
	
class Sentence(object):

	def __init__(self, subject, verb, object_):
		print "Creating sentence", subject, verb, object_
		# remember we take ('noun','princess') tuples and convert them
		# ??Each argument 'subject', 'verb', 'object' is a tuple containing the code and word ??
		self.subject = subject
		self.verb = verb
		self.object_ = object_

	def __eq__(self, other):
		return (self.subject == other.subject and
				self.verb == other.verb and
				self.object_ == other.object_)


	
def peek(word_list):
	# word_list is a list of tuples in the form (type, word).
	# This method returns the code of the first tuple in the list
	print "word_list in parser", word_list
	if word_list:
		key, value = word_list[0]
		print "key", key
		return key
	else: 
		return None
		
def match(word_list, expecting):

#  Returns the first word if it matches the expecting type, else returns None.
#  In any case, the first word will be removed from the word_list
	if word_list:
		wordpair = word_list.pop(0)
		print "wordpair", wordpair
		key, value = wordpair
		
		if key == expecting:
			return value
			
		else:
			return None
	else:
		return None
	
def skip(word_list, word_type):
	while peek(word_list) == word_type:
		match(word_list, word_type)

		
def parse_verb(word_list):
	skip(word_list, 'stop')
	
	if peek(word_list) == 'verb':
		return match(word_list, 'verb')
	else:
		raise ParserError("Expected a verb next")
		
def parse_object(word_list):
	skip(word_list, 'stop')
	next = peek(word_list)
	
	if next == 'noun':
		return match(word_list, 'noun')
	if next =='direction':
		return match(word_list, 'direction')
	else:
		raise ParserError("Expected a noun or a direction next")

def parse_number(word_list):
	skip(word_list, 'stop')

	if peek(word_list) == 'number':
		return match(word_list, 'number')
	else:
		raise ParserError()
	
def parse_subject(word_list, subj):

	skip (word_list, 'stop')
	verb = parse_verb(word_list)
	try:
		obj = parse_number(word_list)
	except ParserError:
		obj = parse_object(word_list)
	
	return Sentence(subj, verb, obj)


	
def parse_sentence(word_list):
	skip(word_list, 'stop')
	start = peek(word_list)
	
	if start == 'noun':
		subj = match(word_list, 'noun')
		return parse_subject(word_list, subj)
	elif start == 'verb':
		# assume the subject is the player then
		return parse_subject(word_list, ('player'))
	elif start =='number':
		num = match(word_list, 'number')
		return Sentence('player', 'guess', num)
	else:
		raise ParserError("must start with subject object or verb, not: %s" % start)
		