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
        'werkzeug==0.6.2',
        'jinja2==2.5.5'
    ]
)