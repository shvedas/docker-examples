# JUPYTER
Application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more.
This container based on `jupyter/tensorflow-notebook` image.

### Quick Start:
```bin/bash
docker-compose up -d
docker exec jupyter jupyter notebook list
docker-compose down
```

### Access:
```bin/bash
http://127.0.0.1:8888/login
password: easy
```

> Note: if you want to change password:
>   - exec `password.py` file
>   - copy hash
>   - change `--NotebookApp.password=` in `docker-compose.yml` file

### Useful links:
  - [Jupyter Documentation](https://jupyter.org/documentation)
  - [Jupyter Docker Images](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html)
  - [Docker options](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/common.html)
  - [`tensorflow-notebook` image source](https://github.com/jupyter/docker-stacks/tree/master/tensorflow-notebook)
  - [`base-notebook` image source](https://github.com/jupyter/docker-stacks/tree/master/base-notebook)