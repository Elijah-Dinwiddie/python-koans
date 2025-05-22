#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

__ = None


class AboutWhileLoops(unittest.TestCase):

    def test_count_down(self):

        numbers = ''
        index = 3
        while index > 0:
            index = index - 1
            numbers = numbers + str(index)

        assert numbers == "210"

    def test_count_down_again(self):

        numbers = ''
        index = 3
        while index > 0:
            numbers = numbers + str(index)
            index = index - 1

        assert numbers == '321'

    def test_find_first_index_of_a_character(self):

        phrase = 'Lord of the Rings'
        index = 0
        while not phrase[index] == 'R':
            index = index + 1

        assert index == 12

    def test_find_first_index_of_a_vowel(self):

        # You can test for character membership using the `in` keyword:
        # >>> 'd' in 'abc'
        # False
        # >>> 'b' in 'abc'
        # True

        vowels = 'aeiou'

        phrase = 'Pdrlso'

        index = 0
        while not phrase[index] vowels:
            index += 1
        # This is to test if this updated correctly - Elijah
        # Your code here
        # Tip reuse code from previous test method

        assert index == 5
