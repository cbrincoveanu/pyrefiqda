import pytest
import uuid
from pyrefiqda.models import (
    Project,
    UsersType,
    UserType,
    ProjectCodeBookType,
    ProjectCodesType,
    ProjectCodeType
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