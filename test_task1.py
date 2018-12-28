import unittest
import task1

class test_task():
    def test_func(self):
      self.assertEqual(task1.func(2,'hex'), '0x2')
      self.assertEqual(task1.func(2), 'два')

if __name__ == '__main__':
    unittest.main()
