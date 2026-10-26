"""
Calculadora em Python (terminal)

Operações: adição, subtração, multiplicação e divisão.
O programa mostra um menu, lê a operação e os valores,
exibe o cálculo realizado e o resultado, e trata divisão por zero.
"""


def exibir_titulo():
    """Mostra o título do programa."""
    print("=" * 40)
    print("          CALCULADORA EM PYTHON")
    print("=" * 40)


def exibir_menu():
    """Mostra o menu de opções e as orientações de uso."""
    print("\nEscolha uma operação:")
    print("  1 - Adição         (+)")
    print("  2 - Subtração      (-)")
    print("  3 - Multiplicação  (*)")
    print("  4 - Divisão        (/)")
    print("  0 - Sair")
    print("-" * 40)
    print("Dica: use ponto ou vírgula para decimais (ex.: 2.5 ou 2,5).")


def ler_numero(mensagem):
    """Lê um número digitado pelo usuário, repetindo até ser válido."""
    while True:
        texto = input(mensagem).strip().replace(",", ".")
        try:
            return float(texto)
        except ValueError:
            print("Valor inválido! Digite apenas números.")


def somar(primeiro_numero, segundo_numero):
    return primeiro_numero + segundo_numero


def subtrair(primeiro_numero, segundo_numero):
    return primeiro_numero - segundo_numero


def multiplicar(primeiro_numero, segundo_numero):
    return primeiro_numero * segundo_numero


def dividir(primeiro_numero, segundo_numero):
    """Divide os números. Retorna None se o divisor for zero."""
    if segundo_numero == 0:
        return None
    return primeiro_numero / segundo_numero


def formatar(numero):
    """Remove o '.0' de números inteiros para deixar a saída mais limpa."""
    if numero == int(numero):
        return str(int(numero))
    return str(round(numero, 6))


def main():
    exibir_titulo()

    while True:
        exibir_menu()
        opcao = input("Opção: ").strip()

        if opcao == "0":
            print("\nEncerrando a calculadora. Até logo!")
            break

        if opcao not in ("1", "2", "3", "4"):
            print("\nOpção inválida! Escolha um número entre 0 e 4.")
            continue

        primeiro_numero = ler_numero("Digite o primeiro valor: ")
        segundo_numero = ler_numero("Digite o segundo valor: ")

        if opcao == "1":
            simbolo = "+"
            resultado = somar(primeiro_numero, segundo_numero)
        elif opcao == "2":
            simbolo = "-"
            resultado = subtrair(primeiro_numero, segundo_numero)
        elif opcao == "3":
            simbolo = "*"
            resultado = multiplicar(primeiro_numero, segundo_numero)
        else:
            simbolo = "/"
            resultado = dividir(primeiro_numero, segundo_numero)

        print("\n" + "-" * 40)
        if resultado is None:
            print("Erro: não é possível dividir por zero!")
        else:
            print(f"Cálculo:   {formatar(primeiro_numero)} {simbolo} "
                  f"{formatar(segundo_numero)}")
            print(f"Resultado: {formatar(resultado)}")
        print("-" * 40)


if __name__ == "__main__":
    main()
