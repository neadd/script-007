import os
import sys
import argparse
import configparser
import utils.genfilename as genfilename
import fileops.fileops as fops


try:
    config=configparser.ConfigParser()
    config.read('config.ini')
    NAME_LEN=int(config['MAIN']['MAX_NAMELEN'])
    DEF_STORAGE=config['MAIN']['STORAGE']
except (configparser.Error,TypeError,ValueError):
    print("Config file error: "+sys.exc_info()[1].args[0])
    exit()


def cmd_args_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f', '--folder', default=DEF_STORAGE,
        help='working directory')
    parser.add_argument(
        '-n','--name',default=genfilename.genfilename(NAME_LEN),help='file name')
    parser.add_argument(
        '-c','--cmd',default=fops.getactionslist()[0],
        choices=fops.getactionslist(),help='command to execute')
    return parser
