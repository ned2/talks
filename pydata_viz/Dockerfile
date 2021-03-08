FROM ubuntu:20.10

RUN apt-get update && apt-get install -y \
    build-essential \
    npm \
    nodejs \
    python3.9 \
    python3.9-dev \
    python3.9-venv \
    # Cartopy dependencies
    libgeos-dev \
    libproj-dev \
    proj-data \
    proj-bin

# create new user and switch to it
RUN useradd --create-home --shell /bin/bash jovyan
USER jovyan
WORKDIR /home/jovyan

# create and activate virtualenv
RUN python3.9 -m venv /home/jovyan/venv
ENV PATH="/home/jovyan/venv/bin:$PATH"

# install numpy first to workaround cartopy issue:
# https://github.com/SciTools/cartopy/issues/1584
RUN pip3.9 install -U pip wheel numpy

# install Python dependencies
COPY requirements.txt ./
RUN pip3.9 install --no-cache-dir -r requirements.txt

RUN jupyter labextension install jupyterlab-plotly@4.14.3
RUN jupyter labextension install @jupyter-widgets/jupyterlab-manager plotlywidget@4.14.3

EXPOSE 8888

ENTRYPOINT ["jupyter-lab", "--ip=0.0.0.0", "--allow-root", "--no-browser"]
