import zipfile
from pathlib import Path
from xsdata_pydantic.bindings import XmlParser, XmlSerializer
from .models import Project

class RefiProject:
    @staticmethod
    def load(file_path: str | Path, extract_dir: str = "./extracted_qdpx") -> Project:
        """
        Unzips a .qdpx file, finds the .qde XML, and parses it into Pydantic models.
        """
        file_path = Path(file_path)
        extract_path = Path(extract_dir)

        # 1. Unzip the .qdpx file
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)

        # 2. Find the .qde XML file inside
        qde_files = list(extract_path.glob("*.qde"))
        if not qde_files:
            raise FileNotFoundError("No .qde file found inside the .qdpx archive.")
        
        qde_file = qde_files[0]

        # 3. Parse the XML into the generated Pydantic models
        parser = XmlParser()
        project = parser.parse(str(qde_file), Project)
        
        return project

    @staticmethod
    def save(project: Project, file_path: str | Path):
        """
        Serializes a Project Pydantic model back to XML and packages it into a .qdpx zip archive.
        """
        file_path = Path(file_path)
        
        # 1. Serialize the Pydantic model back to an XML string
        serializer = XmlSerializer()
        xml_string = serializer.render(project)
        
        # 2. Package it into a .qdpx (zip) file
        with zipfile.ZipFile(file_path, 'w') as zip_ref:
            # Write the XML string directly into the zip archive as a .qde file
            zip_ref.writestr("project.qde", xml_string)