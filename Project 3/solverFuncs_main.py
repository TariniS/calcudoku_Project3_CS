#sName: Tarini Srikanth
#Instructor: Turner
#Project 3- Main


from solverFuncs import *

def main():
    puzzle=getPuzzle()
    #getting the puzzle
    cages= get_cages()
    #getting the cages
    checks=0
    backtracks=0
    #intiliazing checks and backtracks
    current_state=False
    #intiliazing current_state
    i=0
    while i<25:
        #going the length of the 2d puzzle (5*5), starts with i=0
        #using a while loop rather than a for loop
        #if(puzzle[i//5][i%5] < 5):
        if(puzzle[i//5][i%5]>5):
            puzzle[i//5][i%5]=0
        else:
            puzzle[i//5][i%5] = puzzle[i//5][i%5]+1
        #incrementing the value of the current cell by 1
        current_state=check_valid(puzzle,cages)
        #checking the state of the puzzle
        checks=checks+1
        #increasing checks
        if current_state==True and puzzle[i//5][i%5] <=5:
            i=i+1
            #if the state is True and the number is less than 5, then increment the i by 1 to go to the next cell
        elif puzzle[i//5][i%5]<=4:
            i=i
            #continue with the while loop
        else:
            puzzle[i//5][i%5]=0
            #this means that the number is greater than 5
            #set the number to 0
            i=i-1
            #go to the previous cell
            backtracks=backtracks+1
            #increment backtracks
   
    print("\n")
    print("---Solution---")
    print("\n")
    for listNew in puzzle:
        print(*listNew, sep=" ")
        #using string formatting to print the list
    print("checks: ",checks," backtracks: ",backtracks)
        
   


if __name__ == '__main__':
    main()
            
        
