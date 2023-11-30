#Data Ingection part. Data have to be injected or need to bring from yaml file. 

from dataclasses import dataclass 
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

    # DataIngestionConfig is an entity. if one function defined with return type as this entity,
    #  that function should return 4 variable values (with data type defined) as mentioned in entity