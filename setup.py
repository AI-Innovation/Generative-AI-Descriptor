from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="generative-ai-descriptor",
    version="0.1.0",
    author="AI Innovators",
    author_email="contact@ai-innovators.com",
    description="A generative AI system for creating accessible descriptions of various media types",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AI-Innovators/Generative-AI-Descriptor",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy==1.21.2",
        "pandas==1.3.3",
        "requests==2.26.0",
        "beautifulsoup4==4.10.0",
        "lxml==4.6.3",
        "openai==0.27.0",
        "GPT-NeoXT-Chat-Base-20B==1.0.0",
        "Flask==2.0.1",
    ],
)
