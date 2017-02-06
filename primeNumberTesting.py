import unittest
from prime_number import prime_number

 
class primenumber(unittest.TestCase):


    def test_numbers_10(self):
        self.assertEqual( prime_number(10), [2, 3, 5, 7])
 
    def test_strings_str(self):
        self.assertEqual( prime_number("Two"), "invalid input")

    def test_numbers_1(self):
        self.assertEqual( prime_number(1), "No prime number in range")
 
    def test_number_2(self):
        self.assertEqual( prime_number(2), [2])

    def test_numbers_negative_1(self):
        self.assertEqual( prime_number(-1), "No prime number in range")
 
    def test_strings_3(self):
        self.assertEqual( prime_number(3), [2,3])
 
    def test_strings_5(self):
        self.assertEqual( prime_number(5), [2,3,5])
     
    def test_strings_20(self):
        self.assertEqual( prime_number(20), [2, 3, 5, 7, 11, 13, 17, 19])

    def test_strings_50(self):
        self.assertEqual( prime_number(50), [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47])

    def test_strings_5(self):
        self.assertEqual( prime_number(5), [2,3,5])

    def test_strings_121(self):
        self.assertEqual( prime_number(121), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113])

    
 
if __name__ == '__main__':
    unittest.main()
