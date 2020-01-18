board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

#Prints the board
def show(x):
    for i in range(len(x)):
        if i%3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(x[0])):

            if j%3 == 0 and j !=0:
                print(" | ",end="")
            if j == 8:
                print(x[i][j])
            else:
                print(x[i][j],end=" ")


#Return the index of empty spaces
def empty(x):
    for i in range(len(x)):
        for j in range(len(x[0])):
            if x[i][j] == 0:
                return (i,j)
    return None
#Check Validity
def valid(x,num,pos):
    #Checking row
   for i in range(len(x[0])):
        if x[pos[0]][i] == num and i != pos[1]:
            return False

     #Checking column
   for i in range(len(x)):
        if x[i][pos[1]] == num and i != pos[0]:
            return False    

     #Checking Box
   box_x = pos[1] // 3 
   box_y = pos[0] // 3

   for i in range(box_y * 3, box_y *3 + 3):
       for j in range(box_x * 3, box_x * 3 +3):
           if x[i][j] == num and (i,j) != pos:
               return False
  
   return True
#Using the above functions to solve the board using recurssion
def solve(x):
    find = empty(x)
    if not find:
        return True
    else:
        row,column = find

    for i in range(1,10):
        if valid(x, i , (row,column)):
            x[row][column] = i
            if solve(x):
                return True
            x[row][column]=0
    return False
   

show(board)
print("\n*******SOLVED!*********\n")
solve(board)
show(board)