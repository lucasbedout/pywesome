from types import LambdaType
from random import randint

def map(collection, function):
	mapped_collection = []
	for item in collection:
		mapped_collection.append(function(item))
	return mapped_collection

def reduce(collection, function, carry=None):
	if not carry:
		carry = collection[0]
		collection.pop(0)
	for item in collection:
		carry = function(carry, item)
	return carry

def filter(collection, function):
	filtered_collection = []
	for item in collection:
		if function(item):
			filtered_collection.append(item)
	return filtered_collection

def reject(collection, function):
	filtered_collection = []
	for item in collection:
		if not function(item):
			filtered_collection.append(item)
	return filtered_collection

def contains(haystack, needle):
	if isinstance(needle, LambdaType):
		for item in haystack:
			if needle(item):
				return True
		return False
	return needle in haystack

def search(haystack, needle):
	for index, item in enumerate(haystack):
		if item == needle or (isinstance(needle, LambdaType) and needle(item)):
			return index
	return False

def random(collection, offset=1):
	indexes = []
	results = []
	for i in range(offset):
		index = random_number(0, len(collection) - 1, indexes)
		results.append(collection[index]) 
	return results[0] if len(results) == 1 else results

'''
Helpers (not related to collections)
Could be moved elsewhere at some point
'''

def random_number(start, end, rejects=[]):
	index = randint(start, end)
	if index in rejects:
		return random_number(start, end, rejects)
	return index
