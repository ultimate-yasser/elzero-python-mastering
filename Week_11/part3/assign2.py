def decorate(func):
    print("Sugar Added From Decorators")
    func()
    print('#' * 20)

@decorate
def make_tea():
  print("Tea Created")

@decorate
def make_coffe():
  print("Coffe Created")