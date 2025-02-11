from queue import Queue
from typing import Any


class CircularBufferQueue:
    '''Create a circular buffer object with a given maximum size
    
    If size not integer, raise exception 'Size must be integer'
    '''
    def __init__(self, size:int) -> None:
        if not isinstance(size, int):
            raise ValueError('Size must be integer')
        
        self.size = size
        self.buffer = Queue(maxsize=size)


    def add_item(self, item:Any) -> None:
        '''Add an item in the circular buffer.
        
        If buffer is full, raise exception 'Buffer is full'
        '''
        if self.buffer.full():
            raise OverflowError('Buffer is full')
        
        self.buffer.put(item)


    def pop_item(self) -> Any:
        '''Remove and terurn the item
        
        If buffer is empty, raise exception 'Buffer is empty'
        '''
        if self.buffer.empty():
            raise IndexError('Buffer is empty')
        
        return self.buffer.get()
    
    
    def __str__(self) -> str:
        return str(list((self.buffer.queue)))


class CircularBufferList:
    '''Create a circular buffer object with a given maximum size
    
    If size not integer, raise exception 'Size must be integer'
    '''
    def __init__(self, size:int) -> None:
        if not isinstance(size, int):
            raise ValueError('Size must be integer')
        
        self.size = size
        self.buffer = [None] * size
        self.head = 0 
        self.tail = 0  
        self.count = 0  


    def add_item(self, item:Any) -> None:
        '''Add an item in the circular buffer.
        
        If buffer is full, raise exception 'Buffer is full'
        '''
        if self.is_full():
            raise OverflowError('Buffer is full')
        
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.size
        self.count += 1


    def pop_item(self) -> Any:
        '''Remove and terurn the item
        
        If buffer is empty, raise exception 'Buffer is empty'
        '''
        if self.is_empty():
            raise IndexError('Buffer is empty')
        
        item = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.size
        self.count -= 1

        return item


    def is_full(self) -> bool:
        '''Return True if buffer is full, else return False'''
        return self.count == self.size


    def is_empty(self) -> bool:
        '''Return True if buffer is empty, else return False'''
        return self.count == 0
    

    def __str__(self) -> str:
        if self.head < self.tail:
            return str(self.buffer[self.head:self.tail])
        return str(self.buffer[self.head:] + self.buffer[:self.tail])


class CircularBufferQueueWithRewriting(CircularBufferQueue):
    def add_item(self, item:Any) -> None:
        '''Add an item in the circular buffer.
        
        If buffer is full, rewriting oldest item in the buffer
        '''
        if self.buffer.full():
            self.pop_item()
        
        self.buffer.put(item)


class CircularBufferListWithRewriting(CircularBufferList):
    def add_item(self, item:Any) -> None:
        '''Add an item in the circular buffer.
        
        If buffer is full, rewriting oldest item in the buffer
        '''
        if self.is_full():
            self.pop_item()
        
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.size
        self.count += 1
