# Basket Pricer

Basket Pricer is a component of a customer checkout system which calculates the price of a customers basket before and after discounts have been applied.

Basket pricer accepts 3 arguments:

* Customer basket (a list of dictionaries containing product name and quantity)
* shop catalogue (a list of dictionaries containing products and prices)
* offers (a list of offers with dynamic contents depending on the offer type, more below)

Basket pricer returns a dictionary that looks like the following:

```JSON
{
    "sub-total": 6.96,
    "discount": 0.95,
    "total": 6.01
}
```

## Installation

0. Install Python 3.7 and pipenv on your dev machine
1. Clone the repo `git clone https://github.com/pfizer/cat-base-sam`
2. Install requirements `make install`
3. Confirm tests work with `make test`

## Testing

This component uses Unittest to test it's features.

In development, utilise your IDE's debugger as often as possible. There is tons of information on the internet for how to install and use debuggers. VSCode has a brilliant Python debugger which you should be using all the time.

Important
* Print out only what you abolutely need to.
* Mock and Patch functions you are interacting with, but not testing.
* Aim for 70% test coverage.
* Remember: You are paid to write working code, not tests. 100% test coverage isn't our goal.

If you _have_ to run tests outside of your IDE's debugger:

Run all test suites:

```
make test
```

Run single suite of tests:

```
python3 -m unittest shopping_basket_tests/test_Filter.py
```

Run one test method:

```
python3 -m pytest shopping_basket_tests/test_Filter.py -k "test_defaultFilter"
```

## API

### CLI

### Importing Directly