# your code goes here!
anagram = ['enlists', 'google', 'inlets', 'banana']

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, anagram):
        sort_words = sorted(self.word)
        matches = [anagram for anagram in anagram if sort_words == sorted(anagram)]
        return matches
    
checker = Anagram("listen")
anagram = checker.match(anagram)
print(anagram)
