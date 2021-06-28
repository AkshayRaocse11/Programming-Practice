#program to remove adjancent and duplicated character
def removeDuplicates( s):
    stack = []         
    for char in range(len(s)):
        # this stack[-1] because it causes stack undeflow error, so we have to validate stack and stack[-1]
        if stack and stack[-1] == s[char]:
            stack.pop()
        else:
            stack.append(s[char])
                
    return "".join(stack)
str = "abbaccaacf"
str = removeDuplicates(str)    
print(str)