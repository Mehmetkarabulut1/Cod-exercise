#1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastıran işlemler 3 farklı şekilde yazılmıştır.
#1
i = 0
while i < 101: 
    if i%3 == 0:
        print(i)
    i += 1

#2
for i in range(0,101):
    if i%3 == 0:
        print(i)

#3
for i in range(0,101):
    if i%3 != 0:
        continue
    print(i)
