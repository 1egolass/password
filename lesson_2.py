import random 



symbol =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password = int(input("пожалуйста ведите длину пароля"))

generated_password = ""

for i in range(password):
    generated_password += random.choice (symbol)

print(generated_password)