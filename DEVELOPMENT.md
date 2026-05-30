# Development & Maintenance Guide

This document contains instructions for the maintainers of `pyrefiqda` on how to regenerate the data models and publish new versions to PyPI. 

## Environment Setup
Create the environment and install build tools:

```bash
python -m venv venv
source venv/bin/activate

# Install the necessary build tools and the xsdata pydantic plugin
pip install build twine xsdata[cli,lxml] xsdata-pydantic
```

## Regenerating the Pydantic Models
If the REFI-QDA standard updates, replace the `.xsd` files in the `refi-qda-standard/` folder and run:

```bash
xsdata generate refi-qda-standard/ --output pydantic --package pyrefiqda.models
```

## Publishing to PyPI
Remember to increment the `version` in `pyproject.toml` before building.

```bash
# Clean old builds (optional but recommended)
rm -rf dist/

# Build and upload package
python -m build
python -m twine upload dist/*
```
