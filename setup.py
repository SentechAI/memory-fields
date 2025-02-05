from setuptools import setup, find_packages

setup(
    name="memory-fields",
    version="0.1.0",
    author="Sentech AI",
    author_email="service@sentech.ai",
    description="A Python client for interacting with SenTech AI's memory fields API.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SentechAI/memory-fields",
    packages=find_packages(),
    install_requires=[
        "requests",
        "requests_toolbelt"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
