import os
import utils.config as cfg
import file as ops

if __name__ == '__main__':
      parser=cfg.cmd_args_parser()
      params=parser.parse_args()
      os.chdir(params.folder)
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
