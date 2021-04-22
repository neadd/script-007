"""Main module of fileserver"""
import os
import logging
import utils.getconfig as cfg
import utils.requestparams as req
import fileops.fileops as ops


def processrequest():
    """Get request parameters and call execute request"""
    params = req.requestparams()
    responce = ops.execute_command(params)
    return responce

if __name__ == '__main__':
    logging.basicConfig(filename = 'fileserver.log',
                        format   = '%(asctime)s %(message)s',
                        level    = logging.WARNING)
    cfg.readconfig()
    result = processrequest()
    print result
