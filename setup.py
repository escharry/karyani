# pip3 install setuptools twine wheel
# python3 setup.py sdist bdist_wheel
# twine upload dist/*


import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

with (HERE / "requirements.txt").open() as f:
    requirements = f.read().splitlines()

setup(
    name="karyani",
    version="0.1.0",
    description="python cli task manager",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/escharry/karyani",
    author="escharry",
    author_email="echarry@berkeley.edu",
    license="MIT",
    entry_points={
        'console_scripts': [
            'karyani = karyani.cli:main',
        ],
    },
    python_requires='>=3.6',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=["karyani"],
    include_package_data=True,
    install_requires=requirements,
)
