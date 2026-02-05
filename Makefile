# Makefile so you don't have to remember the exact commands

build: ux
	uv build

pytest:
	uv run pytest -r A

# untested
upload:
	uv run twine upload dist/*.whl dist/*.tar.gz


#######################################################################
# Aliases for backward compatibility
#######################################################################

sdist: build

wheel: build
