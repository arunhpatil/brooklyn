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
The test case illustrates the usage of miRge3.0 with a sample dataset, mapping to human reference libraries. 

- Download the sample file from Source Forge, [SRR772403](https://sourceforge.net/projects/mirge3/files/test/SRR772403.fastq.gz/download)
```
You can download to your working directory as shown below:
wget -O SRR772403.fastq.gz "https://sourceforge.net/projects/mirge3/files/test/SRR772403.fastq.gz/download"
```
- Run basic miRge3.0 command to annotate and report isomiRs
```
miRge3.0 -s SRR772403.fastq.gz -lib /mnt/d/Halushka_lab/Arun/miRge3_Lib -a illumina -on human -db mirbase -o output_dir -gff -cpu 8

bowtie version: 1.3.0
cutadapt version: 3.1
Samtools version: 1.11
Collecting and validating input files...

miRge3.0 will process 1 out of 1 input file(s).

Cutadapt finished for file SRR772403 in 3.4343 second(s)
Collapsing finished for file SRR772403 in 0.0216 second(s)

Matrix creation finished in 0.0263 second(s)

Data pre-processing completed in 3.5111 second(s)

Alignment in progress ...
Alignment completed in 8.1488 second(s)

Summarizing and tabulating results...
Summary completed in 2.27 second(s)


The analysis completed in 15.2276 second(s)
```
- Output folder, sample output can be accessed [here](https://sourceforge.net/projects/mirge3/files/test/output_dir/)
```
miRge creates a subfolder inside the folder "output_dir" and all the files will be stored there. The test output can be accessed at the following link:
https://sourceforge.net/projects/mirge3/files/test/output_dir/miRge.2021-06-25_15-16-58/
```

## Resources 
