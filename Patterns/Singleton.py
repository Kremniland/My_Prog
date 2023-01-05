class Solar:
    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance = super(Solar, cls).__new__(cls)
        return cls.instance


s = Solar()
print(id(s))
print(s)

d = Solar()
print(id(d))
print(d)

