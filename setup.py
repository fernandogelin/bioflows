from setuptools import setup

setup(
    name='bioflows',
    version='0.99',
    packages=['tests', 'tests.test_catalog', 'tests.test_wrappers', 'tests.test_rnaseq_workflow', 'bioutils',
              'bioutils.access_sra', 'bioutils.parse_fastqc', 'bioflowutils', 'definedworkflows',
              'definedworkflows.rnaseq'],
    #install_requires= [luigi, saga-python, lxml, biopython, jsonpickle, pyyaml],
    url='',
    license='GPLv2',
    author='Ashok Ragavendran',
    author_email='ashok_ragavendran@brown.edu',
    description='',
    entry_points={
        'console_scripts': ['bioflow-rnaseq = definedworkflows.rnaseq.rnaseqworkflow:main'],
    }
)