from setuptools import setup, find_packages

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="lingx",
    version="0.1.6",
    description="A library for introducing state-of-the-art metrics on measuring linguistic complexity",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Mehdi Mirzapour",
    author_email="mehdi.mirzapour@gmail.com",
    url="https://github/ContentSide/lingx",
    packages=find_packages(exclude="tests"),  # same as name
    license="MIT",
    install_requires=required,
    include_package_data=True,
    python_requires=">=3.6"
)