install:
	pipenv install

test:
	pytest ./shopping_basket_tests -vvv

# Validate Python code according to the style guide.
flake:
	flake8 .

# Reformat Python code according to the style guide.
black:
	black .

testcli:
	py ./basket_pricer.py shopping_basket_tests/fixtures/test_basket_one.json shopping_basket_tests/fixtures/test_catalogue.json shopping_basket_tests/fixtures/test_offers.json