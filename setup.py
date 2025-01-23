from setuptools import find_packages, setup

setup(
    name="make-flask",
    version="1.0.0",
    author="Lord J. Hackwell",
    author_email="lordhck@niton.dev",
    description="a cli tool for creating flask apps",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/nitondev/make-flask",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "make-flask=make_flask.cli:main",
        ],
    },
)
