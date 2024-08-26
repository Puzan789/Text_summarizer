import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from typing import Any
from pathlib import Path


@ensure_annotations #
def read_yaml(path_to_yaml:Path)->ConfigBox :
    """
    Reads a YAML file and returns a Box object containing the data.

    Args:
        path_to_yaml (path): The path to the YAML file.

    Returns:
        ConfigBox: A Box object containing the data from the YAML file.

    Raises:
        BoxValueError: If the YAML file is invalid.
    """
    try :
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml_file:{path_to_yaml} loaded successfully")
            return ConfigBox(content) # return a ConfigBox object
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def get_size(path:Path)-> str:
    """
    Returns the size of a file in kb.

    Args:
        path (Path): The path to the file.

    Returns:
        str: The size of the file in kb.
    """
    size_in_kb =round(os.path.getsize(path)/1024)
    return f" ~{size_in_kb} KB"















"""

from box import ConfigBox

# Sample configuration data, could be loaded from a YAML or JSON file
config_data = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "user": "admin",
        "password": "secret"
    },
    "logging": {
        "level": "INFO",
        "handlers": ["console", "file"]
    },
    "features": {
        "enable_feature_x": True,
        "max_retries": 5
    }
}

# Convert the dictionary to a ConfigBox object
config = ConfigBox(config_data)

# Accessing configuration using dot notation
print("Database Host:", config.database.host)         # Outputs: localhost
print("Database Port:", config.database.port)         # Outputs: 5432
print("Logging Level:", config.logging.level)         # Outputs: INFO

# Accessing nested configuration using dot notation
print("Is Feature X Enabled?", config.features.enable_feature_x)  # Outputs: True
print("Max Retries:", config.features.max_retries)                # Outputs: 5

# Modifying values
config.database.user = "new_user"
print("Updated Database User:", config.database.user)  # Outputs: new_user

# Adding new keys dynamically
config.new_feature = {"enabled": True, "version": "1.0"}
print("New Feature Enabled:", config.new_feature.enabled)  # Outputs: True
print("New Feature Version:", config.new_feature.version)  # Outputs: 1.0

# Handling missing keys (this will raise an error)
try:
    print(config.database.non_existent_key)
except KeyError as e:
    print("KeyError:", e)  # Outputs: KeyError: 'non_existent_key'
```

### Explanation of the Example:

1. **Creating `ConfigBox`**:
   - We start with a regular Python dictionary `config_data` that contains some nested configuration data. This dictionary is then passed to the `ConfigBox` constructor to create a `ConfigBox` object.

2. **Accessing Values**:
   - You can access the values in the configuration using dot notation (e.g., `config.database.host`). This is much cleaner and more intuitive than using standard dictionary access methods like `config['database']['host']`.

3. **Modifying Values**:
   - You can easily modify existing values using dot notation (e.g., `config.database.user = "new_user"`).

4. **Adding New Keys**:
   - New keys can be added dynamically using dot notation, and these new keys can also be accessed in the same way (e.g., `config.new_feature.enabled`).

5. **Handling Missing Keys**:
   - If you try to access a key that doesn't exist in the `ConfigBox`, it will raise a `KeyError`, which helps in identifying mistakes early in the code.

"""