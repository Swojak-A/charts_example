FROM python:3.8-slim

# set MODE for pip requirements ('prod'|'stage'|'') defult: '' (installs dev requirements)
ARG MODE

# tell python not to buffer stdout
ENV PYTHONUNBUFFERED=1

# os dependencies
RUN apt-get update -y && \
    apt-get -y install --no-install-recommends build-essential \
        postgresql-client \
        netcat \
        binutils \
        libjpeg-dev \
        libpq-dev \
        zlib1g-dev

# user
RUN groupadd -r user --gid=998 && \
    useradd -r -g user -d /user/ --uid=998 -s /sbin/nologin -c "Docker image user" user

# copy scripts
COPY --chown=user:user scripts /user/scripts
RUN chmod ug+x /user/scripts/*

# install requirements
COPY --chown=user:user requirements /user/requirements
RUN /user/scripts/install-requirements.sh $MODE user

# copy code
COPY --chown=user:user app /user/app

USER user

WORKDIR /user/app
