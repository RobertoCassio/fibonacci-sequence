

def fibbonaci():
    fibbo = 0
    fibbo1 = 1
    fibbo2 = 1
    Num = int(input("Digite um número acima de 3 que você deseja que a sequência de Fibonacci va até: \n"))

    if Num > 2:
        print (fibbo)
        print (fibbo1)
        print (fibbo2)

        while fibbo < Num:
            fibbo = fibbo1 + fibbo2
            if fibbo <= Num:
                print (fibbo)
            fibbo1 = fibbo2
            fibbo2 = fibbo
    else:
        print ("O numero informado é inferior a 2, favor inserir um valor válido \n")
        fibbonaci()
fibbonaci()
Retry = int(input("Deseja verificar outro número? 1 para Sim e 2 Para Não \n"))
if Retry == 1:
    fibbonaci()
else:
    print("Obrigado por utilizar")