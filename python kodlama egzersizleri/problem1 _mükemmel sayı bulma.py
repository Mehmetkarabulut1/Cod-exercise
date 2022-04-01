#Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.
#Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)
while True:
    a = int(input("sayı giriniz: "))
    c = a
    for i in range(1,a):
        if a % i == 0:
            c -= i
        elif c == 0:
            print("mükemmel sayı")
            break
        else:
            print("mükemmel değil")
            break
