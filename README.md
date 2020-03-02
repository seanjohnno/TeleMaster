# TeleMaster
Displays various views on publicly available telephone mast data

## To run
* ```cd``` to base directory, run ```python main.py```

## To run tests
* ```cd``` to base directory, run ```python -m unittest discover ./tests/ "test_*.py"```

## Outstanding/Issues
* main.py / telemaster_service.py have been rushed and could be better:
** telemaster_service.py - It's basically glue code but it needs some tests + a lot of the duplication can be extracted out
** main.py - With more time, I was planning on creating a dictionary of numbers to actions and descriptions
* Bumped into some gotchas with Pythons equality comparisons that I only caught while manual testing. My initial unit tests/mocking were duff (see commit history)
