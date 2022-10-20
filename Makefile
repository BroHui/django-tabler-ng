branch:
ifeq ($(shell git rev-parse --abbrev-ref HEAD), master)
	@echo "On branch master."
else
	@echo "Error - Not on branch master!"
	@exit 1;
endif

publish:
	python setup.py sdist bdist_wheel
	twine check dist/*
	twine upload dist/*