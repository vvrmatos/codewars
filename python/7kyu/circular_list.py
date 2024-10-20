#!/usr/bin/env python3


class CircularList:
    def __init__(self, *args):
        if not args:
            raise

        self.clist = args
        self.length = len(self.clist)
        self.index = None
        
    def next(self):
        if self.index is None:
            self.index = 0
            return self.clist[self.index]
        self.index = self.index + 1 if self.index + 1 < self.length else 0
        return self.clist[self.index]

    def prev(self):
        if self.index is None:
            self.index = -1
            return self.clist[self.index]
        self.index = self.index - 1 if self.index - 1 > -(self.length + 1) else -1
        return self.clist[self.index]
