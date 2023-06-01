#! /usr/bin/env python3
import argparse
import logging
import sys

import uvicorn
from main import app
from utils import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(sys.argv[0])


def serve(args):
    logger.info("Running server at {host}:{port}".format(host=settings.APP_HOST, port=settings.APP_PORT))
    uvicorn.run(app, host=settings.APP_HOST, port=settings.APP_PORT)


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    parser_server = subparsers.add_parser("serve", help="start the server")
    parser_server.add_argument("--config", help="path to configuration file")
    parser_server.set_defaults(func=serve)

    args = parser.parse_args()
    serve(args)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Exiting on KeyboardInterrupt")
    except Exception as exc:
        logger.info(f"Exiting on unknown error {exc}")
    finally:
        pass
