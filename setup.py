import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rssreader", # Replace with your own username
    version="1.0.0",
    author="Robbe Van Herck",
    author_email="robbe@robbevanherck.be",
    description="A simple RSS aggregator and API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Robbe7730/RSSReader",
    packages=['rssreader'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    package_data={'rssreader': ['templates/*', 'static/*']},
)
