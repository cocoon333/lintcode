"""
648. Unique Word Abbreviation
中文
English

An abbreviation of a word follows the form<first letter><number><last letter>. Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
d) l|ocalizatio|n          --> l10n

Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.
Example

Example1

Input:
[ "deer", "door", "cake", "card" ]
isUnique("dear")
isUnique("cart")
Output:
false
true
Explanation:
Dictionary's abbreviation is ["d2r", "d2r", "c2e", "c2d"].
"dear" 's abbreviation is "d2r" , in dictionary.
"cart" 's abbreviation is "c2t" , not in dictionary.

Example2

Input:
[ "deer", "door", "cake", "card" ]
isUnique("cane")
isUnique("make")
Output:
false
true
Explanation:
Dictionary's abbreviation is ["d2r", "d2r", "c2e", "c2d"].
"cane" 's abbreviation is "c2e" , in dictionary.
"make" 's abbreviation is "m2e" , not in dictionary.
"""

class ValidWordAbbr:
    """
    @param: dictionary: a list of words
    """
    def __init__(self, dictionary):
        self.dict = set()
        self.og_dict = set(dictionary)
        for word in self.og_dict:
            abbr = self._abbreviate(word)
            if abbr in self.dict:
                self.dict.add(abbr+"2")
            else:
                self.dict.add(abbr)

    """
    @param: word: a string
    @return: true if its abbreviation is unique or false
    """
    def isUnique(self, word):
        abbr = self._abbreviate(word)
        if word in self.og_dict:
            if abbr+"2" in self.dict:
                return False
            else:
                return True
        return not abbr in self.dict
        

    def _abbreviate(self, word):
        if len(word) < 3:
            return word
        return word[0] + str(len(word)-2) + word[-1]

if __name__ == "__main__":
    abbr1 = ValidWordAbbr([ "deer", "door", "cake", "card" ])
    abbr2 = ValidWordAbbr([ "a", "a"])
    abbr3 = ValidWordAbbr(['dog'])
    assert(not abbr1.isUnique("dear"))
    assert(not abbr1.isUnique("cane"))
    assert(abbr1.isUnique("make"))
    assert(abbr1.isUnique("cart"))
    assert(abbr2.isUnique('a'))
    assert(abbr3.isUnique('dog'))
