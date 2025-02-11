import unittest
from src.circular_FIFO_classes import CircularBufferQueue, CircularBufferList, CircularBufferListWithRewriting, CircularBufferQueueWithRewriting

class TestCircularBufferQueue(unittest.TestCase):
    def test_wrong_size(self):
        wrong_size = 'Some string'
        with self.assertRaises(ValueError):
            CircularBufferQueue(wrong_size)
    

    def test_add_item(self):
        buffer = CircularBufferQueue(3)
        buffer.add_item('Some item')

        self.assertEqual(buffer.buffer.qsize(), 1)
    

    def test_add_and_pop_item(self):
        buffer = CircularBufferQueue(3)
        buffer.add_item('Some item')
        
        self.assertEqual(buffer.pop_item(), 'Some item')
    

    def test_overflow(self):
        buffer = CircularBufferQueue(2)
        buffer.add_item('Item 1')
        buffer.add_item('Item 2')
        
        with self.assertRaises(OverflowError):
            buffer.add_item('Item 3')
    

    def test_empty(self):
        buffer = CircularBufferQueue(2)
        
        with self.assertRaises(IndexError):
            buffer.pop_item()
    

class TestCircularBufferList(unittest.TestCase):
    def test_wrong_size(self):
        wrong_size = 'Some string'
        with self.assertRaises(ValueError):
            CircularBufferQueue(wrong_size)
    

    def test_add_item(self):
        buffer = CircularBufferList(3)
        buffer.add_item('Some item')
        
        self.assertEqual(buffer.head, 0)
        self.assertEqual(buffer.tail, 1)
        self.assertEqual(buffer.count, 1)
    

    
    def test_add_and_pop_item(self):
        buffer = CircularBufferList(3)
        buffer.add_item('Some item')
        
        self.assertEqual(buffer.pop_item(), 'Some item')
        self.assertEqual(buffer.head, 1)
        self.assertEqual(buffer.tail, 1)
        self.assertEqual(buffer.count, 0)
     

    def test_overflow(self):
        buffer = CircularBufferList(2)
        buffer.add_item('Item 1')
        buffer.add_item('Item 2')
        
        with self.assertRaises(OverflowError):
            buffer.add_item('Item 3')
    

    def test_empty(self):
        buffer = CircularBufferList(2)
        
        with self.assertRaises(IndexError):
            buffer.pop_item()


class TestCircularBufferQueueWithRewriting(unittest.TestCase):
    def test_rewriting(self):
        buffer = CircularBufferQueueWithRewriting(2)
        buffer.add_item('Item 1')
        buffer.add_item('Item 2')
        
        self.assertEqual(str(buffer), str(['Item 1', 'Item 2']))
        buffer.add_item('Item 3')

        self.assertEqual(str(buffer), str(['Item 2', 'Item 3']))


class TestCircularBufferListWithRewriting(unittest.TestCase):
    def test_rewriting(self):
        buffer = CircularBufferListWithRewriting(2)
        buffer.add_item('Item 1')
        buffer.add_item('Item 2')
        
        self.assertEqual(str(buffer), str(['Item 1', 'Item 2']))
        buffer.add_item('Item 3')

        self.assertEqual(str(buffer), str(['Item 2', 'Item 3']))







