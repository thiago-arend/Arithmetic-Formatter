import re

def arithmetic_arranger(problems, show=False):
    # ---- validações -----
    # testa a quantidade de problemas
    if len(problems) > 5:
        return "Error: Too many problems"

    # descobre qual o operador
    # testa a presença de + ou -
    operador = None  # 1 == + ; 0 == -
    linha1 = list()
    linha2 = list()
    linha3 = list()
    linha4 = list()

    for p in problems:
        if " + " not in p and " - " not in p:
            return "Error: Operator must be '+' or '-'"
        elif " + " in p and " - " not in p:
            operador = 1
        elif " - " in p and " + " not in p:
            operador = 0

        # captura os numeros da operação
        if operador:
            numeros = p.split(" + ")
            operacao = "+"
        else:
            numeros = p.split(" - ")
            operacao = "-"

        # testa pelo tamanho dos numeros
            # captura o tamanho do maior
        # testa pela presença de digitos
        len_maior_numero = None
        numero_final = 0  # resultado da operação

        for n in numeros:
            if len(n) > 4:
                return "Error: Numbers cannot be more than four digits"

            if re.search("[^0-9]", n):
                return "Error: Numbers must only contain digits"

            len_corrente = len(n)
            if len_maior_numero is None or len_corrente > len_maior_numero:
                len_maior_numero = len_corrente

            # realiza operação
            if operador:
                numero_final = int(numeros[0]) + int(numeros[1])
            else:
                numero_final = int(numeros[0]) - int(numeros[1])

        # preenche 7 colunas, 1 linha
        # 4 colunas de operações, 3 de espaços

        str_num_final = str(numero_final)

        len_opr_1 = len(numeros[0])
        len_opr_2 = len(numeros[1])
        len_resultado = len(str_num_final)

        recuos_col_1_lin_3 = len_maior_numero + 2
        recuos_col_1_lin_1 = recuos_col_1_lin_3 - len_opr_1
        recuos_col_1_lin_2 = recuos_col_1_lin_3 - len_opr_2 - 1
        recuos_col_1_lin_4 = recuos_col_1_lin_3 - len_resultado

        pedaco = ""
        for i in range(recuos_col_1_lin_1):
            pedaco += " "
        pedaco += numeros[0]
        linha1.append(pedaco)

        pedaco = operacao  # variável foi definida no momento do split() dos operandos
        for i in range(recuos_col_1_lin_2):
            pedaco += " "
        pedaco += numeros[1]
        linha2.append(pedaco)

        pedaco = ""
        for i in range(recuos_col_1_lin_3):
            pedaco += "-"
        linha3.append(pedaco)

        pedaco = ""
        for i in range(recuos_col_1_lin_4):
            pedaco += " "
        pedaco += str_num_final
        linha4.append(pedaco)

    linhas = [linha1, linha2, linha3, linha4]

    # testa se arg 'show' é verdadeiro
    if not show:
        linhas.pop(3)  # linhas correspondente ao resultado

    for linha in linhas:
        linha_saida = ""
        col_index = 1
        for coluna in linha:
            linha_saida += coluna
            if col_index == len(linha): break  # len(linha) armazena o numero de operações
            linha_saida += "    "
            col_index += 1
        print(linha_saida)

print(arithmetic_arranger(["23 - 5", "6743 - 6755", "324 + 8888", "456 - 78", "67 - 900"], True))

"""
lista = list()
mostrar = False
i = 5
while i > 0:
    problema = input("Entre com um cálculo de soma ou subtração."
                     "\nLembre-se de utilizar espaços ao redor do sinal de operação.\n"
                     "Digite 'sair' para fechar o programa")
    if problema == "sair": break
    lista.append(problema)
    i -= 1
    print(i, "operações restantes")

print(arithmetic_arranger(lista, True))
"""
