def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

test_function()
#inner_function()
# Попытка вызвать inner_function вне test_function приведёт к ошибке,
# так как функция определена только внутри test_function и не доступна снаружи.
