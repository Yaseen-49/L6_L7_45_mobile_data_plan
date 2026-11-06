# Lab 7: Fuzz Testing – Mobile Data Plan

**Name:** YASEEN MULLA  
**SRN:** PES2UG24CS607

## 1. Objective

The objective of this lab is to perform fuzz testing using Python's Hypothesis library to identify input validation bugs. Random and unexpected inputs are supplied to the application to check whether the functions handle invalid data safely without crashing.

## 2. Tools Used

- Python 3.13.7
- Pytest 9.2.0
- Hypothesis 6.170.14

## 3. Files

| File | Description |
|---|---|
| `mobile_data_plan.py` | Application containing the input-processing functions |
| `test_mobile_data_plan.py` | Hypothesis fuzz tests and validation tests |
| `README.md` | Lab description and execution instructions |

## 4. Functions Tested

1. `parse_plan()` – Parses the mobile plan name and data allowance.
2. `usage_average()` – Calculates average daily data usage.
3. `payable_bill()` – Calculates the payable bill after tax and discount.

## 5. Bugs Identified and Fixes

The original application did not properly handle invalid inputs.

The following problems were identified:

- Missing input values caused errors.
- Incorrect separators caused parsing errors.
- Empty strings were not handled safely.
- Non-numeric values caused conversion errors.
- Negative and non-finite numeric values were not validated.

**Fixes implemented:**

- Added input type and format validation.
- Added safe numeric conversion using exception handling.
- Rejected negative and non-finite values.
- Returned `None` for invalid inputs instead of crashing.
- Added clear invalid-input messages in the application.

## 6. Testing Performed

Hypothesis was used to generate random strings and `None` values for all three functions.

The test cases include:

- Fuzz testing of `parse_plan()`.
- Fuzz testing of `usage_average()`.
- Fuzz testing of `payable_bill()`.
- Testing valid inputs.
- Testing invalid inputs.

## 7. Commands Used

Install dependencies:

```bash
python -m pip install hypothesis pytest
```

Run the tests:

```bash
python -m pytest test_mobile_data_plan.py -v
```

Run the application:

```bash
python mobile_data_plan.py
```

## 8. Test Results

**Final test result: 5 passed in 1.32 seconds.**

All five tests passed successfully, including the three Hypothesis fuzz tests, valid-input tests, and invalid-input tests.

The application was also executed with valid sample inputs:

| Input | Expected output |
|---|---|
| `standard:5` | `('Standard', 5.0)` |
| `300,450,800` | `516` |
| `399\|50` | `420.82` |

All outputs matched the expected results.

## 9. Conclusion

Fuzz testing was successfully performed using Hypothesis and Pytest. Invalid and unexpected inputs were identified and handled through proper input validation. All five tests passed, and the corrected application produced the expected results for valid inputs.

