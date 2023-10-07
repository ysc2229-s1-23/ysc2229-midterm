"""
Kth+1 Largest Number in a Stream

Problem Statement:
Design a class that can efficiently find the Kth+1 largest element in a stream of numbers.

Requirements:
1. The class should have a constructor which accepts an integer array containing initial numbers from the stream and an integer ‘K’. 
2. The class should have a function add(int num) which will store the given number and return the Kth+1 largest number.

Example:
Input: [3, 1, 5, 12, 2, 11], K = 4
1. Calling add(6) should return '2' (5th largest).
2. Calling add(13) should return '5' (5th largest).
3. Calling add(4) should still return '5' (5th largest).

Note: 
The stream can contain duplicate numbers.
Make sure to handle edge cases. When might we not be able to return the kth+1 largest number?

Tags:
    - Sorting
    - Priority Queue
    - Google Interview Question

"""

import heapq

class KthPlusOneLargest:
    def __init__(self, nums, k):
        return 

    def add(self, num):
        return -1