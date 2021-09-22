import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BMI500HW4",
    version="0.0.3",
    author="Chenbin Huang",
    author_email="chenbin.huang@@emory.edu",
    description="BMI 500 HW4 Clustering Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/soyhcb/BMI500_HW4_Packaging",
    project_urls={
        "Bug Tracker": "https://github.com/soyhcb/BMI500_HW4_Packaging/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
          'scikit-learn',
          'matplotlib'
      ]
)