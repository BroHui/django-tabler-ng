from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django-tabler-ng',
    setup_requires=['setuptools_scm'],
    use_scm_version={'version_scheme': 'post-release'},
    description='Django wit Tabler template',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/BroHui/django-tabler-ng',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=['django', 'tabler', 'dashboard', 'template', 'ui'],
    author='BroHui',
    author_email='hui.dev@outlook.com',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
