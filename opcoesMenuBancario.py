import datetime

menu = """
[ D ] Depositar
[ S ] Sacar
[ E ] Extrato
[ Q ] Sair
"""

saldo = 0
limite = float(500)
extratos_bancarios = {
    "Extrato de Deposito": [],
    "Extrato de Saques": [],
    "Extrato Geral": []
}
numeros_saques = 0
LIMITE_SAQUES = 3
data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # DATA atual e hora

while True:
    opcao = input(menu)

    if opcao.upper() == "D":
        valor_deposito = float(input("Valor de deposito: R$ "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extratos_bancarios["Extrato de Deposito"].append(f"Data: {str(data)} - Deposito: R$ {valor_deposito:.2f}")
            extratos_bancarios["Extrato Geral"].append(f"Data: {str(data)} - Deposito: R$ {valor_deposito:.2f}")
        else:
            print("Depositar acima de R$ 0")

    elif opcao.upper() == "S":
        if numeros_saques < LIMITE_SAQUES:

            valor_saque = float(input("Valor de saque: R$ "))
            if valor_saque > 0:
                if valor_saque <= limite and valor_saque <= saldo:
                    extratos_bancarios["Extrato de Saques"].append(f"Data: {str(data)} - Saque: R$ {valor_saque:.2f}")
                    extratos_bancarios["Extrato Geral"].append(f"Data: {str(data)} - Saque: R$ {valor_saque:.2f}")
                    print("Saque Realizado com Sucesso!")
                    numeros_saques += 1
                else:
                    print(f"O limite de saque é de {limite:.2f}")
            else:
                print("Você deve informar um valor de saque válido!")
        else:
            print("Você não pode efetuar o saque, você escedeu o limite diário (3 saques)")

    elif opcao.upper() == "E":
        while True:
            opcao_de_estrato = int(input("""
    [ 1 ] Extrato Geral
    [ 2 ] Extrato de Saques
    [ 3 ] Extrato de Depósitos
    [ 4 ] Sair
    """))

            if opcao_de_estrato == 1:
                for extrato_geral in extratos_bancarios["Extrato Geral"]:
                    print(extrato_geral)

            if opcao_de_estrato == 2:
                for extrato_saque in extratos_bancarios["Extrato de Saques"]:
                    print(extrato_saque)

            if opcao_de_estrato == 3:
                for extrato_deposito in extratos_bancarios["Extrato de Deposito"]:
                    print(extrato_deposito)

            if opcao_de_estrato == 4:
                break
    elif opcao.upper() == "Q":
        break

    else:
        print("Operação inválida, por favor digite uma opção válida.")
print("Volte sempre e conte com os nossos serviços!")
