#!/usr/bin/env python3

import subprocess
import os
import sys


PLATFORMS = [
    'ubuntu:trusty', 'ubuntu:xenial', 'ubuntu:bionic', 'debian:jessie',
    'debian:stretch', "debian:buster"
]

TEMPLATE = """
FROM {dist}
SHELL ["/bin/bash", "-c"]
ARG http_proxy
ARG https_proxy

RUN apt-get update && apt-get install -y --no-install-recommends \\
# Pyenv requirements
    build-essential \\
    python-dev \\
    python-pip \\
    python3-dev \\
    python3-pip \\
# Other requirements
    libavcodec-dev \\ 
    libswscale-dev \\ 
    libffi-dev \\
    {dist_dependencies}

RUN useradd -m python_user

WORKDIR /home/python_user
USER python_user

ENV HOME  /home/python_user
ENV PATH $HOME/.local/bin/:$PATH

# Optionally install pathlib2 if Python3 <= 3.5
RUN (python3 -c "import sys; sys.exit(sys.version_info <= (3, 5, 0))" || pip3 install --user pathlib2) \\
    && pip3 install --user "tox==3.4.0" 

COPY --chown=python_user:python_user . $HOME/build
WORKDIR $HOME/build
ENTRYPOINT ["tox"]
"""

def template(dist, dependencies):
    return TEMPLATE.format(
        dist=dist,
        dist_dependencies=dependencies
    )

common_dependencies = ['libavcodec-dev', 'libswscale-dev', 'libffi-dev']

DEBIAN_DEPENDENCIES = 'libjpeg62-turbo-dev'
UBUNTU_DEPENDENCIES = 'libjpeg-turbo8-dev'

def dockerfile(dist, dependencies):
    with open(dist + '.dockerfile', 'w') as f:
        f.write(template(dist, dependencies))

def main():
    dockerfile('ubuntu:trusty', UBUNTU_DEPENDENCIES)   
    dockerfile('ubuntu:xenial', UBUNTU_DEPENDENCIES)
    dockerfile('ubuntu:bionic', UBUNTU_DEPENDENCIES)
    dockerfile('debian:jessie', DEBIAN_DEPENDENCIES)
    dockerfile('debian:stretch', DEBIAN_DEPENDENCIES)
    dockerfile('debian:buster', DEBIAN_DEPENDENCIES)
    
if __name__ == '__main__':
    main()
