from setuptools import setup, find_packages

setup(
    name="zentri-ai",
    version="0.1.0",
    description="Open-source framework for building community-driven code analysis agents.",
    author="Zentri AI Community",
    author_email="contact@zentri.ai",
    url="https://github.com/zentri-ai/zentri-ai",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "radon==5.1.0",
        "flake8==6.0.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
