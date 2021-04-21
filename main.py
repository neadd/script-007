import os
import utils.getconfig as cfg
import fileops.fileops as ops



def processrequest():
      parser=cfg.cmd_args_parser()
      params=parser.parse_args()
      ops.execute_command(params)

if __name__ == '__main__':
      processrequest()