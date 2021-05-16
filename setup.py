import setuptools

with open("README.md") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sislcrmsystem",
    version="0.0.2",
    author="Ramkumar",
    author_email="jd.ramkumar@gmail.com",
    description="Professional Python Development",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iomegak12/professionalpython",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Licese :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
    install_requires=[
        "requests",
        "json",
        "injector",
        "prettytable",
        "flask"
    ],
)
