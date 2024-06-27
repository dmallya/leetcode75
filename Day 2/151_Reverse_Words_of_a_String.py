class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.strip().split(" ")
        clean_list = []
        for word in word_list:
            if len(word) > 0:
                word.strip()
                clean_list.append(word)
                print(len(word))
        return " ".join(clean_list[::-1])
