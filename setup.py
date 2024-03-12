from setuptools import setup

setup(
    # Package metadata
    name='qiymeti-az',
    version='0.1.0',
    description='A Python package for scraping product prices from various Azerbaijani websites.',
    long_description='A Python package for scraping product prices from various Azerbaijani websites (Kontakt Home, Baku Electronics, Music Gallery, World Telecom, ByTelecom, Irshad).',
    author='Ziya Mammadov',
    author_email='ziyamm08@gmail.com',
    license='MIT',

    # Dependencies
    install_requires=[
        'requests>=2.26.0',
        'beautifulsoup4>=4.10.0',
        'fuzzywuzzy>=0.18.0'
    ],

    # Additional metadata
    url='https://github.com/zmmmdf/qiymeti_az',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
