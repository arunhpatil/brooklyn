# Installation

## Welcome to installation protocol of Brooklyn 

#### Requirements for brooklyn\_plot package are python3.8 and R (ggplot2)
This installation protocol is based on Ubuntu, please use the commands that suit your Linux distribution. For example, `apt` should be replaced with `yum` in Fedora/CentOS. 
- Search and start the terminal
- Follow the commands to update Ubuntu and install python 3.8<br/>
A password will be prompted when you type `sudo`, use the one you have set during Ubuntu (or your distro) installation.<br/>
```
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.8
sudo apt install python3-setuptools
sudo apt install python3-pip
sudo apt install r-base
```
- Please seek IT administrators help if you have difficulty in installing Python and R 
  
#### Installing brooklyn\_plot with conda 

```
conda install -c bioconda brooklyn_plot
```

If you want to use your own environment, please follow the instruction [here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands).

##### Updating brooklyn\_plot with conda
```
conda update brooklyn_plot 
```

#### Installing brooklyn\_plot with PyPi

##### Install brooklyn\_plot by this simple command
```
python3.8 -m pip install --user brooklyn_plot 
```

##### To upgrade brooklyn\_plot 
```
python3.8 -m pip install --user --upgrade brooklyn_plot 
```
