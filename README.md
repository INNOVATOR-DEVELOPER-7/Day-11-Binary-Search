# Day-11-Binary-Search
Here Python Program for Shell Sort. Day 8 of Day 365.
- Initial Setup: Start with a sorted array and two pointers, one at the beginning (low) and one at the end (high) of the array.
- Middle Element: Calculate the middle element of the array.
- Comparison:
  - If the middle element is the target, the search is complete.
  - If the target is smaller than the middle element, adjust the high pointer to the middle element minus one.
  - If the target is larger than the middle element, adjust the low pointer to the middle element plus one.
- Repeat: Repeat the process until the target element is found or the pointers converge (low exceeds high).

Here's a visual representation using the example array [1, 3, 5, 7, 9, 11, 13, 15, 17, 19], and searching for the target value 7:

1. Initial Array: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
2. Initial Pointers: Low = 0, High = 9
3. Calculate Middle: Middle = 4, Middle Element = 9
   - Target (7) is less than 9, adjust high to 3
4. New Pointers: Low = 0, High = 3
5. Calculate New Middle: Middle = 1, Middle Element = 3
   - Target (7) is greater than 3, adjust low to 2
6. New Pointers: Low = 2, High = 3

7. Calculate New Middle: Middle = 2, Middle Element = 5
   - Target (7) is greater than 5, adjust low to 3
8. New Pointers: Low = 3, High = 3
9. Calculate New Middle: Middle = 3, Middle Element = 7
   - Target (7) is found

The target value 7 is located at index 3.
