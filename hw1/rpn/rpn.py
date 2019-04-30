
# define the stack
Stack_cup=[]
operators= {'/':2 , '*':2 , '~':1, '+':2, '-':2}

while True:
    try:
        calculate=input()
    except EOFError:
        break
    try:
        if len(Stack_cup) >= operators[calculate]:
            if calculate=='~':
                Stack_cup.append(Stack_cup.pop()*-1) 
            elif calculate=='+':
                x = Stack_cup.pop()
                y = Stack_cup.pop()
                # print (x+y)
                Stack_cup.append(x+y)
            elif calculate == '-':
                x = Stack_cup.pop()
                y = Stack_cup.pop()
                # print (y-x)
                Stack_cup.append(y-x)
#                Stack_cup.append((Stack_cup.pop()-Stack_cup.pop())*-1)
            elif calculate =='*':
                x = Stack_cup.pop()
                y = Stack_cup.pop()
                # print (x*y)
                Stack_cup.append(x*y)
#                Stack_cup.append(Stack_cup.pop()*Stack_cup.pop())
            elif calculate == '/':
                x = Stack_cup.pop()
                y = Stack_cup.pop()
                # print (y/x)
                Stack_cup.append(y/x)
#                Stack_cup.append(float((1/Stack_cup.pop())*(Stack_cup.pop()/1)))
            print(Stack_cup[-1])
        
        else:
            print("invalid operation")
    except KeyError:
        try:
            Stack_cup.append((int(calculate)))
            print(calculate)
        except:
            continue
    

            


