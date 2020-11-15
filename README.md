# Docker Examples :whale:
This is a repository of simple Docker examples and manage their deployment with Docker Compose. These samples use in local development environments such as project setups and learning, must not be deployed in production environments.

## Examples

### Python
| Name | Description |
| --- | --- |
| [jupyter](jupyter/README.md) | Jupyter notebook allows you create live code python scripts, statistical model, data visualization |

## Getting started

### Prerequisites

- Make sure that you have Docker and Docker Compose installed
- Download some or all of the samples from this repository.

### Running a sample

The root directory of each sample contains the `docker-compose.yaml` which
describes the configuration of service components. All samples can be run by executing:

```console
docker-compose up -d
```

Check the `README.md` of each sample to get more details on the structure.
To stop and remove all containers of the sample application run:

```console
docker-compose down
```