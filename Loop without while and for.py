def func1():
    print('hello func2')
    func2()
def func2():
    print('hi func1')
    func1()
func1()
