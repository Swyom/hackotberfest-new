s = "({{{{}}}))"

stack = []
for char in s:                       # char = )
    
    if char in ["(", "{", "["]:     # stack = [ ({{{{ ]
        stack.append(char)

    else:
                
        if not stack:
            print (False)
                
        current_char = stack.pop()             #current_char = {
        if current_char == "(":
            if char != ")":
                print (False)
                quit()
        if current_char == "[":
            if char != "]":
                print (False)
                quit()
        if current_char == "{":
            if char != "}":
                print (False)
                quit()


if stack:
    print (False)
    quit()
else:
    print (True)
        