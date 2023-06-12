from dataclasses import dataclass
from pathlib import Path

#custom return type using entity
#entity for Data ingestion
@dataclass(frozen= True)
class DataIngestionConfig: 
    """
    Data Ingestion Config
    """
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

#entity for prepare_base_model
@dataclass
class PrepareBaseModelConfig:
    root_dir:Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int    


#entity for callbacks
@dataclass
class PrepareCallbacksConfig:
    root_dir:Path
    tensorboard_root_log_dir: Path
    checkpoint_model_filepath: Path 


#entity for model training
@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    params_epochs: int
    params_batch_size: int
    params_is_augmentation: bool
    params_image_size: list


#entity for model evaluation
@dataclass(frozen=True)
class EvaluationConfig:
    path_of_model: Path
    training_data: Path
    all_params: dict
    params_image_size: list
    params_batch_size: int