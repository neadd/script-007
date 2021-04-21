import os
import argparse

def cmd_args_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f', '--folder', default=os.getcwd(),
        help='working directory (default: current app folder)')
    parser.add_argument(
        '-n','name',help='file name')
    parser.add_argument(
        '-c','--cmd',default='list',
        choices=['list','create','delete','read','meta'],help='command to execute')
    return parser
