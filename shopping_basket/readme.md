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
1. Clone the repo `git clone https://github.com/StuMason/cx-interview-questions`
2. Install requirements `make install`
3. Confirm tests work with `make test`

## Testing

This component uses a combination of Unittest and Pytest to test it's features.

Run all test suites:

```BASH
make test
```

Run single suite of tests:

```BASH
python3 -m unittest shopping_basket_tests/test_basket_pricer.py
```

Run one test method:

```BASH
pytest ./shopping_basket_tests -vvv -s -k "test_defaultFilter"
```

## API

### CLI

You can run `basket_pricer.py` in terminal directly by passing it three arguments - being the locations for json files for the basket, catalogue and offers, i.e.

```BASH
python3 ./basket_pricer.py shopping_basket_tests/fixtures/test_basket_one.json shopping_basket_tests/fixtures/test_catalogue.json shopping_basket_tests/fixtures/test_offers.json
```

The above command uses test json files within the fixtures directory.

It outputs a JSON formatted string to the terminal.

### Importing Directly

You can import the basket pricer directly