import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="er-utils",
    version="0.0.1",
    author="Tommaso Teofili",
    author_email="tommaso.teofili@gmail.com",
    description="utilities for working with ER models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url= 'https://github.com/tteofili/er-utils.git',
    packages=['er-utils'],
    install_requires=[
          'pandas',
          'numpy',
          'scipy',
          'scikit-learn',
          'tqdm',
          'transformers',
          'torch',
          'tensorflow',
          'deepmatcher',
          'keras'
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: Apache Software License',
        "Operating System :: OS Independent",
        'Topic :: Scientific/Engineering :: Artificial Intelligence :: Data management',
    ],
    python_requires='>=3.6',
)
