from solverFuncs import *

def main():
    puzzle =[[3,5,2,1,4],[5,1,3,4,2],[2,4,1,5,3],[1,2,4,3,5],[4,3,5,2,1]]
    
    cages =[[9,3,0,5,6],[7,2,1,2],[10,3,3,8,13],[14,4,4,9,14,19],[3,1,7],
            [8,3,10,11,16],[13,4,12,17,21,22],[5,2,15,20],[6,3,18,23,24]]
    puzzle1=[[0,0,0,0,0],[0,0,0,1,1],[2,3,4,5,6],[5,6,7,3,4],[2,3,1,4,5]]
    
    value = check_valid(puzzle,cages)
    print(value)

if __name__ == '__main__':
   main()
    
