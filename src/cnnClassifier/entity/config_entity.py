from dataclasses import dataclass
from pathlib import Path

#custom return type using entity
@dataclass(frozen= True)
class DataIngestionConfig:
    """
    Data Ingestion Config
    """
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path