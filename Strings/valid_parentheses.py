class Solution:
    def isValid(self, s: str) -> bool:
        
        paranthesis_stack = list()
        
        for i in s:
            if i == '(' or i == '{' or i == '[':
                paranthesis_stack.append(i)
            else:
                if(len(paranthesis_stack) >= 1):
                    if(i == ')'):
                        if(paranthesis_stack[-1] == '('):
                            paranthesis_stack.pop()
                        else:
                            return False
                    elif(i == ']'):
                        if(paranthesis_stack[-1] == '['):
                            paranthesis_stack.pop()
                        else:
                            return False
                    elif(i == '}'):
                        if(paranthesis_stack[-1] == '{'):
                            paranthesis_stack.pop()
                        else:
                            return False
                else:
                    return False
            
        if(len(paranthesis_stack) == 0):
            return True
        else:
            return False
                        
