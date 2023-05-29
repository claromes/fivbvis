from setuptools import setup, find_packages
import re

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt', 'r', encoding='utf-8') as f:
    install_requires = f.read().splitlines()

with open('fivbvis/version.py', 'r', encoding='utf-8') as f:
    version = re.search(r"^__version__\s*=\s*'(.*)'.*$",
        f.read(), flags=re.MULTILINE).group(1)

setup(
    name='fivbvis',
    version=version,
    author='claromes',
    description='FIVB VIS Web Service Python Client',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='api-wrapper fivbvis fivb volleyball beachvolleyball',
    url='https://github.com/claromes/fivbvis',
    project_urls={
        'Documentation': 'https://claromes.github.io/fivbvis/',
        'Issue Tracker': 'https://github.com/claromes/fivbvis/issues',
    },
    packages=find_packages(exclude=['docs', 'tests*']),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ],
    python_requires='>=3.8',
    install_requires=install_requires
)