#!/usr/bin/env python3

import os
import sys
import random
import unittest


sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'app'))

from solution_1 import window

class TestSlidingWindows(unittest.TestCase):
    
    def setUp(self):
        random.seed(42)
    
    def test_basic_examples(self):
        # Arrange
        # Act & Assert
        self.assertEqual(window(2, 1, [0, 1, 2, 3, 4]), [[0, 1], [1, 2], [2, 3], [3, 4]])
        self.assertEqual(window(2, 2, [0, 1, 2, 3, 4]), [[0, 1], [2, 3]])
        self.assertEqual(window(2, 3, [0, 1, 2, 3, 4]), [[0, 1], [3, 4]])
    
    def test_zero_length_windows(self):
        # Arrange
        test_cases = [
            ([], 1),
            ([1], 1),
            ([1, 2], 1),
            ([1, 2, 3], 1),
            ([1, 2, 3, 4], 1),
            ([1, 2, 3, 4, 5], 1),
            ([1, 2], 2),
            ([1, 2, 3, 4], 2),
            ([1, 2, 3, 4, 5, 6], 3),
            ([1, 2, 3], 2),
            ([1, 2, 3, 4, 5, 6], 4),
        ]
        
        for lst, offset in test_cases:
            # Arrange
            expected = [[] for _ in range(0, len(lst)+1, offset)]
            
            with self.subTest(lst=lst, offset=offset):
                # Act & Assert
                self.assertEqual(window(0, offset, lst), expected)
    
    def test_single_element_windows(self):
        # Arrange
        test_cases = [
            ([1], 1, [[1]]),
            ([1, 2], 1, [[1], [2]]),
            ([1, 2, 3], 1, [[1], [2], [3]]),
            ([1, 2, 3, 4], 1, [[1], [2], [3], [4]]),
            ([1, 2, 3, 4, 5], 1, [[1], [2], [3], [4], [5]]),
            ([1, 2, 3, 4], 2, [[1], [3]]),
            ([1, 2, 3, 4, 5, 6], 2, [[1], [3], [5]]),
            ([1, 2, 3, 4, 5, 6], 3, [[1], [4]]),
        ]
        
        for lst, offset, expected in test_cases:
            with self.subTest(lst=lst, offset=offset):
                # Act & Assert
                self.assertEqual(window(1, offset, lst), expected)
    
    def test_length_2_windows(self):
        # Arrange
        test_cases = [
            ([1, 2], 1, [[1, 2]]),
            ([1, 2, 3], 1, [[1, 2], [2, 3]]),
            ([1, 2, 3, 4], 1, [[1, 2], [2, 3], [3, 4]]),
            ([1, 2, 3, 4, 5], 1, [[1, 2], [2, 3], [3, 4], [4, 5]]),
            ([1, 2, 3, 4], 2, [[1, 2], [3, 4]]),
            ([1, 2, 3, 4, 5, 6], 2, [[1, 2], [3, 4], [5, 6]]),
            ([1, 2, 3, 4, 5, 6], 3, [[1, 2], [4, 5]]),
        ]
        
        for lst, offset, expected in test_cases:
            with self.subTest(lst=lst, offset=offset):
                # Act & Assert
                self.assertEqual(window(2, offset, lst), expected)
    
    def test_length_3_windows(self):
        # Arrange
        test_cases = [
            ([1, 2, 3], 1, [[1, 2, 3]]),
            ([1, 2, 3, 4], 1, [[1, 2, 3], [2, 3, 4]]),
            ([1, 2, 3, 4, 5], 1, [[1, 2, 3], [2, 3, 4], [3, 4, 5]]),
            ([1, 2, 3, 4, 5, 6], 1, [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]),
            ([1, 2, 3, 4, 5, 6], 2, [[1, 2, 3], [3, 4, 5]]),
            ([1, 2, 3, 4, 5, 6], 3, [[1, 2, 3], [4, 5, 6]]),
        ]
        
        for lst, offset, expected in test_cases:
            with self.subTest(lst=lst, offset=offset):
                # Act & Assert
                self.assertEqual(window(3, offset, lst), expected)
    
    def test_empty_lists(self):
        # Arrange
        test_cases = [
            (0, 1, []),
            (0, 2, []),
            (0, 3, []),
        ]
        
        for length, offset, lst in test_cases:
            # Arrange
            expected = [[] for _ in range(0, len(lst)+1, offset)]
            
            with self.subTest(length=length, offset=offset, lst=lst):
                # Act & Assert
                self.assertEqual(window(length, offset, lst), expected)

        # Arrange
        lengths = [1, 2, 5]
        
        for length in lengths:
            # Act & Assert
            self.assertEqual(window(length, 1, []), [])
    
    def test_single_element_lists(self):
        # Arrange
        test_cases = [
            (0, 1, [5]),
            (0, 2, [5]),
        ]
        
        for length, offset, lst in test_cases:
            # Arrange
            expected = [[] for _ in range(0, len(lst)+1, offset)]
            
            with self.subTest(length=length, offset=offset, lst=lst):
                # Act & Assert
                self.assertEqual(window(length, offset, lst), expected)

        # Act & Assert
        self.assertEqual(window(1, 1, [5]), [[5]])
        self.assertEqual(window(2, 1, [5]), [])
    
    def test_large_offsets(self):
        # Arrange
        test_cases = [
            (0, 10, [1, 2, 3]),
            (0, 10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        ]
        
        for length, offset, lst in test_cases:
            # Arrange
            expected = [[] for _ in range(0, len(lst)+1, offset)]
            
            with self.subTest(length=length, offset=offset, lst=lst):
                # Act & Assert
                self.assertEqual(window(length, offset, lst), expected)

        # Act & Assert
        self.assertEqual(window(1, 10, [1, 2, 3]), [[1]])
        self.assertEqual(window(2, 10, [1, 2, 3]), [[1, 2]])
        self.assertEqual(window(3, 10, [1, 2, 3]), [[1, 2, 3]])
    
    def test_length_larger_than_list(self):
        # Arrange
        test_cases = [
            (5, 1, [1, 2, 3]),
            (10, 1, [1, 2, 3]),
            (5, 2, [1, 2, 3]),
            (3, 1, [1, 2]),
        ]
        
        for length, offset, lst in test_cases:
            with self.subTest(length=length, offset=offset, lst=lst):
                # Act & Assert
                self.assertEqual(window(length, offset, lst), [])
    
    def test_string_lists(self):
        # Arrange
        test_cases = [
            (0, 1, ['a', 'b', 'c']),
            (0, 2, ['a', 'b', 'c', 'd']),
        ]
        
        for length, offset, lst in test_cases:
            # Arrange
            expected = [[] for _ in range(0, len(lst)+1, offset)]
            
            with self.subTest(length=length, offset=offset, lst=lst):
                # Act & Assert
                self.assertEqual(window(length, offset, lst), expected)

        # Act & Assert
        self.assertEqual(window(1, 1, ['a', 'b', 'c']), [['a'], ['b'], ['c']])
        self.assertEqual(window(2, 1, ['a', 'b', 'c']), [['a', 'b'], ['b', 'c']])
        self.assertEqual(window(3, 1, ['a', 'b', 'c']), [['a', 'b', 'c']])
        self.assertEqual(window(2, 2, ['a', 'b', 'c', 'd']), [['a', 'b'], ['c', 'd']])
    
    def test_mixed_type_lists(self):
        # Arrange
        test_cases = [
            (0, 1, [1, 'a', 2.5]),
        ]
        
        for length, offset, lst in test_cases:
            # Arrange
            expected = [[] for _ in range(0, len(lst)+1, offset)]
            
            with self.subTest(length=length, offset=offset, lst=lst):
                # Act & Assert
                self.assertEqual(window(length, offset, lst), expected)

        # Act & Assert
        self.assertEqual(window(1, 1, [1, 'a', 2.5]), [[1], ['a'], [2.5]])
        self.assertEqual(window(2, 1, [1, 'a', 2.5]), [[1, 'a'], ['a', 2.5]])
        self.assertEqual(window(3, 1, [1, 'a', 2.5]), [[1, 'a', 2.5]])
    
    def test_negative_numbers(self):
        # Arrange
        test_cases = [
            (0, 1, [-1, -2, -3]),
            (0, 2, [-1, -2, -3, -4]),
        ]
        
        for length, offset, lst in test_cases:
            # Arrange
            expected = [[] for _ in range(0, len(lst)+1, offset)]
            
            with self.subTest(length=length, offset=offset, lst=lst):
                # Act & Assert
                self.assertEqual(window(length, offset, lst), expected)

        # Act & Assert
        self.assertEqual(window(1, 1, [-1, -2, -3]), [[-1], [-2], [-3]])
        self.assertEqual(window(2, 1, [-1, -2, -3]), [[-1, -2], [-2, -3]])
        self.assertEqual(window(3, 1, [-1, -2, -3]), [[-1, -2, -3]])
        self.assertEqual(window(2, 2, [-1, -2, -3, -4]), [[-1, -2], [-3, -4]])
    
    def test_floating_point_numbers(self):
        # Arrange
        test_cases = [
            (0, 1, [1.5, 2.7, 3.1]),
        ]
        
        for length, offset, lst in test_cases:
            # Arrange
            expected = [[] for _ in range(0, len(lst)+1, offset)]
            
            with self.subTest(length=length, offset=offset, lst=lst):
                # Act & Assert
                self.assertEqual(window(length, offset, lst), expected)
        
        # Act & Assert
        self.assertEqual(window(1, 1, [1.5, 2.7, 3.1]), [[1.5], [2.7], [3.1]])
        self.assertEqual(window(2, 1, [1.5, 2.7, 3.1]), [[1.5, 2.7], [2.7, 3.1]])
        self.assertEqual(window(3, 1, [1.5, 2.7, 3.1]), [[1.5, 2.7, 3.1]])
    
    def test_nested_lists(self):
        # Arrange
        test_cases = [
            (0, 1, [[1], [2], [3]]),
        ]
        
        for length, offset, lst in test_cases:
            # Arrange
            expected = [[] for _ in range(0, len(lst)+1, offset)]
            
            with self.subTest(length=length, offset=offset, lst=lst):
                # Act & Assert
                self.assertEqual(window(length, offset, lst), expected)
        
        # Act & Assert
        self.assertEqual(window(1, 1, [[1], [2], [3]]), [[[1]], [[2]], [[3]]])
        self.assertEqual(window(2, 1, [[1], [2], [3]]), [[[1], [2]], [[2], [3]]])
        self.assertEqual(window(3, 1, [[1], [2], [3]]), [[[1], [2], [3]]])
    
    def test_boolean_values(self):
        # Arrange
        test_cases = [
            (0, 1, [True, False, True]),
        ]
        
        for length, offset, lst in test_cases:
            # Arrange
            expected = [[] for _ in range(0, len(lst)+1, offset)]
            
            with self.subTest(length=length, offset=offset, lst=lst):
                # Act & Assert
                self.assertEqual(window(length, offset, lst), expected)
        
        # Act & Assert
        self.assertEqual(window(1, 1, [True, False, True]), [[True], [False], [True]])
        self.assertEqual(window(2, 1, [True, False, True]), [[True, False], [False, True]])
        self.assertEqual(window(3, 1, [True, False, True]), [[True, False, True]])
    
    def test_none_values(self):
        # Arrange
        test_cases = [
            (0, 1, [None, None, None]),
        ]
        
        for length, offset, lst in test_cases:
            # Arrange
            expected = [[] for _ in range(0, len(lst)+1, offset)]
            
            with self.subTest(length=length, offset=offset, lst=lst):
                # Act & Assert
                self.assertEqual(window(length, offset, lst), expected)
        
        # Act & Assert
        self.assertEqual(window(1, 1, [None, None, None]), [[None], [None], [None]])
        self.assertEqual(window(2, 1, [None, None, None]), [[None, None], [None, None]])
        self.assertEqual(window(3, 1, [None, None, None]), [[None, None, None]])
    
    def test_random_small_lists(self):
        for _ in range(100):
            # Arrange
            lst_length = random.randint(0, 10)
            lst = [random.randint(-100, 100) for _ in range(lst_length)]
            length = random.randint(0, min(5, lst_length + 1))
            offset = random.randint(1, max(1, lst_length))
            
            with self.subTest(lst=lst, length=length, offset=offset):
                # Act
                result = window(length, offset, lst)
                
                # Assert
                for window_list in result:
                    self.assertEqual(len(window_list), length)
                if length == 0:
                    expected = [[] for _ in range(0, len(lst)+1, offset)]
                    self.assertEqual(result, expected)
    
    def test_random_medium_lists(self):
        for _ in range(100):
            # Arrange
            lst_length = random.randint(10, 50)
            lst = [random.randint(-1000, 1000) for _ in range(lst_length)]
            length = random.randint(0, min(10, lst_length + 1))
            offset = random.randint(1, max(1, lst_length // 2))
            
            with self.subTest(lst=lst, length=length, offset=offset):
                # Act
                result = window(length, offset, lst)
                
                # Assert
                for window_list in result:
                    self.assertEqual(len(window_list), length)
                if length == 0:
                    expected = [[] for _ in range(0, len(lst)+1, offset)]
                    self.assertEqual(result, expected)
    
    def test_random_large_lists(self):
        for _ in range(100):
            # Arrange
            lst_length = random.randint(50, 200)
            lst = [random.randint(-10000, 10000) for _ in range(lst_length)]
            length = random.randint(0, min(20, lst_length + 1))
            offset = random.randint(1, max(1, lst_length // 4))
            
            with self.subTest(lst=lst, length=length, offset=offset):
                # Act
                result = window(length, offset, lst)
                
                # Assert
                for window_list in result:
                    self.assertEqual(len(window_list), length)
                if length == 0:
                    expected = [[] for _ in range(0, len(lst)+1, offset)]
                    self.assertEqual(result, expected)
    
    def test_edge_case_combinations(self):
        # Arrange
        edge_cases = [([1, 2, 3], 1000), ([1, 2, 3], 2), ([1, 2, 3, 4, 5, 6], 3)]
        
        for lst, offset in edge_cases:
            # Arrange
            expected = [[] for _ in range(0, len(lst)+1, offset)]
            
            with self.subTest(length=0, offset=offset, lst=lst):
                # Act & Assert
                self.assertEqual(window(0, offset, lst), expected)
        
        # Act & Assert
        self.assertEqual(window(3, 1, [1, 2, 3]), [[1, 2, 3]])
        self.assertEqual(window(4, 1, [1, 2, 3, 4]), [[1, 2, 3, 4]])
        self.assertEqual(window(1, 3, [1, 2, 3]), [[1]])
        self.assertEqual(window(2, 3, [1, 2, 3]), [[1, 2]])
        self.assertEqual(window(2, 2, [1, 2, 3, 4]), [[1, 2], [3, 4]])
        self.assertEqual(window(3, 3, [1, 2, 3, 4, 5, 6]), [[1, 2, 3], [4, 5, 6]])
    
    def test_known_correct_results(self):
        # Arrange
        known_results = [
            (0, 1, [1, 2, 3]),
            (0, 2, [1, 2, 3, 4]),
            (0, 3, [1, 2, 3, 4, 5, 6]),
        ]
        
        for length, offset, lst in known_results:
            # Arrange
            expected = [[] for _ in range(0, len(lst)+1, offset)]
            
            with self.subTest(length=length, offset=offset, lst=lst):
                # Act & Assert
                self.assertEqual(window(length, offset, lst), expected)
        
        # Act & Assert
        self.assertEqual(window(1, 1, [1, 2, 3]), [[1], [2], [3]])
        self.assertEqual(window(2, 1, [1, 2, 3]), [[1, 2], [2, 3]])
        self.assertEqual(window(3, 1, [1, 2, 3]), [[1, 2, 3]])
        self.assertEqual(window(1, 2, [1, 2, 3, 4]), [[1], [3]])
        self.assertEqual(window(2, 2, [1, 2, 3, 4]), [[1, 2], [3, 4]])
        self.assertEqual(window(3, 2, [1, 2, 3, 4]), [[1, 2, 3]])
        self.assertEqual(window(4, 2, [1, 2, 3, 4]), [[1, 2, 3, 4]])
        self.assertEqual(window(1, 3, [1, 2, 3, 4, 5, 6]), [[1], [4]])
        self.assertEqual(window(2, 3, [1, 2, 3, 4, 5, 6]), [[1, 2], [4, 5]])
        self.assertEqual(window(3, 3, [1, 2, 3, 4, 5, 6]), [[1, 2, 3], [4, 5, 6]])
    
    def test_basic_validation_tests(self):
        for _ in range(100):
            # Arrange
            lst_length = random.randint(0, 20)
            lst = [random.randint(-100, 100) for _ in range(lst_length)]
            length = random.randint(0, min(10, lst_length + 1))
            offset = random.randint(1, max(1, lst_length))
            
            with self.subTest(lst=lst, length=length, offset=offset):
                # Act
                result = window(length, offset, lst)
                
                # Assert
                for window_list in result:
                    self.assertEqual(len(window_list), length)
                
                for window_list in result:
                    if length > 0:
                        for element in window_list:
                            self.assertIn(element, lst)

if __name__ == '__main__':
    unittest.main()
