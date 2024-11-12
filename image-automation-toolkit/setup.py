from setuptools import setup, find_packages

setup(
    name="image-automation-toolkit",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "Pillow>=9.0.0",
        "img2pdf>=0.4.0",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A toolkit for automated image processing and PDF generation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/image-automation-toolkit",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)