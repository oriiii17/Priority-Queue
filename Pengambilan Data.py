def peek(self):
    if self.is_empty() == True:
        return None
    else:
        return tuple([self._head._data, self._head._priority])