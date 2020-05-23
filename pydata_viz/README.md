# Doing Data Viz in Python

This is a Jupyter Notebook that takes you on a guided tour of some of the key 
visualisation tools available in the Python data ecosystem. By the end of the 
Notebook you will have a sense of the options you have available, their 
strengths, limitations, and thus be able to make a more informed decision about 
which tools might be appropriate for your intended context of use. It will also 
cover some useful tips and tricks when working with these libtaries and general 
suggestions for how to think about doing data visualisation more generally.  

## Dependencies

This notebook makes use of a number of different data visualisation libraries,
and therefore requireds a number of different dependencies to be installed.

You will need python 3.6+, and it is recommended to firstly create and activate
a fresh virtual environment before installing the Python dependencies:

    pip install -r requirements.txt

If you are using Jupyer Lab (which is recommended!) you will need to install the
following JupyterLab extensions. You will need a working Node.js installation
for this, which isn't documented here as this will vary depending on your OS.


    jupyter labextension install jupyterlab-plotly@4.7.1
    jupyter labextension install @pyviz/jupyterlab_pyviz
    jupyter labextension install @jupyter-widgets/jupyterlab-manager
    jupyter labextension install @jupyterlab/vega5-extension
    
