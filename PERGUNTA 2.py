def verificar_e_contar_a(string):
    count = 0
    for char in string:
        if char.lower() == 'a':
            count += 1

    if count > 0:
        print(f"A letra 'a' aparece {count} vez(es) na string.")
    else:
        print("A letra 'a' não aparece na string.")

# Exemplo de uso:
texto = input("Digite uma string: ")
verificar_e_contar_a(texto)
