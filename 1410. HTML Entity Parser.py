class Solution:
    def entityParser(self, text: str) -> str:
        entities = {
            "&quot;": "\"", 
            "&apos;": "'", 
            "&gt;": ">",
            "&lt;": "<", 
            "&frasl;": "/", 
            "&amp;": "&"
        }
        
        for k, v in entities.items():
            text = text.replace(k, v)
            
        return text
