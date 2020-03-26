import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()




setuptools.setup(
    name="dirtree2json-t6580",
    version="0.0.1",
    author="Tim Pogue",
    author_email="t.pogue.python@gmail.com",
    description="converts directory tree including files to JSON object",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Accoustium/dirtree2json",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)