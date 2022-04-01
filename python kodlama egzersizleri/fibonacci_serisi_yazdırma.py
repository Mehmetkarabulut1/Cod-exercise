a = 0
b = 1
buraya_kadar = int(input("sayı giriniz:"))
for i in range(0,buraya_kadar):
    a , b = b ,a+b
    print(a)