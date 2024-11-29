ano = int(input("digite um ano: "))
if ano % 400 == 0:
    print("{} é bissexto!".format(ano))
    
elif ano % 4 == 0 and (ano % 100 !=0):
    print("{} é um ano bissexto ")
    