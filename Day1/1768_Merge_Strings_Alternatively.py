class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = str()
        if len(word1) > len(word2):
            for letter1, letter2 in zip(word1[: len(word2)], word2):
                word += letter1
                word += letter2
            word += word1[len(word2) :]
        elif len(word1) < len(word2):
            for letter1, letter2 in zip(word1, word2[: len(word1)]):
                word += letter1
                word += letter2
            word += word2[len(word1) :]
        else:
            for letter1, letter2 in zip(word1, word2):
                word += letter1
                word += letter2
        return word
