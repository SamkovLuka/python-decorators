from datetime import datetime



def show_args(func):
    def wrapper(*args, **kwargs):
        if args or kwargs:
            print("Отримані аргументи:", args, kwargs)
        else:
            print("Аргументів немає")
        return func(*args, **kwargs)
    return wrapper




def show_datetime(func):
    def wrapper(*args, **kwargs):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("Функція виконана:", now)
        return func(*args, **kwargs)
    return wrapper



def require_args(func):
    def wrapper(*args, **kwargs):
        if not args and not kwargs:
            print("Помилка: потрібно хоча б один аргумент!")
            return None
        return func(*args, **kwargs)
    return wrapper




@show_args
def test(a, b, c=10):
    return a + b + c

test(1, 2, c=3)



@show_datetime
def hello():
    print("Привіт!")

hello()




@require_args
def mult(a, b):
    return a * b

print(mult(5, 2))
print(mult())
