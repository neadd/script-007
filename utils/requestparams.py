"""Module for request preparation based on config and command line params"""
import os
import sys
import argparse
import utils.genfilename as genfilename
import fileops.fileops as fops
import utils.getconfig as cfg
import utils.mylogger as log

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
        '-k','--keypath',
        default = None,
        help    = 'Asymmetric key path')
    
    parser.add_argument(
        '-d','--data',
        default = '',
        help    = 'Data')
    
    parser.add_argument(
        '-i','--infile',
        default = None,
        help    = 'Read data from file')
    
    parser.add_argument(
        '-w','--writeto',
        default = None,
        help    = 'write read data to file (rsa only)')
    
    params = parser.parse_args()
    if params.infile != None:
        try:
            with open(params.infile,"rb") as datafile:
                params.data=datafile.read()
        except OSError:
            log.raiserror(f"Read data file error: {sys.exc_info()[1].args[0]}")
            raise
    return params
