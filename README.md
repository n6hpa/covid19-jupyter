# covid19-jupyter
Notebooks for viewing COVID-19 data


https://towardsdatascience.com/jupyter-data-science-stack-docker-in-under-15-minutes-19d8f822bd45

# To run the docker container:

`cd covid19-jupyter`
`git submodule init`
`git submodule update`
`docker-compose up`

# Setting up a virtual environment on Ubuntu
Not needed if just running the docker image + Jupyter

Only needed if developing on Ubuntu without the docker image

`sudo apt install python3-venv`
`python3 -m venv .venv`
`source .venv/bin/activate`
`pip install -r requirements.txt`