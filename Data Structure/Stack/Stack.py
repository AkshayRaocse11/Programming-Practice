def removeDuplicates(str1):
    stack = "abbacca"
    holdArray = [] 
    str1 = ""
    for element in range(0, len(stack)):
        holdArray.append(stack[element])
    for element in range(1, len(holdArray)):
        if holdArray[element-1]==holdArray[element]:
            holdArray.pop(element)
            holdArray.pop(element-1)
            removeDuplicates(str1)    
        else:
            str1 += stack[element]
    
     
    return holdArray
stack = "abbacca"
removeDuplicates(stack) 