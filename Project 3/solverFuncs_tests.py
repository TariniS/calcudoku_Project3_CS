#Name:Tarini Srikanth
#Instructor: Turner
#Project 3- Function tests
import unittest
from solverFuncs import *

class TestCases(unittest.TestCase):
    def test_puzzle(self):
        self.assertEqual(getPuzzle(),[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
    def test_rows_check(self):
        a= [[5,1,2,3,4],[2,3,2,1,4],[3,1,2,5,4],[2,1,3,4,5],[1,2,3,4,5]]
        self.assertEqual(check_rows_valid(a),False)
    def test_duplicates(self):
        p=[2,2,2,2,2]
        self.assertEqual(containsDuplicates(p),True)
    def test_duplicates5(self):
        p=[1,2,2,5,5]
        self.assertEqual(containsDuplicates(p),True)
    def test_duplicates2(self):
        a=[3,4,5,6,7]
        self.assertEqual(containsDuplicates(a),False)
    def test_rows_check2(self):
        b=[[1,2,3,4,5],[1,2,3,4,5],[3,4,1,2,5],[2,3,4,5,1],[1,2,3,4,5]]
        self.assertEqual(check_rows_valid(b),True)
    def test_rows_check8(self):
        p=[[1,2,2,5,5],[1,2,3,4,5],[3,4,1,2,5],[2,3,4,5,1],[1,2,3,4,5]]
        self.assertEqual(check_rows_valid(p),False)
    def test_rows_check5(self):
        c=[[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        self.assertEqual(check_rows_valid(c),True)
    def test_col_check(self):
        a= [[1,2,3,4,5],[2,3,4,5,1],[3,4,5,1,2],[4,5,1,2,3],[5,1,2,3,4]]
        self.assertEqual(check_columns_valid(a),True)
    def test_col_check2s(self):
        b=[[1,2,3,4,5],[1,2,3,4,5],[3,4,1,2,5],[2,3,4,5,1],[1,2,3,4,5]]
        self.assertEqual(check_columns_valid(b),False)
    def test_col_checks3(self):
        ab=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        self.assertEqual(check_columns_valid(ab),True)
    def test_col_checks4(self):
        cd=[[1,0,0,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        self.assertEqual(check_columns_valid(cd),False)
    def test_1_toN(self):
        a=[1,2,3,4,5]
        self.assertEqual(checkIfNumIsFrom1ToN(a),True)
    def test_1_toN2(self):
        a=[0,1,2,3,4]
        self.assertEqual(checkIfNumIsFrom1ToN(a),True)
    
        
    
        
        
        
    
if __name__== '__main__':
    unittest.main()
    
        
    
    
        
