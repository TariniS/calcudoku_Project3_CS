#Name:Tarini Srikanth
#Instructor: Turner
#Project 3- Solver Funcs

def get_cages():
    #based on the user value
    numOfCages = input("Number of cages: ")
    numOfCagesInt = int(numOfCages)
    cagesList =[]
    for i in range(numOfCagesInt):
        a = input("Cage number "+str(i)+" :").split()
        #adding the number of the cages to the user input
        inputList = list(a)
        #making a list of input values
        inputList =[int(i)for i in inputList]
        cagesList.append(inputList)
        #adding to the above list to make it a 2d array
    return cagesList
    
    

def getPuzzle():
    a=[[0 for i in range(5)] for j in range(5)]
    #filling the puzzle with 0's using list comprehension
    return a
      

        
def check_rows_valid(puzzle):
    #takes a list of lists, checks if every row has no repeats
    #only values 1-n
    #[
    # [0,0,0,0,0]
    # [1,3,4,5,6]
    # [2,3,4,5,6]
    #]
    for i in range(5):
        #creating a boolean variable that checks if each row contains duplicates and only contains value from 1 to N, including 0's
        if(i==0):
            a1=(containsDuplicates(puzzle[i])==False) and (checkIfNumIsFrom1ToN(puzzle[i])==True)
        if(i==1):
            a2=(containsDuplicates(puzzle[i])==False) and (checkIfNumIsFrom1ToN(puzzle[i])==True)
        if(i==2):
            a3=(containsDuplicates(puzzle[i])==False) and (checkIfNumIsFrom1ToN(puzzle[i])==True)
        if(i==3):
            a4=(containsDuplicates(puzzle[i])==False) and (checkIfNumIsFrom1ToN(puzzle[i])==True)
        if(i==4):
            a5=(containsDuplicates(puzzle[i])==False) and (checkIfNumIsFrom1ToN(puzzle[i])==True)
    #returning true only if all of the rows are valid
    return (a1 and a2 and a3 and a4 and a5)
        
                

def containsDuplicates(listInPuzzle):
    #checks if the list contains duplicates. 
    #calling this method in check rows and check columns
    duplicateCount=0
    for item in listInPuzzle:
        if item!=0:
            duplicateCount = listInPuzzle.count(item)
            if duplicateCount>1:
                return True
    return False

def checkIfNumIsFrom1ToN(listInPuzzle):
    #checks if the list contains numbers only from 0-N
    #calling this method in check rows and check columns
    for i in range(len(listInPuzzle)):
        if ((listInPuzzle[i]<0)or(listInPuzzle[i]>5)):
            return False
    return True
                   
def check_columns_valid(puzzle):
    #takes a list of lists, checks if every column has no repeats
    #and only values 1-n
    #[
    # [0,0,0,0,0]
    # [1,3,4,5,6]
    # [2,3,4,5,6]
    # [3,4,5,6,7]
    #]
    # [[0,1,2,3]
    #  [0,3,3,4]
    #  [0,4,4,5]
    a=[]
    array0=[]
    array1=[]
    array2=[]
    array3=[]
    array4=[]
    for i in range(5):
        if(i==0):
            for j in range(5):
                array0.append(puzzle[j][0])
        elif(i==1):
            for k in range(5):
                array1.append(puzzle[k][1])
        elif(i==2):
            for p in range(5):
                array2.append(puzzle[p][2])
        elif(i==3):
            for e in range(5):
                array3.append(puzzle[e][3])
        else:
            for q in range(5):
                array4.append(puzzle[q][4])
    a.append(array0)
    a.append(array1)
    a.append(array2)
    a.append(array3)
    a.append(array4)
    #above code was converting the columns into rows using for loops
    for i in range(5):
        if(i==0):
            a1=(containsDuplicates(a[i])==False) and (checkIfNumIsFrom1ToN(a[i])==True)
        if(i==1):
            a2=(containsDuplicates(a[i])==False) and (checkIfNumIsFrom1ToN(a[i])==True)
        if(i==2):
            a3=(containsDuplicates(a[i])==False) and (checkIfNumIsFrom1ToN(a[i])==True)
        if(i==3):
            a4=(containsDuplicates(a[i])==False) and (checkIfNumIsFrom1ToN(a[i])==True)
        if(i==4):
            a5=(containsDuplicates(a[i])==False) and (checkIfNumIsFrom1ToN(a[i])==True)
    #using the same code for check_rows, creating a boolena variable
    #return true only if all of them are ture
    return (a1 and a2 and a3 and a4 and a5)
    
    
    
   

        
def check_cages_valid(puzzle,cages):
    #using the get_cages method, make sure that each value adds up
    #to the sum
    #
    #[9 3 0 5 6],[7 2 1 2],[10 3 3 8 13],[14 4 4 9 14 19],[3 1 17]
    #[8 3 10 11 16],[13 4 12 17 21 22],[5 2 15 20],[6,3,18,23,24]]
    #
    #
    #[[3,5,2,1,4],[5,1,3,4,2],[2,4,1,5,3],[1,2,4,3,5],[4,3,5,2,1]]
    #col index: 0%5, row index: 0//5
    #col index: 5%5, row index: 5//5
    #col index: 6%5, row index: 6//5
    return checkAllCages(cages,puzzle)

    

def checkAllCages(cages,puzzle):
    booleanVar= True
    for i in range (len(cages)): #goes through the array of arrays of cages, #small array is the smaller array in the bigger array
            totalSum=0
            numOfCells = cages[i][1]
            valueOfPuzzleNum=0
            for r in range(int(numOfCells)):
                #goes the length of the 2nd value
                columnIndex =(int(cages[i][r+2]))%5
                rowIndex =(int(cages[i][r+2]))//5
                #creates the row index and column index based off the r+2 value
                #that is the value were the indexes start
                puzzleNum = int(puzzle[rowIndex][columnIndex])
                totalSum = totalSum +puzzleNum
                if(puzzleNum==0):#accounting for 0's to be valid
                    valueOfPuzzleNum+=1
            if valueOfPuzzleNum<=0:
                if cages[i][0]!=totalSum: #for the fully filled cage
                    booleanVar=False
            
    return booleanVar
    

def check_valid(puzzle,cages):
    #check the validility of the puzzle and the cages using all the methods
    if (check_rows_valid(puzzle)==True and check_columns_valid(puzzle)==True and check_cages_valid(puzzle,cages)==True):
        return True
    return False
    #only returns True if cages, rows and columns are true





    




