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