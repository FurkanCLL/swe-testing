# Testing Strategy

## What Was Tested

The following components were tested:

- Core calculation logic (engine)
- Interaction between button input and calculation logic (controller)

Unit tests focus on individual arithmetic operations.
Integration tests simulate user button presses.


## What Was Not Tested

- Visual appearance of the GUI
- Performance under heavy load
- UI responsiveness

These aspects were not tested because the main objective of this assignment is functional correctness and understanding testing principles.


## Testing Pyramid

This project follows the Testing Pyramid concept:

- Most tests are Unit Tests (engine logic)
- A smaller number are Integration Tests (controller flow)
- No end-to-end system tests were implemented

This reflects the recommended structure where unit tests form the base of the pyramid.


## Black-box vs White-box Testing

- Unit tests use white-box testing, since internal methods are directly tested.
- Integration tests act more like black-box tests, since they simulate user input without accessing internal engine details.


## Functional vs Non-Functional Testing

- Functional testing was implemented (correct arithmetic behavior).
- Non-functional aspects such as performance and usability were not tested.


## Regression Testing

The test suite can be used as regression protection.
If future changes break existing functionality, the failing tests will immediately reveal the issue.


## Test Results Summary

| Test Name | Type | Status |
|-----------|------|--------|
| test_addition | Unit | Pass |
| test_subtraction | Unit | Pass |
| test_multiplication | Unit | Pass |
| test_division | Unit | Pass |
| test_division_by_zero | Unit | Pass |
| test_negative_numbers | Unit | Pass |
| test_decimal_numbers | Unit | Pass |
| test_clear | Unit | Pass |
| test_full_flow_addition | Integration | Pass |
| test_clear_resets_display | Integration | Pass |