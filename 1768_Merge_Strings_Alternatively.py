class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        if len(word1) > len(word2):
            for letter1, letter2 in zip(word1[: len(word2)], word2):
                merged.extend([letter1, letter2])
            merged.extend(word1[len(word2) :])
        elif len(word1) < len(word2):
            for letter1, letter2 in zip(word1, word2[: len(word1)]):
                merged.extend([letter1, letter2])
            merged.extend(word2[len(word1) :])
        else:
            for letter1, letter2 in zip(word1, word2):
                merged.extend([letter1, letter2])
        return "".join(merged)
