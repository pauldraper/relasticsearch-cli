# Elasticsearch CLI

Elasticsearch CLI client

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Usage](#usage)
- [Example](#example)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

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

es --endpoint http://localhost:9200 GET /\_cat/indices
