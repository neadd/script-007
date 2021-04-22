"""File operations module"""
import sys
import os
import utils.logging as log


def execute_command(params):
    """Execute command according to request params"""
    try:
        os.chdir(params.folder)
    except (NotADirectoryError,PermissionError,FileNotFoundError):
        log.raiserror("Incorrect folder, exception " 
                      + sys.exc_info()[1].args[0])
        exit()
    result = actions.get(params.cmd,
                        lambda x: log.raiserror("Incorrect command: "+x)
                        )(params.name)
    return result

def list(_):
    """List folder contents"""
    try:
        result = os.listdir(None)
    except OSError:
        log.raiserror("list folder error" + sys.exc_info()[1].args[0])
    return result

def create(filename):
    """Create file in folder"""
    try:
        if os.path.exists(filename):
            raise OSError("File exists")
        with open(filename, "w") as fhandler:
            result = "File created: " + filename
    except OSError:
        log.raiserror("Create file error: " + sys.exc_info()[1].args[0])
    return result

def delete(filename):
    """Delete file in folder"""
    try:
        os.remove(filename)
        result = "File deleted: " + filename
    except OSError:
        log.raiserror("Delete file error: " + sys.exc_info()[1].args[0])   
    return result

def read(filename):
    """Open and read file"""
    try:
        with open(filename, "r") as fhandler:
            result = fhandler.read()
    except OSError:
        log.raiserror("Read file error: " + sys.exc_info()[1].args[0]) 
    return result

def meta(filename):
    """Get file metainformation"""
    try:
        statinfo = os.stat(filename)
    except OSError:
        log.raiserror("Meta file error: " + sys.exc_info()[1].args[0])
    return statinfo

def getactionslist():
    """Get list of possible actions"""
    return actions.keys()

actions={
        "list"   : list,
        "create" : create,
        "delete" : delete ,
        "read"   : read,
        "meta"   : meta
        }
