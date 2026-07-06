import os
import zipfile
import shutil
import uuid
from pathlib import Path
from xsdata_pydantic.bindings import XmlParser, XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
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
    def save(project: Project, file_path: str | Path, source_media_dir: str | Path | None = None) -> None:
        """Serializes a Project Pydantic model back to XML and packages it into a .qdpx zip archive.

        This method handles the standard compression required by the REFI-QDA
        specification, ensuring it can be opened by NVivo, MAXQDA, etc.

        Args:
            project: The populated Pydantic Project model.
            file_path: The destination path where the .qdpx file will be saved.
            source_media_dir: (Optional) The local directory containing the source files 
                (e.g., PDFs, images) that need to be packaged into the archive's `sources/` folder.

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
        config = SerializerConfig(xml_declaration=True, encoding="UTF-8")
        serializer = XmlSerializer(config=config)
        xml_string = serializer.render(project, ns_map={None: "urn:QDA-XML:project:1.0"})
        
        # 2. Package it into a .qdpx (zip) file
        with zipfile.ZipFile(file_path, 'w') as zip_ref:
            # Write the XML string directly into the zip archive as a .qde file
            zip_ref.writestr("project.qde", xml_string)

            # Package all source files if a directory was provided
            if source_media_dir:
                source_path = Path(source_media_dir)
                if source_path.exists() and source_path.is_dir():
                    for root, _, files in os.walk(source_path):
                        for file in files:
                            local_file = Path(root) / file
                            # Preserve the 'sources/' folder structure inside the zip
                            arcname = f"sources/{file}"
                            zip_ref.write(local_file, arcname=arcname)
    
    @staticmethod
    def resolve_source_path(internal_path: str, extract_dir: str | Path) -> Path:
        """Resolves a REFI-QDA internal path to an actual local file path.
        
        REFI-QDA projects store media and text files inside a `sources/` directory 
        and reference them using an `internal://` URI scheme. This helper translates 
        that URI into a usable Python `Path` object pointing to the extracted file.

        Args:
            internal_path: The REFI-QDA internal URI string (e.g., `"internal://<GUID>.txt"`).
            extract_dir: The local directory where the `.qdpx` archive was originally extracted.

        Returns:
            Path: The resolved local filesystem path pointing to the source file.

        Raises:
            ValueError: If the provided `internal_path` does not start with `"internal://"`.
        
        Example: 
            ```python
            from pyrefiqda import RefiProject
            project = RefiProject.load("research.qdpx", extract_dir="./temp_project")

            # Analyze transcripts
            for source in project.sources.text_source:
                # Use helper to find the actual file on the hard drive
                local_path = RefiProject.resolve_source_path(
                    source.plain_text_path, 
                    "./temp_project"
                )
                
                with open(local_path, "r", encoding="utf-8") as f:
                    transcript_text = f.read()
                    
                print(transcript_text)
            ```
        """
        if not internal_path.startswith("internal://"):
            raise ValueError("Provided path is not a valid REFI-QDA internal path.")
        
        filename = internal_path.replace("internal://", "")
        return Path(extract_dir) / "sources" / filename
    
    @staticmethod
    def import_source_file(local_file_path: str | Path, extract_dir: str | Path, source_guid: str | None = None) -> str:
        """Copies a local file into the project's sources directory and returns its REFI-QDA internal URI.

        This method ensures full compliance with the REFI-QDA standard by copying the file 
        into a `sources/` subfolder and renaming it to a unique GUID while preserving 
        the original file extension.

        Args:
            local_file_path: The path to the raw media/text file you want to add to the project.
            extract_dir: The temporary working directory for your project.
            source_guid: (Optional) A specific GUID to use. If None, a new UUID4 is generated.

        Returns:
            str: The properly formatted REFI-QDA internal URI (e.g., `"internal://<GUID>.pdf"`).

        Raises:
            FileNotFoundError: If the provided `local_file_path` does not exist.

        Example:
            ```python
            from pyrefiqda import RefiProject
            
            internal_uri = RefiProject.import_source_file(
                "raw_data/interview1.docx", 
                "./working_dir"
            )
            print(internal_uri) # Output: internal://b5566006-eb5f-43f0...docx
            ```
        """
        local_file_path = Path(local_file_path)
        extract_dir = Path(extract_dir)
        
        if not local_file_path.exists():
            raise FileNotFoundError(f"Source file not found: {local_file_path}")
            
        # Ensure the sources directory exists
        sources_dir = extract_dir / "sources"
        sources_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate GUID if not provided
        guid = source_guid or str(uuid.uuid4())
        
        # Standard mandates: GUID as filename, retaining original extension
        ext = local_file_path.suffix
        new_filename = f"{guid}{ext}"
        
        # Copy the file into the project's source directory
        dest_path = sources_dir / new_filename
        shutil.copy2(local_file_path, dest_path)
        
        # Return the internal URI string
        return f"internal://{new_filename}"