"""
Setup.py file.
Install once-off with:  "pip install ."
For development:        "pip install -e .[dev]"
"""
import setuptools


with open("requirements.txt") as f:
    install_requires = f.read().splitlines()

PROJECT_NAME = "myapp"

setuptools.setup(
    name=PROJECT_NAME,
    version="0.0",
    author="Jacopo Margutti",
    author_email="jmargutti@redcross.nl",
    description="template of a python app",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            f"run-app = {PROJECT_NAME}.run:main",
        ]
    }
)