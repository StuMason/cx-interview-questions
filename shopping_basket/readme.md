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
python3 -m unittest tests/test_basket_pricer.py
```

Run one test method:

```BASH
pytest ./tests -vvv -s -k "test_offer_calc_return_value"
```

## Inputs

### Basket

List of products in customers basket.

#### Breakdown

Name | Type | Description | Required
--- | --- | --- | --- | ---
name | *string* | Name of the product | *YES*
quantity | *integer* | Quantity of product in users basket | *YES*

#### Structure

Example structure below:

```JSON
[
    {"name": "Baked Beans", "quantity": 4},
    {"name": "Biscuits", "quantity": 1}
]
```

### Catalogue

List of products a shop has.

#### Breakdown

Name | Type | Description | Required
--- | --- | --- | --- | ---
name | *string* | Name of the product | *YES*
price | *float* | Price of line item | *YES*

#### Structure

Example structure below:

```JSON
[
    {"name":"Baked Beans", "price": 0.99},
    {"name":"Biscuits", "price": 1.20},
    {"name":"Sardines", "price": 1.89},
    {"name":"Shampoo (Small)", "price": 2.00},
    {"name":"Shampoo (Medium)", "price": 2.50},
    {"name":"Shampoo (Large)", "price": 3.50}
]
```

### Offers

List of available offers.

Currently there are only 2 offer types - percentage and bogof. Both of these offers types are customisable using the `details` object.

#### Breakdown

Name | Type | Description | Required
--- | --- | --- | --- | ---
name | *string* | Name of the product | *YES*
discount_type | *string* | Type of discount - directly related to the method in the OfferCalculator class | *YES*
details | *string* | discount_type specific details | *YES*
products | *list* | list of strings of product names that currently are uder this offer | *YES*

#### Structure

Example structure below:

```JSON
[
    {
        "name":"buy two get one free",
        "discount_type": "bogof",
        "details": {
            "buy":2,
            "free":1
        },
        "products": [
            "Baked Beans"
        ]
    },
    {
        "name":"25% off total",
        "discount_type": "percentage",
        "details": {
            "amount": 25
        },
        "products": [
            "Sardines"
        ]
    }
]
```

## CLI

You can run `basket_pricer.py` in terminal directly by passing it three arguments - being the locations for json files for the basket, catalogue and offers, i.e.

```BASH
python3 ./basket_pricer.py tests/fixtures/test_basket_one.json tests/fixtures/test_catalogue.json tests/fixtures/test_offers.json
```

The above command uses test json files within the fixtures directory.

It outputs a JSON formatted string to the terminal.
