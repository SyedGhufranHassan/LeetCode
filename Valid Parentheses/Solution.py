def isValid(s):
    stack=[]
    for p in s:
        if p=='(':
            stack.append(p)
        elif p=='[':
            stack.append(p)
        elif p=='{':
            stack.append(p)
        
        elif p==']':
            if len(stack)==0:
                return False
            elif stack[-1]=='[':
                stack.pop()
            else:
                return False
        elif p==')':
            if len(stack)==0:
                return False
            elif stack[-1]=='(':
                stack.pop()
            else:
                return False
        elif p=='}':
            if len(stack)==0:
                return False
            elif stack[-1]=='{':
                stack.pop()
            else:
                return False
                
    if len(stack)==0:
        return True
    return False
            

s='[(){}[()]]'
print(isValid(s))
