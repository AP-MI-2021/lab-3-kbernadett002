def is_palindrome(n):
    '''
    Determina daca un nr este palindrom
    :param n: int, un numar
    :return: True daca este palindrom si False in caz contrar
    '''
    oglindit_n = 0
    copie_n = n
    while n != 0:
        oglindit_n = oglindit_n * 10 + n % 10
        n = n // 10
    if oglindit_n == copie_n:
        return True
    else:
        return False


def is_power(n,k):
    '''
    Determina daca un nr n poate fi scris ca baza**k
    :param n: un nr intreg pozitiv
    :param k: o putere intreaga
    :return: True daca nr n poate fi scris ca baza**k sau False, in caz contrar
    '''
    baza=0
    while True:
        if baza**k==n:
            return True
        elif baza**k>n:
            return False
        baza=baza+1


def print_menu():
    print("1. Citire lista")
    print("2.Afisare cea mai lunga subsecventa de elemente palindroame")
    print("3.Afisare cea mai lunga subsecventa de elemente care se pot scrie ca x**k")
    print("4.Afisare cea mai lunga subsecventa de elemente cu toate numerele divizibile cu k")
    print("5. Iesire")


def citire_lista():
    l = []
    n = int(input("Dati nr de elemente"))
    for i in range(n):
        l.append(int(input("L[" + str(i) + "]=")))
    return l


def citire_putere():
    n=int(input("Dati puterea"))
    return n


def citire_k():
    n=int(input("Dati un numar"))
    return n

def toate_elementele_din_lista_sunt_palindroame(l):
    '''
    Determina daca toate elementele din lista sunt palindroame
    :param l: o lista de nr intregi
    :return: True daca toate elementele din lista sunt palindroame sau False, in caz contrar
    '''
    for x in l:
        if is_palindrome(x) is False:
            return False
    return True


def test_toate_elementele_din_lista_sunt_palindroame():
    assert toate_elementele_din_lista_sunt_palindroame([]) is True
    assert toate_elementele_din_lista_sunt_palindroame([2332,5665]) is True
    assert toate_elementele_din_lista_sunt_palindroame([23,5665,898]) is False


def get_longest_all_palindromes(lst:list[int]) -> list[int]:
    '''
    Determina cea mai lunga secventa de elemente palindroame
    :param lst:lista de nr intregi
    :return:cea mai lunga subsecventa de elemente palindroame
    '''
    subsecventa_max=[]
    for i in range(len(lst)):
        for j in range(i,len(lst)):
            if toate_elementele_din_lista_sunt_palindroame(lst[i:j+1]) and len(subsecventa_max)< len(lst[i:j+1]):
                subsecventa_max=lst[i:j+1]
    return subsecventa_max


def test_get_longest_all_palindromes():
    assert get_longest_all_palindromes([])==[]
    assert get_longest_all_palindromes([546,563,2487])==[]
    assert get_longest_all_palindromes([2332,456,1221,131,151])==[1221,131,151]


def toate_elementele_x_la_puterea_k(l,k):
    '''
    Determina daca toate elementele din lista sunt palindroame
    :param l: o lista de nr intregi
    :return: True daca toate elementele din lista sunt palindroame sau False, in caz contrar
    '''
    for x in l:
        if is_power(x,k) is False:
            return False
    return True


def test_toate_elementele_x_la_puterea_k():
    assert toate_elementele_x_la_puterea_k([25],2) is True
    assert toate_elementele_x_la_puterea_k([4,25,9],2) is True
    assert toate_elementele_x_la_puterea_k([23,56],5) is False


def get_longest_powers_of_k(lst: list[int], k: int) -> list[int]:
    '''
    Determina cea mai lunga subsecventa de elemente care se pot scrie ca x**k
    :param lst: o lista de numere intregi
    :param k: o putere
    :return: Cea mai lunga subsecventa de elemente care se pot scrie ca x**k
    '''
    subsecventa_max=[]
    for i in range(len(lst)):
        for j in range(i,len(lst)):
            if toate_elementele_x_la_puterea_k(lst[i:j+1],k) and len(subsecventa_max)< len(lst[i:j+1]):
                subsecventa_max=lst[i:j+1]
    return subsecventa_max


def test_get_longest_powers_of_k():
    assert get_longest_powers_of_k([],1)==[]
    assert get_longest_powers_of_k([4,25,9],2)==[4,25,9]
    assert get_longest_powers_of_k([2332,456,1221,131,151],56)==[]


def toate_numerele_divizibile_k(lst, k):
    '''
    Determina daca o secventa are toate numerele divizibile cu k
    :param lst: o lista de numere
    :param k: un numar intreg
    :return: True daca o secventa are toate numerele divizibile cu k sau False, in caz contrar
    '''
    for x in lst:
        if x % k != 0:
            return False
    return True


def test_toate_numerele_divizibile_k():
    assert toate_numerele_divizibile_k([12, 33, 66, 99], 3) is True
    assert toate_numerele_divizibile_k([10, 100000, 50000], 5) is True
    assert toate_numerele_divizibile_k([42, 778], 5) is False


def get_longest_div_k(lst: list[int], k: int) -> list[int]:
    '''
    Determina cea mai lunga subsecventa care are toate elementele divizibile cu k
    :param lst: o lista de nr
    :param k: un numar intreg
    :return: Cea mai lunga subsecventa care are toate elementele divizibile cu k.
    '''
    subsecventa_max = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if toate_numerele_divizibile_k(lst[i:j + 1], k) and len(subsecventa_max) < len(lst[i:j + 1]):
                subsecventa_max = lst[i:j + 1]
    return subsecventa_max


def test_get_longest_div_k():
    assert get_longest_div_k([21, 3, 33, 52, 45], 3) == [21, 3, 33]
    assert get_longest_div_k([5, 11, 56], 3) == []
    assert get_longest_div_k([2, 88, 33, 120], 3) == [33, 120]


def main():
    test_toate_elementele_din_lista_sunt_palindroame()
    test_get_longest_all_palindromes()
    test_toate_elementele_x_la_puterea_k()
    test_get_longest_powers_of_k()
    test_toate_numerele_divizibile_k()
    test_get_longest_div_k()
    k=0
    l = []
    while True:
        print_menu()
        optiune = input("Dati optiunea:")
        if optiune == "1":
            l = citire_lista()
        elif optiune=="2":
            print(get_longest_all_palindromes(l))
        elif optiune== "3":
            k = citire_putere()
            print (get_longest_powers_of_k(l,k))
        elif optiune=="4":
            k=citire_k()
            print(get_longest_div_k(l,k))
        elif optiune == "5":
            break
        else:
            print("Optiune gresita!Reincercati")

if __name__ == '__main__':
  main()

