def decorate(arg1, arg2, arg3):
    print('Je suis dans la fonction "decorate".')
    def decorated(func):
        print ('Je suis dans la fonction "decorated".')
        def wrapper(*args, **kwargs):
            print('Je suis dans la fonction "wrapper".')
            print ("les arguments du décorateurs sont: %s, %s, %s." % (arg1, arg2, arg3))
            print ("Pré-traitement.")
            print ("Execution de la fonction %s." % func. __name__)
            response = func(*args, **kwargs)
            print ("Post-traitement.")
            return response
        return wrapper
    return decorated

@decorate("Arg 1", "Arg 2", "Arg 3")
def foobar():
    print("Je suis foobar, je vous reçois 5 sur 5.")

foobar()
