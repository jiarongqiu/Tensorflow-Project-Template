import argparse
import os
import shutil
import importlib


def get_args():
    argparser = argparse.ArgumentParser(description=__doc__)
    argparser.add_argument(
        '-c', '--config',
        metavar='C',
        default='None',
        type=str,
        help='The Configuration file')
    argparser.add_argument(
        '-m', '--model',
        metavar='C',
        default='None',
        type=str,
        help='The Model file')
    argparser.add_argument(
        '-d', '--dataset',
        metavar='C',
        default='None',
        type=str,
        help='The Dataset file')
    argparser.add_argument(
        '-it', '--is_training',
        action='store_true', default=False,
        help='Is training')
    args = argparser.parse_args()
    return args


def import_module(path):
    return importlib.import_module(path)


def rm_dir(path):
    try:
        if os.path.exists(path):
            shutil.rmtree(path)
        return 0
    except Exception as err:
        print("Removing directories error: {0}".format(err))
        exit(-1)


def create_dir(path):
    """
    dirs - a list of directories to create if these directories are not found
    :param dirs:
    :return exit_code: 0:success -1:failed
    """
    try:
        if not os.path.exists(path):
            os.makedirs(path)
        assert os.path.exists(path)
        return 0
    except Exception as err:
        print("Creating directories error: {0}".format(err))
        exit(-1)


def rm_and_create_dir(path):
    rm_dir(path)
    create_dir(path)
