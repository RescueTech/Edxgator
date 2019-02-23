import argparse
import uvicorn

from .app import app


def run_server(*args, **kwargs):
    uvicorn.run(app, host='localhost', port=8000)


def parse_args():
    parser = argparse.ArgumentParser(description="Edxgator UI")
    subparsers = parser.add_subparsers(
        help="UI - commands", required=True, dest="command")
    sync_edx_command = subparsers.add_parser('runserver', help="Runs Edxgator server")
    sync_edx_command.set_defaults(handler=run_server)
    namespace = parser.parse_args()
    return namespace


def main():
    args = parse_args()
    args.handler(args)
