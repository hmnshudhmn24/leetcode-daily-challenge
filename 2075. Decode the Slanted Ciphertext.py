class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols = len(encodedText) // rows
        decoded_chars = []

        for start_col in range(cols):
            r = 0
            c = start_col

            while r < rows and c < cols:
                idx = (r * cols) + c
                decoded_chars.append(encodedText[idx])
                r += 1
                c += 1

        return "".join(decoded_chars).rstrip()
