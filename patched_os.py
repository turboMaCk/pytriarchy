from lib.patch_in import patch_in
import os

patch_in(__name__, "os")

def getlogin():
    return 'you cannot'

def i_can():
    return os.getlogin()
