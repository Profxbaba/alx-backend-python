#!/usr/bin/env python3
"""
This module contains unit tests for the utility functions.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case for the access_nested_map function to handle exceptions.
    """

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b'),
    ])
    def test_access_nested_map_exception(self, nested_map, path, 
                                         expected_exception_message):
        """
        Test that KeyError is raised with the correct message for invalid paths.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        
        self.assertEqual(
            str(context.exception), 
            expected_exception_message
        )


if __name__ == "__main__":
    unittest.main()
