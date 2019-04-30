class State:
    def __init__(self,name):
        self.name=name
        self.paths=[]

class Path:
    def __init__(self, name, end):
        self.name = name
        self.end = end



def findState(state_name):
    for state in states:
        if state.name == state_name:
            return state
    raise Exception("No state was found")


def check_if_valid(sequence, start, end):


    Starting_State = findState(start)
    for p in sequence:
        # print (Starting_State.name)
        tmp = None
        for path in Starting_State.paths:
            if path.name == p:
                tmp = findState(path.end)
        if tmp == None:
            print ("rejected")
            return
        Starting_State = tmp
    
    # print ("ending node: " + str(Starting_State.name))
    for endingState in end:
        if endingState == Starting_State.name:
            print ("accepted")
            return
    print ("rejected")
    return


# all states 
states = []


states_input = input("")
America=states_input[8:]

for state in America.split():
    states.append(State(state))
    # print (state)



#this is where we get the rules
symbols= input("").split(": ")[1].split(" ")

#print (symbols)

if input() == "begin_rules":
    while True:
        input_string = input()
        if input_string=="end_rules":
            break
        start_path = input_string.split(" -> ")[0]
        end_path = input_string.split(" -> ")[1].split(" on ")[0]
        road = input_string.split(" on ")[1]
        
    #   print(road)

#        print (start_path)
#        print (end_path)
#        print (road)
#        print ("------------------")
        findState(start_path).paths.append(Path(road,end_path))



start_states=input("")
if start_states.split(" ")[0]=="start:":
    start= start_states.split(" ")[1]

# print (start)

final=[]
# print ("aryeh")
final_states=input("")
# print (final_states)
if final_states.split()[0]=="final:":
    final = final_states.split()[1:]
# print (final)





while True:
    try:
        sq=input("")
        check_if_valid(sq,start,final)
    except Exception as identifier:x
        exit()


# this is the final copy of the code febuary 21st






    
    
        






