def dupTripQuad(a):
    print(a)
    print(duplica(a))
    print(triplica(a))
    print(quadruplica(a))

def duplica(a):
    a = a * 2
    return a

def triplica(a):
    a = a * 3
    return a

def quadruplica(a):
    a = a * 4
    return a

x = float(input('Digite um número: '))
dupTripQuad(x)