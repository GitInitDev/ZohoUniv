import random
char = 'qwertyuiopasdfghjklzxcvbnm!@#$%^&*(()'
stren = 10
password = "".join(random.sample(char , stren))
print (password)
