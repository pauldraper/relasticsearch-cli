import json
import os
import sys

import requests
import urllib3


def request_main(args):
    password = os.environ.get("ES_PASSWORD")

    if args.endpoint is not None:
        endpoint = args.endpoint
    elif args.aws_domain is not None:
        import boto3

        es_client = boto3.client("es")
        args.aws_auth = True
        response = es_client.describe_elasticsearch_domain(DomainName=args.domain)
        endpoint = f"https://{response['DomainStatus']['Endpoint']}"
    else:
        print("Missing endpoint", file=sys.stderr)
        sys.exit(1)

    if args.aws_auth:
        import boto3
        import requests_aws4auth

        session = boto3.Session()
        credentials = session.get_credentials()
        if credentials is None:
            print("Missing AWS credentials", file=sys.stderr)
            sys.exit(1)

        auth = requests_aws4auth.AWS4Auth(
            credentials.access_key,
            credentials.secret_key,
            session.region_name,
            "es",
            session_token=credentials.token,
        )
    elif args.username is not None:
        if password is None:
            print("Missing password", file=sys.stderr)
        auth = requests.HTTPBasicAuth(args.username, password)
    else:
        auth = None

    headers = {}
    if args.body is not None:
        headers["Content-Type"] = "application/json"
        body = args.body
    else:
        body = None

    adapter = requests.adapters.HTTPAdapter()
    session = requests.Session()
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    try:
        response = session.request(
            args.method,
            f"{endpoint}{args.path}",
            auth=auth,
            data=body,
            headers=headers,
        )
        response.raise_for_status()
    except requests.ConnectionError as e:
        e = e.args[0].reason
        print(str(e), file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)

    if response.headers["Content-Type"].startswith("application/json"):
        print(json.dump(response.json(), sys.stdout, indent=4, sort_keys=True))
    else:
        print(response.text)
