from setuptools import setup, find_packages
import codecs

with codecs.open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='curaset',
    version='0.1.0',
    description='A data-centric AI tool for label noise detection and uncertainty scoring',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Rayyan Ridwan',
    author_email='rayyan.ridw@gmail.com',
    url='https://github.com/rayyan-ridwan/CuraSet',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    install_requires=[
        'numpy',
        'scikit-learn',
    ],
    extras_require={
        'preview': [
            'pandas',
            'pillow',
            'matplotlib',
            'torch>=1.13,<2.1',
            'torchvision>=0.14,<0.16',
        ],
    },
    entry_points={
        'console_scripts': [
            'curaset=curaset.cli:main',
        ],
    },
    include_package_data=True,
    python_requires='>=3.7',
)
