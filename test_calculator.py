import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    def test_subtract(self):
        self.assertEqual(subtract(5,3),2)
        self.assertEqual(subtract(4,4), 0)
        self.assertEqual(subtract(1,5),-4) # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(mul(1,5), 5)
        self.assertEqual(mul(5,-5), -25)
        self.assertEqual(mul(-2,-3), 6) # 3 assertions
    #     fill in code

    def test_divide(self):
        self.assertEqual(div(5,5), 1)
        self.assertEqual(div(-30,6), -5)
        self.assertEqual(div(-1,-1),1) # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0,5) # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3,4), 5)
        self.assertEqual(hypotenuse(5,12), 13)
        self.assertEqual(hypotenuse(20,21), 29) # 3 assertions
    #     fill in code

    def test_sqrt(self):
        
        with self.assertRaises(ValueError):
            square_root(-5)
        self.assertEqual(square_root(1),1)
        self.assertEqual(square_root(4),2 ) # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()