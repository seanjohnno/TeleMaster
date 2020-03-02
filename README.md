# TeleMaster
Displays various views on publicly available telephone mast data

## To run
* ```cd``` to base directory, run ```python main.py```

## To run tests
* ```cd``` to base directory, run ```python -m unittest discover ./tests/ "test_*.py"```

## Outstanding/Issues
Had to rush through to the finish in the end. There's a couple of bits I'd spend more time on:
* telemaster_service.py - It's basically glue code but it needs some tests + the duplication can be extracted out
* main.py - It's just plain ugly. I was planning on creating a dictionary of numbers to actions and having the console output iterate though that / retrieve the action through user supplied input
* Bumped into some gotchas with Pythons equality comparisons that I only caught while manual testing. My initial unit tests/mocking were duff (see commit history)
