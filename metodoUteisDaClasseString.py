nome = "fabAnO"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "   Olá mundo!"
print(texto)
print(texto.strip() + "  .")
print(texto.rstrip() + "  .")
print(texto.lstrip() + "  .")

menu = "Python"

print("P-y-t-h-o-n") # pra não precisar por o - em todos os espaços eu posso fazer como no exemplo abaixo:
print("-".join(menu))