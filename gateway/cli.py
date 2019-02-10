import argparse

from datetime import datetime

from .course_puller import pull_courses


def parse_args():
    parser = argparse.ArgumentParser(description="Gateway to Edxgator - syncing cleaned courses")
    subparsers = parser.add_subparsers(
        help="Downloads all edx courses again and compiles them", required=True, dest="command")
    sync_edx_command = subparsers.add_parser('sync_edx', help="Syncs all Edx courses right now")
    sync_edx_command.set_defaults(handler=sync_edx)
    namespace = parser.parse_args()
    return namespace


def sync_edx(*args, **kwargs):
    start_time = datetime.now()
    print("Starting sync operation at {}".format(start_time))
    pull_courses()
    end_time = datetime.now()
    print("Sync operation completed at {} with total time: {}".format(end_time, end_time - start_time))


def main():
    args = parse_args()
    args.handler(args)
