from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
        # e.g., "requests>=2.25.1",
    ],
    author="shivako",
    author_email="example@example.com",
    description="A sample Python project",
    keywords="sample, python, project",
    python_requires=">=3.6",
)
