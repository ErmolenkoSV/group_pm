from setuptools import setup, find_packages

setup(
    name='parser',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pymupdf',
        'spacy',
        'python-docx',
        'langdetect',
        'beautifulsoup4',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'my_parser=parser.main:main',
        ],
    },
)
