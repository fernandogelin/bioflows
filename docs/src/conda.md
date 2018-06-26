### 1.1 Conda Package Management


CONDA is a system agnostic software package management system based on
the Anaconda python distribution to ensure that a software and all its
dependencies are bundled together. These conda packages can be
downloaded from various publicly available repositories called
*channels* and one such channel for bio-informatics tools is bioconda.

For ensuring reproducibily, we have established a publicly accessible
channel for all programs that are included with wrappers within the
bioflows tool accessible through the `compbiocore channel <https://anaconda.org/compbiocore/>`_. In this channel, we have provided conda packages of all software used including
the bioflows package itself. To download the packages or the bioflows tool use the command into your conda environment:

```bash
    conda install -c compbiocore /pkg_name/
```

More detailed instructions on how to install anaconda and use the conda environments can be found in the anaconda documentation for:

- [Installation](https://docs.anaconda.com/anaconda/install.html)

- [Getting started](https://docs.anaconda.com/anaconda/user-guide/getting-started.html)
