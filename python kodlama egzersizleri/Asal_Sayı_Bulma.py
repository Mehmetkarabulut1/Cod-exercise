def asal(sayı):
    if sayı == 1:
        return False
    elif sayı == 2:
        return True
    else:
        for i in range(2,sayı):
            if sayı % i == 0:
                return False
        return True
while True:
    sayı = input("sayı:")
    if sayı =="q":
        break
    else:
        sayı = int(sayı)
        if (asal(sayı)):
            print("asal: {}".format(sayı))
        else:
            print("değil")