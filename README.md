# RElasticsearch CLI

Elasticsearch CLI client

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Overview](#overview)
- [Install](#install)
- [Usage](#usage)
- [Example](#example)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Overview

This is a thin CLI wrapper around the ES API. Supports AWS IAM authentication.

## Install

```sh
pip3 install relasticsearch-cli
```

To install with AWS IAM support,

```sh
pip3 install relasticsearch-cli[aws]
```

## Usage

```txt
usage: es [-h] [--body BODY] [--aws-auth AWS_AUTH]
          [--aws-domain AWS_DOMAIN] [--endpoint ENDPOINT]
          [--username USERNAME]
          {DELETE,GET,HEAD,PATCH,POST,PUT} path

positional arguments:
  {DELETE,GET,HEAD,PATCH,POST,PUT}
                        HTTP method
  path

optional arguments:
  -h, --help            show this help message and exit
  --body BODY           Request body
  --aws-auth AWS_AUTH
  --aws-domain AWS_DOMAIN
                        AWS domain
  --endpoint ENDPOINT   Endpoint URL, without the path
  --username USERNAME   Username for basic auth
```

## Example

List indices:

```sh
es --endpoint http://localhost:9200 GET /_cat/indices
```

```txt
green open .kibana_1        XTv6AdigRqWMafUfInRsTg 1 1
```

List indices for AWS Elasticsearch:

```sh
es --aws-domain example GET /_cat/indices
```
