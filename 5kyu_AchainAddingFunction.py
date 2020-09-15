class add_chain(int):
    def __call__(self,v):
        return add_chain(self+v)
    
def add(v):
    return add_chain(v)