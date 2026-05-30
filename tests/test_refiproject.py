import pytest
import uuid
from pathlib import Path
from pyrefiqda.models import (
    Project, 
    UsersType, 
    UserType, 
    ProjectCodeBookType, 
    ProjectCodesType, 
    ProjectCodeType,
    SourcesType,
    TextSourceType,
    PlainTextSelectionType,
    CodingType,
    CodeRefType
)
from pyrefiqda import RefiProject

def test_missing_file():
    with pytest.raises(FileNotFoundError):
        RefiProject.load("does_not_exist.qdpx")

def test_create_save_load(tmp_path):
    # Create a user
    user = UserType(
        guid=str(uuid.uuid4()), 
        name="Coder"
    )
    users = UsersType(user=[user])
    
    # Create a simple Codebook with one Code
    new_code = ProjectCodeType(
        guid=str(uuid.uuid4()),
        name="Code",
        color="#FF0000",
        is_catch_all=False,
        is_codable=True
    )
    codebook = ProjectCodeBookType(
        codes=ProjectCodesType(code=[new_code])
    )

    # Assemble the main Project
    my_project = Project(
        name="Study",
        origin="example",
        users=users,
        code_book=codebook
    )

    # Save to a .qdpx file
    output_filepath = tmp_path / "generated.qdpx"
    RefiProject.save(my_project, output_filepath)

    # Load it back
    loaded_project = RefiProject.load(output_filepath, extract_dir=tmp_path / "extract")

    # Perform assertions to verify the round-trip integrity
    assert loaded_project is not None
    assert loaded_project.name == "Study"
    assert loaded_project.origin == "example"
    # Verify the user survived the round-trip
    assert len(loaded_project.users.user) == 1
    assert loaded_project.users.user[0].name == "Coder"
    
    # Verify the code survived the round-trip
    assert loaded_project.code_book.codes.code[0].name == "Code"

def test_full_end_to_end_project_with_sources(tmp_path):
    # Set up dummy data
    data_dir = tmp_path / "test_data"
    data_dir.mkdir()
    dummy_txt = data_dir / "interview.txt"
    DUMMY_CONTENT = "Hello world, this is a qualitative interview about AI."
    dummy_txt.write_text(DUMMY_CONTENT, encoding="utf-8")
    
    # This is the temporary folder where we build the project before zipping
    build_dir = tmp_path / "build_project"
    
    # Import the source file
    source_guid = str(uuid.uuid4())
    internal_uri = RefiProject.import_source_file(dummy_txt, build_dir, source_guid)
    
    # Assemble Pydantic models
    user = UserType(guid=str(uuid.uuid4()), name="Coder 1")
    
    code1 = ProjectCodeType(
        guid=str(uuid.uuid4()), 
        name="Greetings", 
        color="#FF0000", 
        is_codable=True
    )
    
    # Create a selection that highlights "Hello world" (chars 0 to 11)
    coding = CodingType(
        guid=str(uuid.uuid4()), 
        creating_user=user.guid, 
        code_ref=CodeRefType(target_guid=code1.guid)
    )
    
    selection = PlainTextSelectionType(
        guid=str(uuid.uuid4()), 
        name="Greeting Segment", 
        start_position=0, 
        end_position=11, 
        creating_user=user.guid,
        coding=[coding]
    )
    
    # Attach the internal URI to the TextSource
    text_source = TextSourceType(
        guid=source_guid, 
        name="Interview 1", 
        plain_text_path=internal_uri, 
        plain_text_selection=[selection]
    )
    
    project = Project(
        guid=str(uuid.uuid4()), 
        name="Test Project",
        users=UsersType(user=[user]),
        code_book=ProjectCodeBookType(codes=ProjectCodesType(code=[code1])),
        sources=SourcesType(text_source=[text_source])
    )
    
    # Save the project to a .qdpx file, ensuring the sources folder is included
    qdpx_path = tmp_path / "final_output.qdpx"
    RefiProject.save(project, qdpx_path, source_media_dir=build_dir / "sources")
    
    # Load it back to a fresh directory
    extract_dir = tmp_path / "fresh_extraction"
    loaded_project = RefiProject.load(qdpx_path, extract_dir=extract_dir)
    
    # Verify everything survived the round-trip
    assert loaded_project is not None
    assert loaded_project.name == "Test Project"
    
    # Check that the code is linked to the selection
    loaded_source = loaded_project.sources.text_source[0]
    loaded_selection = loaded_source.plain_text_selection[0]
    assert loaded_selection.name == "Greeting Segment"
    assert loaded_selection.coding[0].code_ref.target_guid == code1.guid
    
    # Verify the file content survived
    resolved_path = RefiProject.resolve_source_path(loaded_source.plain_text_path, extract_dir)
    
    assert resolved_path.exists()
    assert resolved_path.read_text(encoding="utf-8") == DUMMY_CONTENT