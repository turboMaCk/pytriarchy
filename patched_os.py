from lib.patch_in import patch_in

patch_in(__name__, "os")

def getlogin():
    return 'you cannot'
