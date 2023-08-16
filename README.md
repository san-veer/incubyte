# incubyte
# Chandrayaan 3 Testing

This document contains the results of testing the Chandrayaan 3 class.

## Test Case 1: 

Description: 

**Input**:
- Initial position: (0, 0, 0)
- Initial direction: N
- Command: ""

**Expected Output**:
- Final Position: (0, 0, 0)
- Final direction: N

**Actual Output**:
- Final Position: (0, 0, 0)
- Final direction: N

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

## Test Case 2: 

Description: 

**Input**:
- Initial position: (0, 0, 0)
- Initial direction: N
- Command: "f"

**Expected Output**:
- Final Position: (0, 1, 0)
- Final direction: N

**Actual Output**:
- Final Position: (0, 0, 0)
- Final direction: N

FAIL: test_case (__main__.TestSpacecraft.test_case)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "c:\Users\KIIT\Desktop\incubyte\test_case.py", line 16, in test_case
    self.assertEqual(returned_position, expected_position)
AssertionError: Lists differ: [0, 0, 0] != [0, 1, 0]

First differing element 1:
0
1

- [0, 0, 0]
?     ^

+ [0, 1, 0]
?     ^


----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)

## Test Case 2 pass: 

Description: 

**Input**:
- Initial position: (0, 0, 0)
- Initial direction: N
- Command: "f"

**Expected Output**:
- Final Position: (0, 1, 0)
- Final direction: N

**Actual Output**:
- Final Position: (0, 1, 0)
- Final direction: N

Ran 1 test in 0.000s

OK

## Test Case 3: 

Description: 

**Input**:
- Initial position: (0, 0, 0)
- Initial direction: N
- Command: ['f', 'r']

**Expected Output**:
- Final Position: (0, 1, 0)
- Final direction: E

**Actual Output**:
- Final Position: (0, 1, 0)
- Final direction: N

FAIL: test_case (__main__.TestSpacecraft.test_case)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "c:\Users\KIIT\Desktop\incubyte\test_case.py", line 17, in test_case
    self.assertEqual(returned_direction, expected_direction)
AssertionError: 'N' != 'E'
- N
+ E


----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)

## Test Case 3 pass: 

Description: 

**Input**:
- Initial position: (0, 0, 0)
- Initial direction: N
- Command: ['f', 'r']

**Expected Output**:
- Final Position: (0, 1, 0)
- Final direction: E

**Actual Output**:
- Final Position: (0, 1, 0)
- Final direction: E

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK