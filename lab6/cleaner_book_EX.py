#!/usr/bin/env python

import string, re

class Book:
	def __init__(self, filename):

		print 'In init:'
		self.f = open(filename, 'r')
		self.words = []
		for line in self.f:
			for word in line.split():
				self.words.append(word.lower())

		self.words = sorted(self.words)		
		self.unique = set()
		print self.words[1:300]

		for line in self.f:
			for word in line.split():
				self.words.append(word.lower())

		self.words_san_hyphen = [e for e in self.words]

		for element in self.words_san_hyphen:				
			try:
				str_1, str_2, str_3 = element.split("--")
				#print element, str_1, str_2, str_3
				self.words_san_hyphen.remove(element)
				self.words_san_hyphen.append(str_1)
				self.words_san_hyphen.append(str_2)
				self.words_san_hyphen.append(str_3)
			except:
				pass

		for element in self.words_san_hyphen:				
			try:
				str_1, str_2, str_3 = element.split("-")
				#print element, str_1, str_2, str_3
				self.words_san_hyphen.remove(element)
				self.words_san_hyphen.append(str_1)
				self.words_san_hyphen.append(str_2)
				self.words_san_hyphen.append(str_3)
			except:
				pass

		for element in self.words_san_hyphen:
			try:
				str_1, str_2 = element.split("--")
				#print element, str_1, str_2
				self.words_san_hyphen.remove(element)
				self.words_san_hyphen.append(str_1)
				self.words_san_hyphen.append(str_2)
			except:
				pass

		for element in self.words_san_hyphen:
			try:
				str_1, str_2 = element.split("-")
				#print element, str_1, str_2
				self.words_san_hyphen.remove(element)
				self.words_san_hyphen.append(str_1)
				self.words_san_hyphen.append(str_2)
			except:
				pass

		for element in self.words_san_hyphen:
			element = element.translate(None, string.punctuation)
			if element in self.unique:
				pass
			else:
				self.unique.add(element)

		print 'Got', len(self.unique), 'unique words from text.'
	
	def number_of_words(self):

		print 'In number_of_words function:'
		print 'Got', len(self.words), 'words from text.'
		return len(self.words)

	def __sub__(self, other):

		print 'In sub function'
		print 'Got', len(list(self.unique - other.unique)), 'words from text a not in text b.'
		return list(sorted(self.unique - other.unique))
	


if __name__ == '__main__':

	book = Book('war_and_peace.txt')
	d = Book('words')
	#print book.number_of_words()
	#print d.number_of_words()
	#print book -d






