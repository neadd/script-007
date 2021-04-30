"""Configuration module"""
import os
import sys
import configparser
import utils.mylogger as log


def readconfig():
    """Read initial config and setup variables"""
    try:
        global NAMLEN
        global DEFSTORAGE
        global PROTECT_ENABLE
        global PROTECT_KEYFILE
        config = configparser.ConfigParser()
        config.read('config.ini')
        NAMLEN = int(config['MAIN']['MAX_NAMELEN'])
        DEFSTORAGE = config['MAIN']['STORAGE']
        PROTECT_ENABLE = int(config['PROTECT']['ENABLE'])
        if PROTECT_ENABLE == True:
            PROTECT_KEYFILE = config['PROTECT']['KEYFILE']
        else:
            PROTECT_KEYFILE = None
    
    except (configparser.Error,TypeError,ValueError):
        log.raiserror(f"Config file error: {sys.exc_info()[1].args[0]}")
        exit()

def getmaxnamelen():
    """Get configured maximum length of file name"""
    return NAMLEN

def getdefstorage():
    """Get default storage folder"""
    return DEFSTORAGE

def getprotectkeyfile():
    """Get keyfile for protection"""
    return PROTECT_KEYFILE

def isprotectenabled():
    """check enable protection"""
    return PROTECT_ENABLE
