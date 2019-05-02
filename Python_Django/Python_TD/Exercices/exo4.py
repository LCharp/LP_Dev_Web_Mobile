def pain(func):
    def wrapper():
        print("</'''''''\>")
        func()
        print("<\_____/>")
    return wrapper
def ingredients(func):
    def wrapper():
        print("#tomates#")
        func()
        print("~salade~")
    return wrapper

def sandwich(food="--jambon--"):
    print(food)

sandwich()

sandwich= pain(ingredients(sandwich))
sandwich()

@pain
@ingredients
def sandwich(nourriture="--jambon--"):
    print(nourriture)
    sandwich()

@ingredients
@pain
def sandwich_zarb(nourriture):
    print(nourriture)
sandwich_zarb()

