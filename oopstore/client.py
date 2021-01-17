from .storage import OOPStorage
class Client:
    def __init__(self, path):
        self.path = path
    
    def save(self, key, obj):
        oopstore = OOPStorage(key, obj)
        oopstore.save()
    
