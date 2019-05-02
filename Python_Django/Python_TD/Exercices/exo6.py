def singleton(classe_definie):
    instances = {}
    def get_instance(*args, **kwargs):
        if classe_definie not in instances:
            instances[classe_definie] = classe_definie(*args, **kwargs)
        return instances[classe_definie]
    return get_instance
@singleton
class Test:
    def __init__(self,val):
        self.val=val

a=Test("truc")
b=Test("machin")
print (a.val,id(a))
print(b.val,id(b))
print ( a is b)
