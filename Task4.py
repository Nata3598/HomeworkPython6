# Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный. 

# *Пример:* 

# 2+2 => 4; 

# 1+2*3 => 7; 

# 1-2*3 => -5;

# - Добавьте возможность использования скобок, меняющих приоритет операций.

#     *Пример:* 

#     1+2*3 => 7; 

#     (1+2)*3 => 9;

ln_in = input('Введите выражение: ').split()
if ln_in == '':
    ln_in = '( 1 + 2 ) * 3'

def calc(args):
    while len(args) != 1:
        while '*' in args or '/' in args:
            try:
                mul_index = args.index('*')
            except:
                mul_index = 100

            try:
                div_index = args.index('/')
            except:
                div_index = 100
            
            if mul_index < div_index:
                args[mul_index - 1] = float(args[mul_index - 1]) * float(args[mul_index + 1])
                args.pop(mul_index + 1)
                args.pop(mul_index)
            else:
                args[div_index - 1] = float(args[div_index - 1]) / float(args[div_index + 1])
                args.pop(div_index + 1)
                args.pop(div_index)


        while '+' in args or '-' in args:
            try:
                add_index = args.index('+')
            except:
                add_index = 100
            try:
                sub_index = args.index('-')
            except:
                sub_index = 100
            
            if add_index < sub_index:
                args[add_index - 1] = float(args[add_index - 1]) + float(args[add_index + 1])
                args.pop(add_index + 1)
                args.pop(add_index)
            else:
                args[sub_index - 1] = float(args[sub_index - 1]) - float(args[sub_index + 1])
                args.pop(sub_index + 1)
                args.pop(sub_index)
                
    return args[0]
    
def precalc(args):
    while ('(' in args):
        b = args.index('(')
        e = args.index(')', b)
        res = calc( args[ b+1:e ] )
        args[b] = res

        for i in range(e, b, -1):
            args.pop(i)

    return calc(args)
    

res = precalc(ln_in)
print( 'Результат:', res )