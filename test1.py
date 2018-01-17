import time, sys

from danmu import DanMuClient

def printDanmu(msg):
    print(msg.encode(sys.stdin.encoding, 'ignore').
        decode(sys.stdin.encoding))

dmc = DanMuClient('http://www.douyu.com/156277')
if not dmc.isValid(): print('Url not valid')

@dmc.danmu
def danmu_fn(msg):
    printDanmu('[%s] %s' % (msg['NickName'], msg['Content']))

@dmc.gift
def gift_fn(msg):
    # printDanmu('[%s] sent a gift!' % msg['NickName'])
    return

@dmc.other
def other_fn(msg):
    printDanmu('Other message received')

dmc.start(blockThread = True)