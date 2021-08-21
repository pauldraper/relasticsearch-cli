import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--body", help="Request body")
parser.add_argument("--aws-auth", default=False, type=bool)
parser.add_argument("--aws-domain", help="AWS domain")
parser.add_argument("--endpoint", help="Endpoint URL, without the path")
parser.add_argument("--username", help="Username for basic auth")
parser.add_argument(
    "method",
    choices=["DELETE", "GET", "HEAD", "PATCH", "POST", "PUT"],
    help="HTTP method",
)
parser.add_argument("path")
args = parser.parse_args()

from .request import request_main

request_main(args)
