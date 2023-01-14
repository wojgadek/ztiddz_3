import random
import string


# funkcja moe przyjąć parametr z zadaną długością, domyślnie jest to 10
def generate_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for i in range(length))
# sprawdzenie, czy w stringu jest mała litera, wielka litera, cyfra i znak specjalny
    if (any(c.islower() for c in password) 
        and any(c.isupper() for c in password)
        and any(c.isdigit() for c in password) 
        and any(c in string.punctuation for c in password)):
        return password
# jeśli hasło nie spełnia wymagań, wygeneruj je jeszcze raz. 
    else:
        return generate_password(length)


password = generate_password()
print(password)