# pyrefiqda

[![PyPI version](https://badge.fury.io/py/pyrefiqda.svg)](https://pypi.org/project/pyrefiqda/)
[![Python Versions](https://img.shields.io/pypi/pyversions/pyrefiqda.svg)](https://pypi.org/project/pyrefiqda/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

A modern Python library mapping REFI-QDA qualitative research files (.qdpx, .qdc) to strict Pydantic models for seamless programmatic integration.

Created to bridge the gap between qualitative coding software (NVivo, MAXQDA, ATLAS.ti) and Python workflows. 

📖 **[Read the Full Documentation and API Reference here](https://cbrincoveanu.github.io/pyrefiqda)**

## Core Features
* **100% Type-Hinted:** Built entirely on Pydantic `BaseModel` classes, ensuring perfect IDE autocomplete and seamless integration with frameworks like PydanticAI.
* **Standard Compliant:** Reads and writes `.qdpx` (Project) and `.qdc` (Codebook) formats.
* **Media Management:** Includes helper functions to abstract away REFI-QDA's internal URI structures, making it easy to read transcripts and package media back into archives.

## Installation

```bash
pip install pyrefiqda
```

## Why this exists
In qualitative studies, researchers use the REFI-QDA standard to exchange data. However, previous Python tools were GUI-heavy or outdated. `pyrefiqda` uses `xsdata` to auto-generate pure Pydantic models directly from the official XML schemas. This abstracts away zipped archives and internal URIs, giving you flawless type-hinting and programmatic access to qualitative data.

## Showcase
`pyrefiqda` makes it incredibly easy to programmatically assemble qualitative coding projects from scratch, package media files, and export standard `.qdpx` files ready for  exchange and review.

```python
import uuid
from pyrefiqda.refiproject import RefiProject
from pyrefiqda.models import (
    Project, UsersType, UserType, ProjectCodeBookType, 
    ProjectCodesType, ProjectCodeType, SourcesType, 
    TextSourceType, PlainTextSelectionType, CodingType, CodeRefType
)

# 1. Import a raw transcript into the REFI-QDA working directory
working_dir = "./temp_project"
internal_uri = RefiProject.import_source_file("raw_data/interview.txt", working_dir)

# 2. Define a Coder and an emergent Code
user = UserType(guid=str(uuid.uuid4()), name="Coder 1")
code = ProjectCodeType(
    guid=str(uuid.uuid4()), name="Theme 1", color="#FF0000"
)

# 3. Create a coding selection (e.g., characters 0 through 100)
selection = PlainTextSelectionType(
    guid=str(uuid.uuid4()),
    name="Identified Segment",
    start_position=0,
    end_position=100,
    creating_user=user.guid,
    coding=[CodingType(
        guid=str(uuid.uuid4()), 
        creating_user=user.guid, 
        code_ref=CodeRefType(target_guid=code.guid)
    )]
)

# 4. Assemble the final Pydantic Project
project = Project(
    name="GTM Study",
    users=UsersType(user=[user]),
    code_book=ProjectCodeBookType(codes=ProjectCodesType(code=[code])),
    sources=SourcesType(text_source=[
        TextSourceType(
            guid=str(uuid.uuid4()), 
            name="Interview 1", 
            plain_text_path=internal_uri, 
            plain_text_selection=[selection]
        )
    ])
)

# 5. Export to a standard .qdpx file (zipping the XML and the media files together)
RefiProject.save(project, "study.qdpx", source_media_dir=working_dir + "/sources")
```