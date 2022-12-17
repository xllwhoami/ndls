class NDict(dict):
    instances = {}

    def __new__(cls, name: str, *args, **kwargs):
        if not cls.instances:
            cls.instances[name] = dict.__new__(cls, *args, **kwargs)
        
        
        if cls.instances.get(name) is None:
            cls.instances[name] = dict.__new__(cls, *args, **kwargs)
        
            
        return cls.instances[name]
        
        
    def __init__(self, name, new=False, *args, **kwargs):
        super().__init__(self, *args, **kwargs)


class NList(list):
    instances = {}

    def __new__(cls, name: str, *args, **kwargs):
        if not cls.instances:
            cls.instances[name] = list.__new__(cls, *args, **kwargs)
        
        
        if cls.instances.get(name) is None:
            cls.instances[name] = list.__new__(cls, *args, **kwargs)
        
            
        return cls.instances[name]
        
        
    def __init__(self, name, *args, **kwargs):
        super().__init__(self, *args, **kwargs)