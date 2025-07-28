import setuptools

with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()
    
__version__ = "0.0.0"

REPO_NAME = "Text-summarizer"
AUTHOR_USER_NAME= "V Shreya"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "vshreya54321@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text summarization tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VShreya/Text-summarizer",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ]
    project_urls={
        "bug tracker": "https://github.com/VShreya/Text-summarizer/issues"
    }
    
)