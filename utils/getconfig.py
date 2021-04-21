import os
import argparse
import utils.genfilename as genfilename
import fileops.fileops as fops
NAME_LEN=8

def cmd_args_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f', '--folder', default=os.getcwd(),
        help='working directory (default: current app folder)')
    parser.add_argument(
        '-n','name',default=genfilename(NAME_LEN),help='file name')
    parser.add_argument(
        '-c','--cmd',default=fops.actions.keys()[0],
        choices=fops.actions.keys(),help='command to execute')
    return parser
