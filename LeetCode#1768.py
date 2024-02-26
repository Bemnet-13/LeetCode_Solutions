class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        max_length = max(len(word1), len(word2))
        merged_str = ""
        for i in range(max_length):
            if i < len(word1) and i < len(word2):
                merged_str += word1[i] + word2[i]
            elif max_length == len(word1):
                merged_str += word1[i]
            elif max_length == len(word2):
                merged_str += word1[i]
        

        return merged_str