from dataclasses import dataclass
from pathlib import Path

@dataclass#Automatically handles initialization and object printing
class DataIngestionConfig:
    root_dir:Path
    source_URL: str
    local_data_files: Path
    unzip_dir: Path
    
    
@dataclass
class DataValidationConfig:
    root_dir: Path
    data_path: Path
    STATUS_FILE: Path
    all_schema: dict

@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
