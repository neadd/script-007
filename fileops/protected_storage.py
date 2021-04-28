"""Protect files by signature"""
import sys
import os
import hashlib
from collections import OrderedDict
from datetime import datetime
import utils.mylogger as log
import utils.getconfig as cfg
import utils.Exceptions as exc

class Protected_storage():
    def __init__(self,fops):
        try:
            with open(cfg.getprotectkeyfile(), "r") as kfile:
                self._storagekey = kfile.read()
        except OSError:
            log.raiserror(f"Read file error: {sys.exc_info()[1].args[0]}")
            raise
        self._storageclass=fops
    
    def _calc_signature(self,fname,content,meta):
        try:
            hashdata = OrderedDict(
                name=fname,
                mod_date=datetime.fromtimestamp(meta.st_mtime).strftime("%Y.%m.%d %H:%M:%S"),
                size=meta.st_size,
                content=content,
                salt=self._storagekey,
                user_id=meta.st_uid
                )
            buf=''.join('{}{}'.format(key,val) for key,val in hashdata.items())
            hash_obj = hashlib.md5(buf.encode())
            return hash_obj.hexdigest()
        except Exception:
            log.raiserror(f"signature calc error: {sys.exc_info()[1].args[0]}")
            raise
    
    def getcmd(self):
        """skip getcmd to base method"""
        return self._storageclass.getcmd()
    
    def getparams(self):
        """skip getparams to base method"""
        return self._storageclass.getparams()
    
    def list(self):
        """ skip list to base method"""
        return self._storageclass.list()
    
    def create(self):
        """Decorate for create file in folder"""
        try:
            result=self._storageclass.create()
            meta=self._storageclass.meta()
            params=self._storageclass.getparams()
            md5hash=self._calc_signature(params.name,params.data,meta)
            sigdir=os.path.join('.','.sig')
            if not os.path.isdir(sigdir):
                if os.path.exists(sigdir):
                    raise NotADirectoryError(f"Not a folder: {sigdir}")
                os.mkdir(sigdir)
            sigfile=os.path.join('.','.sig',params.name)
            with open(sigfile, "x") as shandler:
                shandler.write(md5hash)
        except Exception:
            log.raiserror(f"Create file error: {sys.exc_info()[1].args[0]}")
            raise
        return result
    
    def delete(self):
        """Delete file in folder and its signature"""
        try:
            params=self._storageclass.getparams()
            result=self._storageclass.delete()
            sigfile=os.path.join('.','.sig',params.name)
            os.remove(sigfile)
        except OSError:
            log.raiserror(f"Delete file error: {sys.exc_info()[1].args[0]}")
            raise
        return result
    
    def read(self):
        """Open and read file, check signature"""
        try:
            content=self._storageclass.read()
            meta=self._storageclass.meta()
            params=self._storageclass.getparams()
            md5hash=self._calc_signature(params.name,content,meta)
            sigfile=os.path.join('.','.sig',params.name)
            with open(sigfile, "r") as shandler:
                storedhash=shandler.read()
            if md5hash != storedhash:
                content=''
                raise exc.Signature_Error("Hash differ")
        except OSError:
            log.raiserror(f"Read file error: {sys.exc_info()[1].args[0]}")
            raise
        return content
    
    def meta(self):
        """ skip meta to base method"""
        return self._storageclass.meta()