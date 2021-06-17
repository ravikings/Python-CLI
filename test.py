import unittest
from unittest import mock
from classRead import ReadCsvFiles as r



"""

   author: Abdulrafiu rabiu
   date: 06-16-2021
    Test carried out here are see if the function are behaving the way they 
    are program to do, by using unittest mock, we are runing function to
    test against each other and see if the behaviour is the same and when test
    against another function should fail, to run test copy command below.

    @runtest: python -m unittest test

"""


class ReadCsvTest(unittest.TestCase):

    # Testing csvGlob function by using mocking method
    @mock.patch('classRead.ReadCsvFiles.csvGlob')
    def testing_classread_csvGlob(self, test_mock):
        
      test_mock = r.csvGlob  
      self.assertEqual(test_mock, r.csvGlob)  
      self.assertNotEqual(test_mock, r.csvColumn)  
      self.assertNotEqual(test_mock, r.avgColumn) 
      self.assertNotEqual(test_mock, r.threadingFunc) 

   # Testing csvColumn function by using mocking method
    @mock.patch('classRead.ReadCsvFiles.csvColumn')
    def testing_classread_csvColumn(self, test_mock):
        
      test_mock = r.csvColumn
      self.assertEqual(test_mock, r.csvColumn)  
      self.assertNotEqual(test_mock, r.csvGlob)  
      self.assertNotEqual(test_mock, r.avgColumn) 
      self.assertNotEqual(test_mock, r.threadingFunc) 


   # Testing avgColumn function by using mocking method
    @mock.patch('classRead.ReadCsvFiles.avgColumn')
    def testing_classread_avgColumn(self, test_mock):
        
      test_mock = r.avgColumn
      self.assertEqual(test_mock, r.avgColumn)  
      self.assertNotEqual(test_mock, r.csvGlob)  
      self.assertNotEqual(test_mock, r.csvColumn) 
      self.assertNotEqual(test_mock, r.threadingFunc) 


   # Testing threadingFunc function by using mocking method
    @mock.patch('classRead.ReadCsvFiles.threadingFunc')
    def testing_classread_threadingFunc(self, test_mock):
        
      test_mock = r.threadingFunc
      self.assertEqual(test_mock, r.threadingFunc)  
      self.assertNotEqual(test_mock, r.csvGlob)  
      self.assertNotEqual(test_mock, r.csvColumn) 
      self.assertNotEqual(test_mock, r.avgColumn) 



if __name__ == "__main__":
    unittest.main()