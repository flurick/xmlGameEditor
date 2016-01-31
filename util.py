from PySide.QtCore import *
from PySide.QtGui import *

def check(box, state):
    if state=="0":
        qstate = Qt.CheckState(0)  # unChecked
    elif state=="-1":
        qstate = Qt.CheckState(2)  # checked
    else:
        qstate = Qt.CheckState(1)  # PartiallyChecked
    box.setCheckState(qstate)


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


def find_first(pattern, path):
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                return (os.path.join(root, name))
    return 'failed'
