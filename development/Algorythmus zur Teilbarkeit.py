from random import randrange

stunde = 13 #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
hälftevonstunde = stunde / 2
erste_zahl = randrange(2, hälftevonstunde)
while stunde % erste_zahl > 0:
    erste_zahl = randrange(2, stunde)
zweite_zahl = stunde / erste_zahl
print(zweite_zahl)

if stunde % 2 > 0 or stunde % 3 > 0 or stunde < 4:
    print("nem")