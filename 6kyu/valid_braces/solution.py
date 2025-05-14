def valid_braces(string: str) -> bool:
    braces = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for char in string:
        # Check if char is an opening brace
        if char in braces:
            stack.append(braces[char])
        # Check if char is a closing brace
        elif char in braces.values():
            if not stack or stack.pop() != char:
                return False
    return not stack





