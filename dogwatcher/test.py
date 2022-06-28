import unittest
from filewatcher2 import FileWatcherBinding

class Test(unittest.TestCase):
    def setup(self):
        pass
        
    
    def test_a_file_event_hadler(self):
        """
        
        """
        self.instance = FileWatcherBinding(1)
        self.instance.file_event_hadler('test/test.txt')
    
    def test_b_dir_event_handler(self):
        self.instance = FileWatcherBinding(1)
        self.instance.dir_event_handler('test')

if _name_ == "_main_":
    unittest.main()
