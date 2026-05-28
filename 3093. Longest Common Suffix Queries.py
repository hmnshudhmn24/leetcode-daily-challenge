from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_idx = -1

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        root = TrieNode()

        def is_better(idx1, idx2):
            if idx2 == -1:
                return True
            len1 = len(wordsContainer[idx1])
            len2 = len(wordsContainer[idx2])
            if len1 != len2:
                return len1 < len2
            return idx1 < idx2

        best_overall = -1
        for i in range(len(wordsContainer)):
            if is_better(i, best_overall):
                best_overall = i

        root.best_idx = best_overall

        for i, word in enumerate(wordsContainer):
            node = root
            for char in reversed(word):
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                if is_better(i, node.best_idx):
                    node.best_idx = i

        ans = []
        for query in wordsQuery:
            node = root
            for char in reversed(query):
                if char in node.children:
                    node = node.children[char]
                else:
                    break
            ans.append(node.best_idx)

        return ans
