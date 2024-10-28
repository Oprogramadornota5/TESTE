def inverter_string(s):
    string_invertida = ""
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    return string_invertida

def main():
    # Você pode definir uma string aqui ou solicitar ao usuário
    string = input("Informe uma string para inverter: ")
    # string = "Olá, mundo!"  # Exemplo de string pré-definida
    string_invertida = inverter_string(string)
    print(f"String invertida: {string_invertida}")

if __name__ == "__main__":
    main()
