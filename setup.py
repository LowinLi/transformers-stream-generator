import setuptools
from os import path
import subprocess

here = path.abspath(path.dirname(__file__))
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="transformers-stream-generator",
    version="0.0.5",
    license="MIT License",
    author="LowinLi",
    author_email="lowinli@outlook.com",
    description="This is a text generation method which returns a generator, streaming out each token in real-time during inference, based on Huggingface/Transformers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LowinLi/transformers-stream-generator",
    project_urls={
        "Repo": "https://github.com/LowinLi/transformers-stream-generator",
        "Bug Tracker": "https://github.com/LowinLi/transformers-stream-generator/issues",
    },
    keywords=[
        "GPT",
        "stream",
        "transformers",
        "NLP",
        "model hub",
        "transformer",
        "text generation",
        "summarization",
        "translation",
        "q&a",
        "qg",
        "machine learning",
        "CausalLM",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=[
        "transformers>=4.26.1",
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
