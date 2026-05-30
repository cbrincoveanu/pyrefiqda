# pyrefiqda
A modern Python parser mapping REFI-QDA qualitative research files (.qdpx) to strict Pydantic models for seamless integration.

## Installation

```bash
pip install pyrefiqda
```

## Quickstart

### 1. Working with complete Projects (.qdpx)
```python
from pyrefiqda import RefiProject

# Load an existing project (e.g., from NVivo, MAXQDA)
project = RefiProject.load("my_research.qdpx")

# Iterate through your codebook
for code in project.code_book.codes.code:
    print(f"Code: {code.name} (Color: {code.color})")

# Save a modified project back to a file
RefiProject.save(project, "my_research_updated.qdpx")
```

### 2. Working with Standalone Codebooks (.qdc)
If you only need to exchange coding hierarchies, REFI-QDA provides the lightweight `.qdc` format.
```python
from pyrefiqda import RefiCodebook

# Load an existing codebook
codebook = RefiCodebook.load("initial_codes.qdc")

# Add a new code
from pyrefiqda.models import CodebookCodeType
import uuid

new_code = CodebookCodeType(
    guid=str(uuid.uuid4()),
    name="Example code",
    color="#FF5733",
    is_catch_all=False,
    is_codable=True
)
codebook.codes.code.append(new_code)

# Save it back
RefiCodebook.save(codebook, "updated_codes.qdc")
```

### 3. Creating a Project from Scratch
```python
import uuid
from pyrefiqda.models import Project, UsersType, UserType
from pyrefiqda import RefiProject

# Create a user
user = UserType(guid=str(uuid.uuid4()), name="Coder")
users = UsersType(user=[user])

# Initialize an empty project ready for qualitative analysis
my_project = Project(
    name="Example study",
    origin="pyrefiqda",
    guid=str(uuid.uuid4()),
    users=users
)

RefiProject.save(my_project, "new_study.qdpx")
```

## Why this exists

In qualitative studies, researchers use the REFI-QDA standard to exchange data. However, previous Python tools were GUI-heavy or outdated. `pyrefiqda` uses `xsdata` to auto-generate pure Pydantic models directly from the official XML schema, meaning you get flawless type-hinting, validation, and zero parsing bloat.
