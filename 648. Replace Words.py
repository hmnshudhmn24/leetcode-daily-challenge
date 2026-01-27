class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        root = TrieNode()
        
        # Build Trie
        for word in dictionary:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True
            
        def get_root(word):
            node = root
            prefix = ""
            for char in word:
                if char not in node.children:
                    return word  # No root found
                node = node.children[char]
                prefix += char
                if node.is_end:
                    return prefix  # Shortest root found
            return word
            
        return " ".join(get_root(w) for w in sentence.split())
