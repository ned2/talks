# Doing Data Viz in Python

This is a Jupyter Notebook that takes you on a guided tour of some of the key 
visualisation tools available in the Python data ecosystem. By the end of the 
Notebook you will have a sense of the options you have available, their 
strengths, limitations, and thus be able to make a more informed decision about 
which tools might be appropriate for your intended context of use. It will also 
cover some useful tips and tricks when working with these libtaries and general 
suggestions for how to think about doing data visualisation more generally.


## Getting the Data

The notebook makes use of some data from the Melbourne City Council [Pedestrian
Counting System
dataset](https://data.melbourne.vic.gov.au/Transport/Pedestrian-Counting-System-2009-to-Present-counts-/b2ak-trbp).

You can download it using a script that comes with the notebook: 

    ./get-data.sh


## Running with Docker

This notebook makes use of a number of different data visualisation libraries,
and therefore requires a number of different dependencies to be installed. The
simplest way to get it running is to use the supplied `Dockerfile`.

1. [Install Docker](https://docs.docker.com/get-docker)

2. Change to the `pydata_viz` directory.

3. Build the Docker image:

    docker build -t pydata-viz .

4. Run the image, mounting 

    docker run -it -v ${PWD}:/home/jovyan/pydata_viz -p 8888:8888 pydata-viz


## Installing Locally:

Dependencies:

* Python 3.6+
* Node.js
* npm

There are also some specific dependencies required for Cartopy. The following
will hopefully do the trick for Ubuntu/Debian:

    sudo apt-get install npm nodejs wget

    # Cartopy dependencies
    sudo apt-get install build-essential libgeos-dev libproj-dev proj-data proj-bin


Then create and activate a fresh virtual environment before installing the
Python dependencies:

    pip install -r requirements.txt

If you are using Jupyter Lab (which is recommended!) you will need to install
the following JupyterLab extensions. You will need node.js and npm installed for
this.

    jupyter labextension install jupyterlab-plotly@4.14.3
    jupyter labextension install @jupyter-widgets/jupyterlab-manager plotlywidget@4.14.3
