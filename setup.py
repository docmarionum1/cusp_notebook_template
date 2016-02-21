from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '0.1'

install_requires = [
    "Paste",
    "PasteScript"
]


setup(name='cusp_notebook',
    version=version,
    description="Paster Template for CUSP iPython Notebooks",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='ipython notebook cusp paster',
    author='Jeremy Neiman',
    author_email='docmarionum1@gmail.com',
    url='jeremyneiman.com',
    license='WTFPL',
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    package_data= {'cusp_notebook': ['template/*']},
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points="""
    [paste.paster_create_template]
    cusp_notebook = cusp_notebook:CUSPNotebookTemplate
    """
)
