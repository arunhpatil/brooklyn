# User guide

## Parameters

To view command-line parameters type `brooklyn_plot -h`:
```
usage: brooklyn_plot [options]

Brooklyn (Gene co-expression and transcriptional bursting pattern recognition tool in single cell/nucleus RNA-sequencing data)

optional arguments:
  -h, --help  show this help message and exit
  --version   show program's version number and exit

Options:

  -h5,   --h5ad               input file in .h5ad format (accepts .h5ad)
  -ba,   --biomart            the reference gene annotations (in .csv format)
  -od,   --outDir             the directory of the outputs (Default: brooklyn-date-hh-mm-ss)
  -of,   --outFile            the name of summarized brooklyn file as CSV file and a brooklyn plot in PDF (Default: brooklyn)
  -ql,   --query              the list of genes to be queried upon (one gene per line and in .csv format)
  -sl,   --subject            the list of genes to be compared with (one gene per line and in .csv format)
  -cm,   --corMethod          the statistical approach for correlation measures (options: [pr, kt, bc] for pearsonr, kendalltau and bayesian correlation respectively. Default: pr)
  -cpu,  --threads            the number of processors to use for trimming, qc, and alignment (Default: 1)
  
```

## CLI - Example usage 

Example command usage:
```
brooklyn_plot -hd <input h5ad file> -ba <biomart_annotations.csv> -od <output_brooklyn> -of <brooklyn_plt>  -ql <queryGeneList.csv> -sl <GeneSearchSpace.csv> -cpu 12  
example: brooklyn_plot -h5 subset_AD_AT8_C3_Excit_EX-1-2-7.h5ad -ba AD_Exci_biomart_AT8_Ex-1-2-7.csv -of brooklyn_pkg -ql genelist_AT8_Ex-1-2-7_head.csv -sl againstlist_AT8_Ex-1-2-7_head.csv -cpu 10
```
Output command line:
```
Entering parallel mode with 10 CPU's.

With chunk size of 1, 9 chunks are created


The brooklyn_arch execution is completed in -8.1604 second(s)


The summary is completed in 0.1124 second(s)


The path to ourput directory: test_brooklyn/brooklyn_2023-03-31_16-50-23

The analysis completed in 10.1727 second(s)

```

### Test 
The test case illustrates the usage of brooklyn_plot with the cardiac cells - dataset  

- NOTE: All test files are now moved from Source Forge to Google Drive. The folder can be accessed [here](https://drive.google.com/drive/folders/1BUTf9XpUwQ91u7vmaRu5dSIeS15-dOLT?usp=sharing). If you have issues with the access, please reachout to us and the files will be made available. 
<!---
- Download the required files from Source Forge, [DCM_data](https://sourceforge.net/projects/brooklyn/files/data/)
```
You can download to your working directory as shown below:
wget -O subset_seidman_TTN.h5ad "https://sourceforge.net/projects/brooklyn/files/data/subset_seidman_TTN.h5ad/download"
wget -O genelist.csv "https://sourceforge.net/projects/brooklyn/files/data/genelist.csv/download"
wget -O againstlist.csv "https://sourceforge.net/projects/brooklyn/files/data/againstlist.csv/download"
wget -O seidmanttn_var_biomart.csv "https://sourceforge.net/projects/brooklyn/files/data/seidmanttn_var_biomart.csv/download"
```
-->
- Run basic brooklyn_plot command: 
```
brooklyn_plot -h5 subset_seidman_TTN.h5ad  -ba seidmanttn_var_biomart.csv -od results_ttn -ql genelist.csv -sl againstlist.csv -cpu 10

Entering parallel mode with 10 CPU's.

With chunk size of 35, 10 chunks are created


The brooklyn_arch execution is completed in -7923.1266 second(s)


The summary is completed in 4.2357 second(s)


The path to ourput directory: results_ttn/brooklyn_2023-04-05_14-25-57

The analysis completed in 7932.9977 second(s)
```
<!---
- The output folder generated here is uploaded as zip file, you can download the same from [here](https://sourceforge.net/projects/brooklyn/files/data/results_ttn.zip/download).
--->
## How to build required input files, such as gene list, h5ad and biomart annotations? 
The .h5ad file can be obtained from a singel cell or single nuclei RNA sequencing datasets for example, [cellxgene-collections](https://cellxgene.cziscience.com/collections). The users are recommended to select a single cell type corresponding to diagnosis/disease/normal state of interest. A detailed example of how we selected cell types from `DCM/ACM heart cell atlas: Cardiomyocytes` and other annotations such as biomart, gene lists are described here [Tutorial-notebook---TTN](https://brooklyn-plot.readthedocs.io/en/latest/notebooks/example_TTN_CV_DCM.html#Tutorial-notebook---TTN).

## Need assistance/have issues: 
Please report any issues/concerns/suggestions [here](https://github.com/arunhpatil/brooklyn/issues). Click create new issue and in Title: “Please describe the error you think is obvious and will be general for the scientific community to recognize”, and Comment: “Give us the maximum information possible regarding the error that you can see on the standard output/terminal”.

## Resources 
The h5ad AnnData was downloaded from [cellxgene](https://cellxgene.cziscience.com/collections/e75342a8-0f3b-4ec5-8ee1-245a23e0f7cb), [Reichart et al. (2022) Science](https://www.science.org/doi/10.1126/science.abo1984)
