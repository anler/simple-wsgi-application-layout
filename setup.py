from setuptools import setup, find_packages
"""
Docs
"""

setup(
    # Basic package data
    name='simplewsgi',
    version='0.1',
    author='ikame',
    author_email='anler86@gmail.com',
    long_description=__doc__,
    # Package structure
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'werkzeug==2.2.3',
        'jinja2==2.11.3'
    ]
)