

all:
	@echo "try:"
	@echo "     make clean"
	@echo "     make run-sdist"
	@echo "     make run-upload-to-pypi"

clean:
	rm -rf README.rst dist *.egg-info

README.rst: README-pypi.md
	pandoc README-pypi.md -o README.rst

run-sdist: clean README.rst
	python setup.py sdist

run-upload-to-pypi: clean README.rst
	python setup.py register sdist upload
	
