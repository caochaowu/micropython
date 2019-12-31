
import os, pyb
os.umount('/flash')
p1 = pyb.Flash(start=0, len=256*1024)
p2 = pyb.Flash(start=256*1024)
os.VfsFat.mkfs(p1)
os.VfsLfs2.mkfs(p2)
os.mount(p1, '/flash')
os.mount(p2, '/data')
os.chdir('/flash')



# import pyboard
# pyboard.execfile('C:/Users/caoch/Desktop/workspace/Git/micropython/micropython_ccw_git/tools/test.py', device='COM4')


# import pyboard
# pyb = pyboard.Pyboard('COM4')
# pyb.enter_raw_repl()
# pyb.exec('import pyb')
# pyb.exec('pyb.LED(1).on()')
# pyb.exit_raw_repl()





