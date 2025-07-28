import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations #this decorator ensures that the function has the necessary annotations
def read_yaml(file_to_yaml: Path) -> ConfigBox:
    try:
        with open(file_to_yaml) as yaml_file:
            content =  yaml.safe_load(file)
            logger.info(f"Successfully loaded YAML file: {file_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"File '{file_to_yaml}' not found.")
    except Exception as e:
        raise e
    
    
@ensure_annotations
def create_directories(path_to_directories:list , verbose=True):
    for path in path_to_directories:
        os.makedirs(path , exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {path}")

@ensure_annotations
def get_size(path:Path)->str:
    size_in_kb = round( os.path.getsize(path) / 1024)
    return f"{size_in_kb} KB"

