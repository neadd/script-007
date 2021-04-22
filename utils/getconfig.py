"""Configuration module"""
import os
import sys
import configparser
import utils.mylogger as log


def readconfig():
    """Read initial config and setup variables"""
    try:
        global __NAMLEN__
        global __DEFSTORAGE__
        config = configparser.ConfigParser()
        config.read('config.ini')
        __NAMLEN__ = int(config['MAIN']['MAX_NAMELEN'])
        __DEFSTORAGE__ = config['MAIN']['STORAGE']
    
    except (configparser.Error,TypeError,ValueError):
        log.raiserror("Config file error: " + sys.exc_info()[1].args[0])
        exit()

def getmaxnamelen():
    """Get configured maximum length of file name"""
    return __NAMLEN__

def getdefstorage():
    """Get default storage folder"""
    return __DEFSTORAGE__
