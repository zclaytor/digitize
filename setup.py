import setuptools


setuptools.setup(
    name="digitize",
    version=1.0,
    author="Zachary R. Claytor",
    author_email="zclaytor@ufl.edu",
    description="Brute-forcing a solution to the NYT Digits puzzle",
    url="https://github.com/zclaytor/digitize",
    license="MIT",
    python_requires='>=3',
    install_requires=['numpy'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
