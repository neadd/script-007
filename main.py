import os
import utils.getconfig as cfg
import fileops as ops
def processrequest():
      parser=cfg.cmd_args_parser()
      params=parser.parse_args()
      try:
            os.chdir(params.folder)
      except NotADirectoryError:
            print("Absent folder")
            exit()
      ops.actions.get(params.cmd,(lambda x: print("Incorrect command: ".x)))(params.name)
      exit()

if __name__ == '__main__':
      processrequest()