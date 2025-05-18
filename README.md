# Checkout System

This project is a simple implementation of a checkout system written in Python. It calculates the total price of items, applies discounts, and handles exceptions for invalid items. The development process followed the **Test-Driven Development (TDD)** methodology using **pytest**.

## Development Process

The project was built using the **Red-Green-Refactor** cycle of TDD:

1. **Red**: Write failing tests for the desired functionality.
2. **Green**: Implement the minimum code required to make the tests pass.
3. **Refactor**: Clean up the code while ensuring all tests still pass.

## Features

- Add item prices.
- Add items to the checkout.
- Calculate the total price of items.
- Apply discounts based on quantity.
- Handle exceptions for invalid items.

## Files

- `Checkout.py`: Contains the implementation of the checkout system.
- `TestCheckout.py`: Contains the test cases written with pytest to validate the functionality.

## Testing

The tests are written using **pytest**. To run the tests, execute the following command in the terminal:

```bash
pytest TestCheckout.py
```

## Example

- Add prices for items.
- Add items to the checkout.
- Apply discounts (if any).
- Calculate the total price.

This project demonstrates the simplicity and effectiveness of TDD in building reliable software.