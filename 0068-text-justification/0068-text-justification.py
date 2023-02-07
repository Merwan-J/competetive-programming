class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        if not len(words):
            return []
        
        result = []
        current_line_len, curr_line = 0, []
        
        for word in words: 
            if current_line_len + len(word) + len(curr_line) > maxWidth:    
                for i in range(maxWidth - current_line_len): 
                    curr_line[i % (len(curr_line) - 1 or 1) ] += ' '
                    
                result.append(''.join(curr_line))   
                current_line_len, curr_line = 0, [] 
                
            current_line_len += len(word)
            curr_line.append(word)
            
        return result + [' '.join(curr_line).ljust(maxWidth)]