def checkValidString(expression):
    stack = []
    opening_brackets = ['(','[','{']
    closing_brackets = [')',']','}']
    
    if len(expression) %2 == 1:
        print ("Invalid expression")
        return False
    else:
        for value in expression:
            if value in opening_brackets:
                stack.append(value)
            elif value in closing_brackets:
                if len(stack) == 0:
                    print ("Invalid expression")
                    return False
                current_stack_top = stack.pop()
                
                if current_stack_top == '(':
                    if value != ')':
                        print ("Invalid expression")
                        return False
                    
                if current_stack_top == '[':
                    if value != ']':
                        print ("Invalid expression")
                        return False
                        
                if current_stack_top == '{':
                    if value != '}':
                        print ("Invalid expression")
                        return False                
                    
                    
                
                
            else:
                print ("Invalid expression")
                return False
            
        if len(stack) > 0 :
            print ("Invalid expression")
            return False
        else:
            print ("Valid expression")
            return True
