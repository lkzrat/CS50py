class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.cookies = 0

    def __str__(self):
        return '🍪'*self.size
    
    def deposit(self, n):
         try:
             self.cookies += n
         except ValueError:
             raise Exception('Invalid cookies format')
         if self.size > self.capacity:
                raise ValueError('The jar is already full')

    def withdraw(self, n):
         try:
             self.cookies -= n
         except ValueError:
            raise Exception('Invalid cookies format')
         if self.size < 0:
            raise ValueError('The jar is already empty')

    @property
    def size(self):
        return self.cookies

    @property
    def capacity(self):
        return  self._capacity

    @capacity.setter
    def capacity(self, capacity):
        try:
            capacity = int(capacity)
        except ValueError:
            raise ValueError('Invalid capacity format, only integers')
        if capacity < 0:
            raise ValueError('Negative capacity is not valid')
        else:
            self._capacity = capacity