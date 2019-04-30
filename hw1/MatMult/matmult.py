

#define the variables here
matrix1 = input("")
mat1Row = int(matrix1.split()[0])
mat1col= int (matrix1.split()[1])
mat1= []
for i in range ((mat1Row)):  
    mat1_Full_Row=input("")
    mat1.append([float(x) for x in mat1_Full_Row.split()])
#print(mat1)

matrix2 = input("")
mat2Row = int(matrix2.split()[0])
mat2col= int (matrix2.split()[1])
if mat1col != mat2Row:
    print("invalid error")
    exit()
mat2= []
for i in range (len(matrix2)):
    mat2_full_row=input("")
    mat2.append([float(x) for x in mat2_full_row.split()])
#print(mat2)
retval=[]
for i in range((mat1Row)):
    retval.append([])
    for j in range((mat2col)):
        final=0
        for h in range ((mat1col)):
            final+=mat1[i][h]*mat2[h][j]
         #   print('r',retval)
        retval[i].append(final)
            
#print(retval)
for finalNum in retval:
    print(" ".join([str(x) for x in finalNum]))
            


