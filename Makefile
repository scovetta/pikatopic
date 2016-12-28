

all:
	@echo "try:"
	@echo "     make clean"
	@echo "     make run-sdist"
	@echo "     make run-upload-to-pypi"

clean:
	rm -rf README.rst dist *.egg-info

README.rst: README.md
	pandoc README.md -o README.rst

run-sdist: README.rst
	python setup.py sdist

run-upload-to-pypi:
	@echo "not implemented"
