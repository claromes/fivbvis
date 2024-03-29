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
    author='Claromes',
    author_email='support@claromes.com',
    description='Python client for the Volleyball Information System (FIVB VIS)',
    license='GPLv3',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='fivbvis fivb volleyball beachvolleyball sports datasets analytics',
    url='https://github.com/claromes/fivbvis',
    project_urls={
        'Documentation': 'https://github.com/claromes/fivbvis/blob/main/docs/documentation.md',
        'Bug Tracker': 'https://github.com/claromes/fivbvis/issues',
        'Releases': 'https://github.com/claromes/fivbvis/releases',
    },
    packages=find_packages(exclude=['docs']),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.11',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ],
    python_requires='>=3.8',
    install_requires=install_requires
)