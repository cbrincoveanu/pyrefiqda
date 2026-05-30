from pathlib import Path
from xsdata_pydantic.bindings import XmlParser, XmlSerializer
from .models import CodeBook

class RefiCodebook:
    """Handler for standalone REFI-QDA Codebook (.qdc) files.
    
    Unlike `.qdpx` projects, `.qdc` files are plain XML files used strictly 
    for exchanging coding hierarchies without media sources.
    """

    @staticmethod
    def load(file_path: str | Path) -> CodeBook:
        """Parses a REFI-QDA Codebook (.qdc) XML file into a Pydantic model.

        Args:
            file_path: The path to the existing `.qdc` codebook file.

        Returns:
            CodeBook: The strictly-typed Pydantic CodeBook model.

        Raises:
            FileNotFoundError: If the provided `.qdc` file does not exist.

        Example:
            ```python
            from pyrefiqda import RefiCodebook
            codebook = RefiCodebook.load("initial_codes.qdc")
            ```
        """
        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"Codebook file not found: {file_path}")
        
        parser = XmlParser()
        return parser.parse(str(file_path), CodeBook)

    @staticmethod
    def save(codebook: CodeBook, file_path: str | Path):
        """Serializes a CodeBook Pydantic model back to XML and saves it as a .qdc file.

        Args:
            codebook: The populated Pydantic CodeBook model.
            file_path: The destination path where the `.qdc` file will be saved.

        Example:
            ```python
            from pyrefiqda import RefiCodebook
            RefiCodebook.save(my_codebook, "updated_codes.qdc")
            ```
        """
        file_path = Path(file_path)
        
        serializer = XmlSerializer()
        xml_string = serializer.render(codebook)
        
        # Write the XML string directly to the file
        file_path.write_text(xml_string, encoding="utf-8")