import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

with open('requirements', 'r') as fh:
    required = fh.read().splitlines()

setuptools.setup(
    name="drishtypy",  # Replace with your own username
    version="0.0.6.18",
    author="Abhinav Rana",
    author_email="rabhinavcs@gmail.com",
    description="Small package to increase modularity for TSAI: EVA",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Abhinavl3v3l/Drishtypy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=required,
)