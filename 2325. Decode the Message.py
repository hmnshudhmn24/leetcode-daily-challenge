class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = {' ': ' '}
        curr_char = 97

        for char in key:
            if char not in mapping:
                mapping[char] = chr(curr_char)
                curr_char += 1
                if curr_char > 122:
                    break

        return "".join(mapping[char] for char in message)
