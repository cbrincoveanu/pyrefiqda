import zipfile
from pathlib import Path
from xsdata_pydantic.bindings import XmlParser, XmlSerializer
from .models import Project

class RefiProject:
    """Handler for REFI-QDA Project (.qdpx) files.
    
    A `.qdpx` file is a zipped archive containing a primary XML project file 
    and optional external sources (like PDFs or media).
    """

    @staticmethod
    def load(file_path: str | Path, extract_dir: str = "./extracted_qdpx") -> Project:
        """Unzips a .qdpx file and parses the internal XML into Pydantic models.

        Args:
            file_path: The path to the existing `.qdpx` project file.
            extract_dir: The directory where the zipped archive will be extracted. 
                Defaults to "./extracted_qdpx".

        Returns:
            Project: The strictly-typed Pydantic Project model containing all qualitative data.

        Raises:
            FileNotFoundError: If the provided `.qdpx` file does not exist, or if 
                no `.qde` XML file is found inside the extracted archive.

        Example:
            ```python
            from pyrefiqda import RefiProject
            project = RefiProject.load("study.qdpx", extract_dir="./temp_extract")
            ```
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
        """Serializes a Project Pydantic model back to XML and packages it into a .qdpx zip archive.

        This method handles the standard compression required by the REFI-QDA
        specification, ensuring it can be opened by NVivo, MAXQDA, etc.

        Args:
            project: The populated Pydantic Project model.
            file_path: The destination path where the .qdpx file will be saved.

        Raises:
            IOError: If there is an issue writing to the destination path.

        Example:
            ```python
            from pyrefiqda import RefiProject
            
            RefiProject.save(my_project, "project.qdpx")
            ```
        """
        file_path = Path(file_path)
        
        # 1. Serialize the Pydantic model back to an XML string
        serializer = XmlSerializer()
        xml_string = serializer.render(project)
        
        # 2. Package it into a .qdpx (zip) file
        with zipfile.ZipFile(file_path, 'w') as zip_ref:
            # Write the XML string directly into the zip archive as a .qde file
            zip_ref.writestr("project.qde", xml_string)