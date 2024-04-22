tum_karakter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

parola_uzunluğu = int(input("parolanın uzunluğu girin: "))

import random
parola = ''.join(random.choice(tum_karakter) for i in range (parola_uzunluğu))

print("oluşturan parolası", parola)
