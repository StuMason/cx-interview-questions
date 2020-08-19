install:
	pipenv install --pre

test:
	pytest ./tests -vvv

# Validate Python code according to the style guide.
flake:
	flake8 .

# Reformat Python code according to the style guide.
black:
	black .

testcli:
	py ./basket_pricer.py tests/fixtures/test_basket_one.json tests/fixtures/test_catalogue.json tests/fixtures/test_offers.json