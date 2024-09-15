sp = float(67836.43)
rj = float(36678.66)
mg = float(29229.88)
es = float(27165.48)
outros = float(19849.53)

total_mensal = sp + rj + mg + es + outros

sp = (sp*100)/total_mensal
rj = (rj*100)/total_mensal
mg = (mg*100)/total_mensal
es = (es*100)/total_mensal
outros = (outros*100)/total_mensal

percentual_total = sp + rj + mg + es + outros

print("""----------------------
      O percentual de representação mensal de cada estado é: 
      
      São Paulo {:.2f}% 
      Rio de Janeiro {:.2f}%
      Minas Gerais {:.2f}%
      Espirito Santo {:.2f}%
      Outros {:.2f}%
      --------------------------
      O Faturamento total dos Estados é de {:.2f}% """.format(sp,rj,mg,es,outros,percentual_total))

