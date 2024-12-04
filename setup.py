from setuptools import setup, find_packages

setup(
    name='my_project',
    version='0.1.0',
    description='A simple Python project',
    author='Your Name',
    author_email='your_email@example.com',
    url='https://github.com/your_username/my_project',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
    ],
)
