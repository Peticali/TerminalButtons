
from setuptools import setup, find_packages
import pathlib, platform


HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="TerminalButtons",
    version="1.0.0",
    description="Buttons in Linux terminal",
    url="https://github.com/Peticali/TerminalButtons",
    author="Peticali",
    long_description_content_type="text/markdown",
    long_description=README,   
    author_email="pedropalmeira68@gmail.com",
    license="MIT",
    py_modules=['TerminalButtons']
)