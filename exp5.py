class StackDepth:
    def maximumDepth(self, stringInput: str) -> int:
        depth = 0
        max_depth = 0
        
        # Iterate through the string
        for char in stringInput:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)  
            elif char == ')':
                depth -= 1
        
        return max_depth


if __name__ == "__main__":
    s = StackDepth()
    print(s.maximumDepth("((()))"))  
