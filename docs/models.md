# Data Models

`pyrefiqda` uses Pydantic to strictly type the REFI-QDA standard. Below is the API reference for the core models, logically grouped by qualitative research concepts.

## Core Hierarchy
The root elements of your research files.

::: pyrefiqda.models.Project
::: pyrefiqda.models.CodeBook

## Users
Models representing human or AI coders.

::: pyrefiqda.models.UsersType
::: pyrefiqda.models.UserType

## Codebook Elements
Types defining your codes, coding hierarchies, and sets.

::: pyrefiqda.models.ProjectCodeBookType
::: pyrefiqda.models.ProjectCodesType
::: pyrefiqda.models.ProjectCodeType
::: pyrefiqda.models.ProjectSetsType
::: pyrefiqda.models.ProjectSetType

## Sources & Transcripts
Models representing the actual qualitative data (documents, audio, video).

::: pyrefiqda.models.SourcesType
::: pyrefiqda.models.TextSourceType
::: pyrefiqda.models.TranscriptType
::: pyrefiqda.models.AudioSourceType
::: pyrefiqda.models.VideoSourceType
::: pyrefiqda.models.PictureSourceType
::: pyrefiqda.models.PdfsourceType

## Codings & Selections
Models representing the application of a code to a specific segment of text or media.

::: pyrefiqda.models.CodingType
::: pyrefiqda.models.PlainTextSelectionType
::: pyrefiqda.models.AudioSelectionType
::: pyrefiqda.models.VideoSelectionType
::: pyrefiqda.models.PictureSelectionType
::: pyrefiqda.models.PdfselectionType

## Cases & Variables
Models for defining case logic and mixed-methods variables.

::: pyrefiqda.models.CasesType
::: pyrefiqda.models.CaseType
::: pyrefiqda.models.VariablesType
::: pyrefiqda.models.VariableType
::: pyrefiqda.models.VariableValueType
::: pyrefiqda.models.TypeOfVariableType

## Memos & Links
Models for memos (notes), relationships, and concept graphs.

::: pyrefiqda.models.NotesType
::: pyrefiqda.models.LinksType
::: pyrefiqda.models.GraphsType