# creating entity means return typeof function 
# This is entity
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path
    source_URL:str
    local_data_file:Path
    unzip_dir:Path


@dataclass(frozen=True)
class DatavalidationConfig:
    root_dir:Path
    STATUS_FILE:str
    ALL_REQUIRED_FILES:list

@dataclass(frozen=True)
class DataTransformConfig:
    root_dir:Path
    data_path:Path
    tokenizer_name:Path