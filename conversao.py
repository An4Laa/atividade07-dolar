real = float(input("Digite valor em real: "))
dolar = float(input("Digite a cotação atual do dólar: "))
conversao = real/dolar
print(f"""Seu valor em real ( R${real} )
       Na atual cotação do dólar ( ${dolar} ) 
       Equivale a {conversao} dólar.""")