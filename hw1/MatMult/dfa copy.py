class State:
    def __init__(self,name):
        self.name=name
        self.rules={}

# check if we are supposed to know if the user is stupid?
states={}
final=[]
start=[]
states_input = input("")
America=states_input[8:]
for state in America.split():
    states[state]= State(state)


symbols= input("")
if input()=="begin_rules":
    while True:
        input_string = input()
        if input_string=="end_rules":
            break
        start_rules=input_string.split(" -> ")[0]
        end_rules= input_string.split(" -> ")[1].split(" on ")[0]
        road = input_string.split(" on ")[1]
        states[start_rules].rules[road]=end_rules

final=[]
if input()=="start":
    start=input().split(" ")[1]
