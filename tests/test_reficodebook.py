import uuid
import pytest
from pyrefiqda.models import (
    CodeBook,
    CodebookCodesType,
    CodebookCodeType
)
from pyrefiqda.reficodebook import RefiCodebook

def test_create_save_load_codebook_from_scratch(tmp_path):
    # Create a code for the codebook
    new_code = CodebookCodeType(
        guid=str(uuid.uuid4()),
        name="Code",
        color="#00FF00",
        is_catch_all=False,
        is_codable=True
    )
    
    codes = CodebookCodesType(code=[new_code])
    
    # Assemble the main CodeBook
    my_codebook = CodeBook(
        origin="example",
        guid=str(uuid.uuid4()),
        codes=codes
    )

    # Save it to a temporary file
    output_filepath = tmp_path / "ai_codebook.qdc"
    RefiCodebook.save(my_codebook, output_filepath)

    # Load it back
    loaded_codebook = RefiCodebook.load(output_filepath)

    # Assert it loaded correctly
    assert loaded_codebook is not None
    assert loaded_codebook.origin == "example"
    
    # Verify the code survived the round-trip
    assert len(loaded_codebook.codes.code) == 1
    assert loaded_codebook.codes.code[0].name == "Code"
    assert loaded_codebook.codes.code[0].color == "#00FF00"

def test_missing_codebook_file():
    with pytest.raises(FileNotFoundError):
        RefiCodebook.load("non_existent_codebook.qdc")