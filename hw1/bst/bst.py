class node: 
    def __init__(self,value): 
        self.left = None
        self.right = None
        self.value = value

    
path = []
def search(root,value):
    if root is None:
        print ("not found")
    else:
        # value is less then current node go left 
        if value < root.value:
            path.append("l")
            search (root.left,value)
        # value is greater then current node go right
        elif  value>root.value:
            path.append("r")
            search(root.right,value)
        else:
            if len(path) == 0:
                print ("found: root") 
            else:
                string = ""
                for val in path:
                    string =  string + val + " "
                print ("found: " + str(string))
    return root    


def insert (root,value):
    if root is None:
        return node(value)
    else:
        # value is less then current node go left 
        if value < root.value:
            root.left = insert (root.left,value)
     
        elif  value>root.value:
            root.right = insert(root.right,value)
        else:
          return
    return root



def inorder(root): 
    if root: 
        inorder(root.left) 
        print(root.value) 
        inorder(root.right) 



root=None


def testing():
    print (root.left.value)
    inorder(root)
    exit()





while True:
    try:
        user_input= input("")
    except Exception as identifier:
        exit()
    values = user_input.split()
    character, integer = values[0], values[1]
    if character == 'i':
        root = insert(root, int(integer) )
    elif(character == 'q'):
        search(root,int(integer))
        path = []




    
    
