## 1 Introduction


This document provides a guide to using the bioflows package for various
workflows to analyse NGS datasets. Currently, we have implemented one
standard RNA-seq workflow and a tutorial is included for analysis of
RNA-seq data using this package.

One primary objective of the Core is to enable reproducibility in
computational analysis of NGS data and critical to this objective is to
provide a consistent software environment across multiple platforms. The
achieve this goal we are using the following approaches:

- Container based approach using `docker <https://www.docker.com>`_ for managing the analysis environment

- `CONDA <https://conda.io/docs/>`_ package management system for managing software tools

- BioFlows workflow tool to ensure consistency in analysis steps and stages with interoperability

across multiple job submission systems
