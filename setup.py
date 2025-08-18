import setuptools

# Open the README.md file and read its content into the 'long_description' variable.
# This will be used to provide a detailed description of the package on platforms like PyPI.
with open("Readme.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Define the version of the package.
__version__ = "0.0.0"

# Metadata about the package
REPO_NAME = "Text_summarizer"         # The name of the repository on GitHub.
AUTHOR_USER_NAME = "puzan789"         # The GitHub username of the author.
SRC_REPO = "textSummarizer"           # The name of the source directory for the package.
AUTHOR_EMAIL = "puzan936@gmail.com"   # The author's email address.

# Setup function to define the package details.
setuptools.setup(
    name=SRC_REPO,                    # The name of the package.
    version=__version__,              # The current version of the package.
    author=AUTHOR_USER_NAME,          # The name of the package author.
    author_email=AUTHOR_EMAIL,        # The email address of the author.
    description="A text summarization tool",  # A short description of the package.
    long_description=long_description,       # A detailed description (from README.md).
    long_description_content="text/markdown", # Specifies that the long description is in Markdown format.
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",  # URL for the bug tracker (GitHub issues page).
    },
    packages=setuptools.find_packages(where="src"),  # Automatically find all packages inside the 'src' directory.
    package_dir={"": "src"},  # Tells setuptools that the package code is located in the 'src' directory.
)
