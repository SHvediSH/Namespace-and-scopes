def test_function():
    #inner_function()                                    #Это неправильная запись кода, невозможно вызвать функцию которая была создана после написания команды.
    def inner_function():
        print("Я в области видимости test_function!")
        global inner_function

test_function()
#inner_function()                                        #Это так же не правильная запись, данная функция создана локально внутри test_function и не может быть вызвана отдельно