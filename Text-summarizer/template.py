import os
from pathlib import Path # to handles errors related to path so it dont throw the error
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name="textSummarizer"
list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "test.py"
]

for filepath in list_of_files:
    # Convert the string path into a Path object for better cross-platform compatibility
    filepath = Path(filepath)

    # Split the path into directory and file name
    filedir, filename = os.path.split(filepath)

    # Check if the directory part of the path is not empty
    if filedir != "":
        # Create the directory if it doesn't exist
        os.makedirs(filedir, exist_ok=True)
        # Log the creation of the directory
        logging.info(f"Created directory: {filedir} for the {filename}")

    # Check if the file doesn't exist or if it exists but is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # Create an empty file
        with open(filepath, "w") as f:
            pass  # No content is written, just creating the file
        # Log the creation of the file
        logging.info(f"Created file: {filepath}")
    else:
        # If the file already exists and is not empty, log that information
        logging.info(f"File {filepath} already exists.")


