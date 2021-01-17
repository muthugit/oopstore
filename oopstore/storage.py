class OOPStorage:
    def __init__(self, key, obj):
        self.key = key
        self.obj = obj
        self.get_type()
    
    def get_type(self):
        self.type = type(self.obj).__name__
        try:
            self.keys = self.obj.__dict__
        except:
            self.keys = None
        
    def save(self):
        print(self.type)
        print(self.key)
        print("Saved")


if __name__ == "__main__":
    test = 'muthu'
    oop = OOPStorage(test)
    print(oop.keys)
    oop.save()