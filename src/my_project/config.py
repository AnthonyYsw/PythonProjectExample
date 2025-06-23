# This file is to configure the project settings. It loads configuration from a TOML file located two directories up from this file.

import tomllib
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
grandparent_dir = os.path.dirname(parent_dir)

def load_toml() -> dict:
    """
    Load the configuration from a TOML file.
    """
    # Find config.toml
    toml_path = os.path.join(grandparent_dir, 'config.toml')

    with open(toml_path, 'rb') as f:
        toml_data: dict = tomllib.load(f)
        return toml_data
    
config_data: dict = load_toml()

