# def func_decorator(func): 
#     def wraper(*args, **kwargs): 
#         print("---  some actions ---") 
#         result = func(*args, **kwargs) 
#         print("---  some actions ---") 
#         return result 
#     return wraper 

# @func_decorator   #   Декоррирует ф-ию func_decorator - ф-ией some_func 
# def some_func(): 
#     print('Functia some_func') 


# if __name__ == '__main__': 
    
#     # f = func_decorator(some_func)    #  Или в двестроки вот так или в 1 строку как далее 
#     # f() 
   
#      some_func()       # Вызов декоратора some_func

def func_dec(func):
    def wraper(*args, **kwargs):
        x, y = args
        func(x+y)
        print('ok!')
        return
    
    return wraper

@func_dec
def start(*args):
    print(args)


start(2,3)
