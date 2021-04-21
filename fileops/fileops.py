import os
import sys
# import utils.getconfig as cfg
import utils.logging as log


def execute_command(params):
      try:
            os.chdir(params.folder)
      except (NotADirectoryError,PermissionError,FileNotFoundError):
            log.raiserror("Incorrect folder, exception "+sys.exc_info()[1].args[0])
            exit()
      actions.get(params.cmd,lambda x: log.raiserror("Incorrect command: "+x))(params.name)
      exit()

def list(_):
    try:
        for fname in os.listdir(None):
            print(fname)
    except OSError:
        log.raiserror("list folder error")
    return

def create(filename):
    try:
        with open(filename,'w') as fhandler:
            print("File created: "+filename)
    except OSError:
        log.raiserror("Create file error: "+sys.exc_info()[1].args[0])
    return

def delete(filename):
    try:
        os.remove(filename)
        print("File deleted: "+filename)
    except OSError:
        log.raiserror("Delete file error: "+sys.exc_info()[1].args[0])   
    return

def read(filename):
    try:
        with open(filename,'r') as fhandler:
            print("File: "+filename)
            print(fhandler.read())
    except OSError:
        log.raiserror("Read file error: "+sys.exc_info()[1].args[0]) 
    return

def meta(filename):
    try:
        statinfo=os.stat(filename)
        print("File: "+filename)
        print(statinfo)
    except OSError:
        log.raiserror("Read file error: "+sys.exc_info()[1].args[0])
    return

def getactionslist():
    return actions.keys()

actions={'list':list,'create':create,'delete':delete,'read':read,'meta':meta}