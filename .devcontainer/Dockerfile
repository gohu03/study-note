FROM mcr.microsoft.com/devcontainers/base:bullseye

ARG NODE_VERSION=v22.11.0
ARG GOLANG_VERSION=1.23.3
ARG DART_SASS_VERSION=1.81.0
ARG HUGO_VERSION=0.139.3
ARG PYTHON_VERSION=3.12.8
RUN mkdir /usr/local/share/node \
  && curl -L https://nodejs.org/dist/${NODE_VERSION}/node-${NODE_VERSION}-linux-x64.tar.xz | tar -C /usr/local/share/node -xJ --strip-components=1\
  && curl -L https://go.dev/dl/go${GOLANG_VERSION}.linux-amd64.tar.gz | tar -C /usr/local/share/ -xz \
  && ln -s /usr/local/share/go/bin/go /usr/local/bin \
  && ln -s /usr/local/share/go/bin/gofmt /usr/local/bin \
  && curl -L https://github.com/sass/dart-sass/releases/download/${DART_SASS_VERSION}/dart-sass-${DART_SASS_VERSION}-linux-x64.tar.gz | tar -C /usr/local/share/ -xz \
  && ln -s /usr/local/share/dart-sass/sass /usr/local/bin/ \
  && mkdir /usr/local/share/hugo \
  && curl -L https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.tar.gz | tar -C /usr/local/share/hugo -xz \
  && ln -s /usr/local/share/hugo/hugo /usr/local/bin/ \
  && hugo completion bash > /etc/bash_completion.d/hugo \
  && apt-get update && apt-get install -y python3 python3-pip && apt-get clean

ENV PATH="/usr/local/share/node/bin/:$PATH"
EXPOSE 1313