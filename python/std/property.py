"""A property object has getter, setter, and deleter methods usable as decorators 
that create a copy of the property with the corresponding accessor function set to the
decorated function. This is best explained with an example:
"""
class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x
    
    # Setter and deleter must have the same function name
    # as the getter
    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x

c = C()
c.x = 2
print(c.x)
