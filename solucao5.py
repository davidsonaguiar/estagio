def inverter_string(string):
    string_invertida = ""
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]
    return string_invertida

entrada = input("Digite uma string para inverter: ")
inverso = inverter_string(entrada)
print("String invertida:", inverso)