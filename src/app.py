anual_sal = float(input("Renda anual com salário: "))
anual_serv = float(input("Renda anual com prestação de serviço: "))
anual_cap = float(input("Renda anual com ganho de capital: "))
gastos_med = float(input("Gastos médicos: "))
gastos_edu = float(input("Gastos educacionais: "))

porcent = 0.0

sal = anual_sal / 12

if sal >= 3000.00 and sal < 5000.00:
    porcent = 0.1
elif sal >= 5000.00:
    porcent = 0.2
elif sal < 3000.00:
    porcent = 0

imp_sal = anual_sal * porcent if sal >= 3000.00 else 0.00

imp_serv = 0.15 * anual_serv if anual_serv > 0.0 else 0.00

imp_cap = 0.2 * anual_cap if anual_cap > 0.0 else 0.00

imp_bruto = imp_sal + imp_serv + imp_cap

max_dedut = imp_bruto * 0.3

dedut = gastos_med + gastos_edu

abat = max_dedut if dedut > max_dedut else dedut

print("RELATÓRIO DE IMPOSTO DE RENDA")
print()
print("CONSOLIDADO DE RENDA")
print(f"Imposto sobre salário: {imp_sal:.2f}")
print(f"Imposto sobre serviços: {imp_serv:.2f}")
print(f"Imposto sobre ganho de capital: {imp_cap:.2f}")
print()
print("DEDUÇÕES")
print(f"Máximo dedutível: {max_dedut:.2f}")
print(f"Gastos dedutíveis: {dedut:.2f}")
print()
print("RESUMO")
print(f"Imposto bruto total: {imp_bruto:.2f}")
print(f"Abatimento: {abat:.2f}")
print(f"Imposto devido: {imp_bruto - abat:.2f}")
