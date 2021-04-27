"""Module for request preparation based on config and command line params"""
import os
import sys
import argparse
import utils.genfilename as genfilename
import fileops.fileops as fops
import utils.getconfig as cfg


def requestparams():
    """compile request params"""
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        '-f', '--folder',
        default = cfg.getdefstorage(),
        help    = 'working directory')
    
    parser.add_argument(
        '-n','--name',
        default = genfilename.genfilename(cfg.getmaxnamelen()),
        help    = 'file name')
    
    parser.add_argument(
        '-c','--cmd',
        required = True,
        choices  = fops.getactions(),
        help     = 'command to execute')
    
    parser.add_argument(
        '-d','--data',
        default = '',
        help    = 'Data')
    
    params = parser.parse_args()
    return params
