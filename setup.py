from setuptools import setup

setup(
    name="weighted_collection",
    packages={"weighted_collection"},
    version="1.0",
    license="MIT",
    description="A WeightedCollection assigns probability weights per elements and returns elements randomly using those weights.",
    author="Seth Alter",
    author_email="subalterngames@gmail.com",
    url="TODO", # TODO
    download_url="TODO", # TODO
    keywords=["collection", "random"],
    install_requires=["numpy"],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
)