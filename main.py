import os
import utils.getconfig as cfg
import file as ops
def processrequest():
      parser=cfg.cmd_args_parser()
      params=parser.parse_args()
      try:
            os.chdir(params.folder)
      except NotADirectoryError:
            print("Absent folder")
            exit()
      if params.cmd == 'list':
            ops.list()
      elif params.cmd == 'create':
            ops.create(params.name)
      elif params.cmd == 'delete':
            ops.delete(params.name)
      elif params.cmd == 'read':
            ops.read(params.name)
      elif params.cmd == 'meta':
            ops.meta(params.name)
      else:
            print("Incorrect command")
            exit()

if __name__ == '__main__':
      processrequest()