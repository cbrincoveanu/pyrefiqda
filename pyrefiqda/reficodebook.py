from pathlib import Path
from xsdata_pydantic.bindings import XmlParser, XmlSerializer
from .models import CodeBook

class RefiCodebook:
    @staticmethod
    def load(file_path: str | Path) -> CodeBook:
        """
        Parses a REFI-QDA Codebook (.qdc) XML file into a Pydantic CodeBook model.
        Note: .qdc files are standard XML, not zipped archives like .qdpx.
        """
        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"Codebook file not found: {file_path}")
        
        parser = XmlParser()
        return parser.parse(str(file_path), CodeBook)

    @staticmethod
    def save(codebook: CodeBook, file_path: str | Path):
        """
        Serializes a CodeBook Pydantic model back to XML and saves it as a .qdc file.
        """
        file_path = Path(file_path)
        
        serializer = XmlSerializer()
        xml_string = serializer.render(codebook)
        
        # Write the XML string directly to the file
        file_path.write_text(xml_string, encoding="utf-8")