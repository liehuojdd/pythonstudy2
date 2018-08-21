import os

def ContinueKey():
    print('Please press "ENTER" to continue, or press "q" to retry:')
    letter = input()
    i=1
    if letter == 'q':
        ContinueKey()
    else:
        return

os.system('D:\KuGou\CD1\simple1.mp3')
print('Line 1')
ContinueKey()
print('Line 2')
ContinueKey()