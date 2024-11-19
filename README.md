# RobustCodeStats

This repository contains the software for computing partition statistics introduced in our paper on "Statistical estimation of sparsity and efficiency for molecular codes", currently available as [a preprint on bioRxiv](https://www.biorxiv.org/content/10.1101/2024.08.13.607773v1).  This repository also contains the notebooks and scripts needed to reproduce all the figures and results in the paper.  

If you use our software, please cite:
> Fung, J. H., Carrière, M., & Blumberg, A. J. (2024). Statistical estimation of sparsity and efficiency for molecular codes. *bioRxiv*. doi:10.1101/2024.08.13.607773

## Installation

First, install `numpy` as it is a prerequisite for `RobustCodeStats`.

Then, clone this repository to your working directory:

    git clone https://github.com/jhfung/RobustCodeStats.git

Make sure the `RobustCodeStats` directory is in your Python module search path.  The module can then be imported using:

    import CodebookStats

## Basic usage

Here, we demonstrate how to use our software using test data from [Reilly et al. (2020)](https://doi.org/10.1038/s41586-020-2618-9), as described in our paper.

```
from CodebookStats import zeta, eta
import pandas as pd

# Download the test data directly from the publisher's website.
url = 'https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-020-2618-9/MediaObjects/41586_2020_2618_MOESM3_ESM.xlsx'

reilly2020 = pd.read_excel(
    url, 
    sheet_name='Binary Neuron Class', 
    index_col=[0,1]
).T.drop('None')

# Compute the partition cardinality
reilly2020_zetas = zeta(reilly2020)
reilly2020_mean_zeta = np.mean(reilly2020_zetas)

# Compute the partition entropy
reilly2020_etas = eta(reilly2020)
reilly2020_mean_eta = np.mean(reilly2020_etas)
```

For more ways to use `RobustCodeStats`, see the Jupyter notebooks included in this repository.

## Detailed documentation

The `CodebookStats` module provides two functions, `zeta` and `eta`, to calculate the partition cardinality and partition entropy respectively of a binary codebook.  The arguments to each function are the same:
- `X` : the input data matrix with codes as rows and code features as columns
- `k` : an integer (default: `10`) to specify the size of the subsampled feature sets
- `b` : an integer (default: `300`) to specify the number of bootstrap samples
- `random_state` : an integer or `RandomState` (default: `42`) to set the random seed for reproducibility.  

The return value of `zeta` and `eta` is a list of `b` floats that represent the value of the normalized cardinality or entropy respectively on each of the subsampled matrices.  

## Reproducibility

To reproduce the results and figures in our paper, we provide two Jupyter notebooks.  
- For the experiments concerning neuronal identity specification in *C. elegans*, see `worm_neuronal_identity.ipynb`.
- For the experiments concerning interpatient heterogeneity from somatic mutational profiles in cancer, see `cancer_mutations_heterogeneity.ipynb`.
