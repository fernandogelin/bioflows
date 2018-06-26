
### 2.1 Setup the Environment for bioflows

First make sure the conda environment is setup in your PATH
variable. In your CCV console type

```bash
    echo $PATH
```

and you should see `/gpfs/data/cbc/cbc_conda_v1/bin/` as the first
element in the list of paths in your output.


>    If  ``/gpfs/data/cbc/cbc_conda_v1/bin/`` is not the first element in the
      list then use the command

> ```bash
    export PATH=/gpfs/data/cbc/cbc_conda_v1/bin/:$PATH
```

>   This will add  `/gpfs/data/cbc/cbc_conda_v1/bin/` to the beginning of
    your `PATH` variable


For convenience we will use `/users/username` as the working directory and you should modify
accordingly.

These scripts should be run in a persistent terminal session and we will
use GNU screen to do that, so that the we can disconnnect from our ssh
sessions for long running jobs. To learn more on how to use screen use
the following link
[gnu screen tutorial] (https://www.linode.com/docs/networking/ssh/using-gnu-screen-to-manage-persistent-terminal-sessions)


Start a screen session naming it `test\_bioflows` as below

```bash
    screen -S test_bioflows
```
once you are in your screen session you set up your python environment
with the following commands

```bash
    source activate bflows
```
Now you are ready to run the predefined RNAseq workflow.
