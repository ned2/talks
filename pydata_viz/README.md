# Doing Data Viz in Python

This is a Jupyter Notebook that takes you on a guided tour of Python data
visualisation tools. By the end of the Notebook you will have a sense of the
options you have available, their strengths, limitations, and thus be able to
make a more informed decision about which tools might be appropriate for your
intended context of use.


## Dependencies

This notebook makes use of a number of different data visualisation libraries,
and therefore required a number of different dependencies to be installed.

You will need python 3.6+, and it is recommended to firstly create and activate
a fresh virtual environment before installing the Python dependencies:

    pip install -r requirements.txt

If you are using Jupyter Lab (which is recommended!) you will need to install
the following JupyterLab extensions. You will need a working Node.js
installation for this, which isn't documented here as this will vary depending
on your OS.


    jupyter labextension install jupyterlab-plotly@4.14.3
    jupyter labextension install @jupyter-widgets/jupyterlab-manager plotlywidget@4.14.3
    
