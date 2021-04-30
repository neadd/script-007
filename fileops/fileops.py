"""File operations module"""
import sys
import os
import utils.mylogger as log


actions=["list","create","delete","read","meta"]

def getactions():
    """Get list of possible actions"""
    return actions

def execute_command(fileservice):
    """Execute command according to request params"""
    command=fileservice.getcmd()
    if command=="list":
        result=fileservice.list()
    elif command=="create":
        result=fileservice.create()
    elif command=="delete":
        result=fileservice.delete()
    elif command=="read":
        result=fileservice.read()
    elif command=="meta":
        result=fileservice.meta()
    else:
        log.raiserror(f"Incorrect command {command}")
        raise ValueError(f"Incorrect command {command}")
    return result


class Filservice:
    
    _instance=None
    _not_inited=True
    def __new__(cls,*args,**kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance=super(Filservice,cls).__new__(cls)
        return cls._instance
    
    def __init__(self,*args,**kwargs):
        if self._not_inited:
            self._params=args[0]
            try:
                os.chdir(self._params.folder)
            except (NotADirectoryError,PermissionError,FileNotFoundError):
                log.raiserror(
                    f"Incorrect folder, exception {sys.exc_info()[1].args[0]}")
                raise
            self._not_inited=False
    
    def getcmd(self):
        return self._params.cmd
    
    def getparams(self):
        return self._params
    
    def list(self):
        """List folder contents"""
        try:
            result = os.listdir('')
        except OSError:
            log.raiserror(f"list folder error {sys.exc_info()[1].args[0]}")
            raise
        return result
    
    def create(self):
        """Create file in folder"""
        try:
            if os.path.exists(self._params.name):
                raise OSError("File exists")
            with open(self._params.name, "xb") as fhandler:
                fhandler.write(self._params.data)
                result = f"File created: {self._params.name}"
        except OSError:
            log.raiserror(f"Create file error: {sys.exc_info()[1].args[0]}")
            raise
        return result
    
    def delete(self):
        """Delete file in folder"""
        try:
            os.remove(self._params.name)
            result = f"File deleted: {self._params.name}"
        except OSError:
            log.raiserror(f"Delete file error: {sys.exc_info()[1].args[0]}")
            raise
        return result
    
    def read(self):
        """Open and read file"""
        try:
            with open(self._params.name, "rb") as fhandler:
                result = fhandler.read()
        except OSError:
            log.raiserror(f"Read file error: {sys.exc_info()[1].args[0]}")
            raise
        return result
    
    def meta(self):
        """Get file metainformation"""
        try:
            statinfo = os.stat(self._params.name)
        except OSError:
            log.raiserror(f"Meta file error: {sys.exc_info()[1].args[0]}")
            raise
        return statinfo
