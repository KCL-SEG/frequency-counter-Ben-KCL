"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
	frequencies = {}
	for item in items:
		item = str(item)
		if item not in frequencies:
			frequencies[item] = 1
		else:
			orig = frequencies[item]
			frequencies[item] = orig + 1
	return frequencies
