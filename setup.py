import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text_Summarization_Project"
AUTHOR_USER_NAME = "allu0786ansari"
SRC_REPO = "Text_Summarization_Project"
AUTHOR_EMAIL = "allu456654ansari@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}/issues",
        "Documentation": f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}/blob/main/README.md",
        "Source Code": f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),


)