install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	ruff *.py

format:	
	black *.py 

test:
	python -m pytest test_script.py 
	python -m pytest test_lib.py
	#python -m pytest descriptive_stats.ipynb --nbval
	
		
all: install lint format test 