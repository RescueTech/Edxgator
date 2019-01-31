import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Gateway to Edxgator - syncing cleaned courses")
    subparsers = parser.add_subparsers(
        help="Downloads all edx courses again and compiles them", required=True, dest="command")
    sync_edx_command = subparsers.add_parser('sync_edx', help="Syncs all Edx courses right now")
    sync_edx_command.set_defaults(handler=sync_edx)
    namespace = parser.parse_args()
    return namespace


def sync_edx(*args, **kwargs):
    print(args)
    print(kwargs)
    print("We're syncing edx right now...")


def main():
    args = parse_args()
    args.handler(args)
