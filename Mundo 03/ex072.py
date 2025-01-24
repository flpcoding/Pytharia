numerosPorExtenso: tuple[str] = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numeroDigitado = int(input('Digite um número entre 0 e 20: '))

while True:
    if numeroDigitado >= 0 and numeroDigitado <= 20:
        print(f'O número digita por extenso é: {numerosPorExtenso[numeroDigitado]}') 
        break
    numeroDigitado = int(input('Número inválido, informe outro valor: '))
