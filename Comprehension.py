lista = []
for i in range(1, 11):
    lista.append(i)

print(lista)

lista_comp = [i for i in range(1, 11)]
print(lista_comp)

# lista contenente i numeri interi compresi tra 1 e 10 inclusi, tutti moltiplicati per 2
lista_doppi = [ i*2 for i in range(1, 11)]
# lista contenente i quadrati dei numeri interi compresi tra 1 e 10 inclusi
lista_quadrati = [ i*i for i in range(1, 11)]
# lista contenente i cubi dei numeri interi compresi tra 1 e 10 inclusi
lista_cubi = [ i**3 for i in range(1, 11)]
# lista contenente la tabellina del 3
lista_tab_3 = [ i for i in range(3, 31, 3)]