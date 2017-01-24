import unittest

import sys
sys.path.append('..\src')
from Event import Event

class TestEvent(unittest.TestCase):
    def test_init(self):
        watcher = MockFileWatcher()
        watcher.fileChanged += log_file_change
        watcher.watchFiles()

def log_file_change(source_path):
    test = unittest.TestCase
    test.assertEquals(source_path, "foo")

def log_file_change2(source_path):
    print "%r changed!" % (source_path,)

class MockFileWatcher:
    def __init__(self):
        self.fileChanged = Event.Event()

    def watchFiles(self):
        source_path = "foo"
        self.fileChanged(source_path)






