alvo = int(input("Digite um número para encontrar na sequência de Fibonacci: "))

a = 0 
b = 1

print("Sequência de Fibonacci até encontrar o número:", end=' ')
while a <= alvo:
    print(a, end=' ')
    if a == alvo:
        print("\nNúmero encontrado na sequência de Fibonacci!")
        break
    a, b = b, a + b

if a > alvo:
    print("\nNúmero não encontrado na sequência de Fibonacci.")

