import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="the-calculator-pkg",
    version="0.1",
    author="Funmi Somoye",
    description="A simple sophisticated calculator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    #url="https://github.com/linda-oranya/pypi_calculator",
    #project_urls={
        #"Bug Tracker": "https://github.com/linda-oranya/pypi_calculator/issues",
    #},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    py_modules=["calculator"],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)