class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        word = str()

        for letter in s:
            if letter.lower() in ["a", "e", "i", "o", "u"]:
                vowels.append(letter)

        for letter in s:
            if letter.lower() in ["a", "e", "i", "o", "u"]:
                word += vowels[-1]
                del vowels[-1]
            else:
                word += letter

        return word
