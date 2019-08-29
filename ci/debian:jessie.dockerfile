
FROM debian:jessie
SHELL ["/bin/bash", "-c"]
ARG http_proxy
ARG https_proxy

RUN apt-get update && apt-get install -y --no-install-recommends \
# Pyenv requirements
    build-essential \
    python-dev \
    python-pip \
    python3-dev \
    python3-pip \
# Other requirements
    libavcodec-dev \ 
    libswscale-dev \ 
    libffi-dev \
    libjpeg62-turbo-dev

RUN useradd -m python_user

WORKDIR /home/python_user
USER python_user

ENV HOME  /home/python_user
ENV PATH $HOME/.local/bin/:$PATH

# Optionally install pathlib2 if Python3 <= 3.5
RUN (python3 -c "import sys; sys.exit(sys.version_info <= (3, 5, 0))" || pip3 install --user pathlib2) \
    && pip3 install --user "tox==3.4.0" 

COPY --chown=python_user:python_user . $HOME/build
WORKDIR $HOME/build
ENTRYPOINT ["tox"]
