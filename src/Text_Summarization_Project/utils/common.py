"""
Code used frequently is stored in utility and called to use in other modules.
"""

import os
from box.exceptions import BoxValueError
import yaml
from Text_Summarization_Project.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read a yaml file and return

    Args:
        path_to_yaml (Path): path like input.

    Raises:
        ValueError: If the yaml is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)

    except BoxValueError:
        raise ValueError("Yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create list of directories

    Args:
        path_to_directories (list): list of path of directories
        verbose (bool, optional): Logs the directory creation. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the size of a file in kb

    Args:
        path (Path): Path of the file
    
    Returns:
        str: Size of the file in kb
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~{size_in_kb} KB"
