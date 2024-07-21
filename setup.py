from setuptools import setup, find_packages

setup(
    name='trellis-python',  # Name of your package
    version='0.1.2',  # Version of your package
    packages=find_packages(),  # Automatically find packages in the directory
    author="Trellis Team",  # Author of your package
    author_email="founders@runtrellis.com",
    install_requires=["httpx"]
)
