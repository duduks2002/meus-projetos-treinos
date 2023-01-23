# Disciplina: LPA e IPE 
# Professor: Eliane
# Descrição: Programa para analisar o usuário para o seguro desemprego.
# Aluno1: Edward  N6247G8 
# Data atual: "21/09/2020"
#Algoritmo "Seguro-Desemprego"


#Quem tem direito ao beneficio:
   
print("PARA SABER SE VOCÊ ESTÁ QUALIFICADO PARA RECEBER O SEGURO,PRECISAMOS SABER SE")
print("Você é um: \n")
print("A- Trabalhador Formal,em virtude da dispensa sem justa causa,inclusive dispensa indireta;\n")
print("B- Trabalhador Doméstico,em virtude da dispensa sem justa causa,inclusive dispensa indireta;\n")
print("C- Trabalhador Formal com contrato de trabalho suspenso em virtude de participação em curso")
print("ou programa de qualificação profissional oferecido pelo empregador;\n")
print("D- Pescador profissional durante periodo de defeso;\n")
print("E- Trabalhador resgatado da condição semelhante a de escravo.\n")
tipos=input("Tipo de trabalhador: ")
if (tipos == "a") or(tipos== "A"): 
         print("=====Analisando se você pode receber o beneficio=====")
elif (tipos=="b")or(tipos=="B"): 
         print("=====Analisando se você pode receber o beneficio=====")
elif (tipos=="c")or(tipos=="C"): 
         print("=====Analisando se você pode receber o beneficio=====")
elif (tipos=="d")or(tipos=="D"): 
         print("=====Analisando se você pode receber o beneficio=====")
elif (tipos=="e")or(tipos=="E"): 
         print("=====Analisando se você pode receber o beneficio=====")
else:
         print("<><><><><><><>Você não pode receber o beneficio<><><><><><><>")

#//Condições para receber o beneficio:
   
if (tipos =="a")or(tipos=="A"): 
      print(" Responda as perguntas com S para sim e N para não!\n")
      r1=input("Você foi dispensado SEM justa causa?\n")
      r2=input("Você recebeu salários de pessoa jurídica/física,no periodo de 6 meses consecutivos,imediatamente anteriores à data de dispensa?\n")
      r3=input("Esta desempregado neste momento?\n")
      r4=input("possui renda própria de qualquer natureza suficiente à sua manutenção e a de sua familia?\n")
      r5=input("Está em gozo de qualquer benefício previdenciário de prestação continuada?(exceção do auxílio-acidente e pensão por morte)\n")
      r6=input("Foi empregado de pessoa jurídica ou de pessoa física equiparada à jurídica,pelo menos 12 meses nos últimos 36 meses que antecedem a data de dispensa?\n")
      print("suas resposta foram:", r1, r2, r3, r4, r5, r6)

elif (tipos =="b")or(tipos=="B"):
      print(" Responda as perguntas com S para sim e N para não !\n")
      r1=input("Você foi dispensado SEM justa causa?\n")    
      r2=input("Você trabalhou,EXCLUSIVAMENTE,como empregado doméstico,pelo período mínimo de 15 meses nos últimos 24 meses que antecederam a data de dispensa que deu origem ao requerimento do Seguro-Desemprego?\n")     
      r3=input("possui renda própria de qualquer natureza suficiente à sua manutenção e a de sua familia?\n")      
      r4=input("Está em gozo de qualquer benefício previdenciário de prestação continuada?(exceção do auxílio-acidente e pensão por morte)\n")
      print("Suas respostas foram:",r1, r2, r3, r4) 

elif (tipos =="c")or(tipos=="C"):

      print(" Responda as perguntas com S para sim e N para não!\n") 
      r1=input("Está com o contrato de trabalho suspenso?\n")
      r2=input("Foi matriculado em um curso ou programa de qualificação profissional,oferecido pelo empregador?\n") 
      r3=input("Esta desempregado neste momento?\n")
      r4=input("possui renda própria de qualquer natureza suficiente à sua manutenção e a de sua familia?\n") 
      r5=input("Está em gozo de qualquer benefício previdenciário de prestação continuada?(exceção do auxílio-acidente e pensão por morte)\n") 
      print("suas resposta foram:", r1, r2, r3, r4, r5)

elif (tipos =="d")or(tipos=="D"):

      print(" Responda as perguntas com S para sim e N para não !\n")
      r1=input("Possui inscrição no INSS como segurado especial?\n")
      r2=input("Possui comprovação de venda do pescado a adquirente pessoa jurídica/cooperativa,no período correspondente aos últimos 12 meses que antecederam ao início do defeso?\n") 
      r3=input("Está em gozo de qualquer benefício de prestação continuada da Previdência Social ou da Assistência Social?(exceção do auxílio-acidente e pensão por morte)\n") 
      r4=input("Tem como comprovar o exercício profissional da atividade de pesca artesanal objeto do defeso e dedicou à pesca,em caráter ininterrupto,durante o período compreendido entre o defeso anterior e o em curso?\n") 
      r5=input("Contém vínculo de emprego ou outra relação de trabalho ou outra fonte de renda diversa da decorrente da atividade pesqueira?\n")
      print("suas resposta foram:", r1, r2, r3, r4, r5)              

elif (tipos =="e")or(tipos=="E"):

      print(" Responda as perguntas com S para sim e N para não !\n")  
      r1=input("Foi comprovadamente resgatado do regime de terabalho forçado ou da condição análoga a de escravo em decorrência de ação de fiscalização do MTE?\n")   
      r2=input("Está em gozo de qualquer benefício previdenciário de prestação continuada?(exceção do auxílio-acidente e pensão por morte)\n")   
      r3=input("possui renda própria de qualquer natureza suficiente à sua manutenção e a de sua familia?\n")   
      print("suas resposta foram:", r1, r2, r3) 
 
#/////parcelas e Cálculo do Benefício::
  
if (tipos=="A")or(tipos=="a"):
      
      if ((r1=="s")or(r1=="S")) and((r2=="s")or(r2=="S")) and((r3=="s")or (r3=="S")) and((r4=="n")or(r4=="N")) and((r5=="n")or(r5=="N"))and ((r6=="s")or(r6=="S")):

            print("<><><><><><>CALCULANDO PARCELAS...<><><><><><>\n")
            print("======Em Qual destes você se aplica?=====\n")
            print("A- (COMPROVAR)Vínculo empregatácio de no mínimo 6 meses e no máximo 11 meses,nos últimos 36 meses;\n")
            print("B- (COMPROVAR)Vínculo empregatácio de no mínimo 12 meses e no máximo 23 meses,nos últimos 36 meses;\n")
            print("C- (COMPROVAR)Vínculo empregatácio de no mínimo 24 meses,nos últimos 36 meses;\n")
            parcela= input("R: ")
            
            if ((parcela=="a")or(parcela=="A")):

                  print("<><><><><>ETAPA FINAL<><><><><>\n")
                  us=float(input("Salário do ultimo mês.....:R$\n"))
                  ps=float(input("Salário do penúltimo mês.....:R$\n"))
                  aps=float(input("Salário do antepenúltimo mês.....:R$\n"))

                  ms=(us+ps+aps)/3
                  print(f"Média Salarial de R$ {ms}")
                  print("Total de parcelas= 3 ")
                  if (ms>2038.15):
                        beneficio= 1385.91                             
                  if (ms<=1222.77):
                        beneficio=ms*0.8
                        if(beneficio<1045.00):
                              beneficio=1045.00
                  elif (ms>=1222.78) and (ms<=2038.15):
                        beneficio=ms*0.5 + 978.22

                  print(f"Valor do beneficio = R${beneficio}")       
            
            elif ((parcela=="b")or(parcela=="B")):

                  print("<><><><><>ETAPA FINAL<><><><><>\n")
                  us=float(input("Salário do ultimo mês.....:R$\n"))
                  ps=float(input("Salário do penúltimo mês.....:R$\n"))
                  aps=float(input("Salário do antepenúltimo mês.....:R$\n"))

                  ms=(us+ps+aps)/3
                  print(f"Média Salarial de R$ {ms}")
                  print("Total de parcelas= 4 ")
                  if (ms>2038.15):
                        beneficio= 1385.91                             
                  if (ms<=1222.77):
                        beneficio=ms*0.8
                        if(beneficio<1045.00):
                              beneficio=1045.00
                  elif (ms>=1222.78) and (ms<=2038.15):
                        beneficio=ms*0.5 + 978.22

                  print(f"Valor do beneficio = R${beneficio}")     

            elif ((parcela=="c")or(parcela=="C")):

                  print("<><><><><>ETAPA FINAL<><><><><>\n")
                  us=float(input("Salário do ultimo mês.....:R$\n"))
                  ps=float(input("Salário do penúltimo mês.....:R$\n"))
                  aps=float(input("Salário do antepenúltimo mês.....:R$\n"))

                  ms=(us+ps+aps)/3
                  print(f"Média Salarial de R$ {ms}")
                  print("Total de parcelas= 5 ")
                  if (ms>2038.15):
                        beneficio= 1385.91                             
                  if (ms<=1222.77):
                        beneficio=ms*0.8
                        if(beneficio<1045.00):
                              beneficio=1045.00
                  elif (ms>=1222.78) and (ms<=2038.15):
                        beneficio=ms*0.5 + 978.22

                  print(f"Valor do beneficio = R${beneficio}")

            else:
                  print("<><><><><><><><><><>BENEFÍCIO NEGADO<><><><><><><><><><>")
      
      
      else:

            print("<><><><><><><><><><>BENEFÍCIO NEGADO<><><><><><><><><><>")

elif (tipos=="B")or(tipos=="b"):

      if((r1=="s")or(r1=="S")) and((r2=="s")or(r2=="S")) and((r3=="n")or (r3=="N")) and((r4=="n")or(r4=="N")):

            print("<><><><><><>CALCULANDO PARCELAS...<><><><><><>\n")
            print("======Em Qual destes você se aplica?=====\n")
            print("A- (COMPROVAR)Vínculo empregatácio de no mínimo 6 meses e no máximo 11 meses,nos últimos 36 meses;\n")
            print("B- (COMPROVAR)Vínculo empregatácio de no mínimo 12 meses e no máximo 23 meses,nos últimos 36 meses;\n")
            print("C- (COMPROVAR)Vínculo empregatácio de no mínimo 24 meses,nos últimos 36 meses;\n")
            parcela= input("R: ")

            if ((parcela=="a")or(parcela=="A")):

                  print("<><><><><>ETAPA FINAL<><><><><>\n")
                  us=float(input("Salário do ultimo mês.....:R$\n"))
                  ps=float(input("Salário do penúltimo mês.....:R$\n"))
                  aps=float(input("Salário do antepenúltimo mês.....:R$\n"))

                  ms=(us+ps+aps)/3
                  print(f"Média Salarial de R$ {ms}")
                  print("Total de parcelas= 3 ")
                  if (ms>2038.15):
                        beneficio= 1385.91                             
                  if (ms<=1222.77):
                        beneficio=ms*0.8
                        if(beneficio<1045.00):
                              beneficio=1045.00
                  elif (ms>=1222.78) and (ms<=2038.15):
                        beneficio=ms*0.5 + 978.22

                  print(f"Valor do beneficio = R${beneficio}")
            
            elif ((parcela=="b")or(parcela=="B")):

                  print("<><><><><>ETAPA FINAL<><><><><>\n")
                  us=float(input("Salário do ultimo mês.....:R$\n"))
                  ps=float(input("Salário do penúltimo mês.....:R$\n"))
                  aps=float(input("Salário do antepenúltimo mês.....:R$\n"))

                  ms=(us+ps+aps)/3
                  print(f"Média Salarial de R$ {ms}")
                  print("Total de parcelas= 4 ")
                  if (ms>2038.15):
                        beneficio= 1385.91                             
                  if (ms<=1222.77):
                        beneficio=ms*0.8
                        if(beneficio<1045.00):
                              beneficio=1045.00
                  elif (ms>=1222.78) and (ms<=2038.15):
                        beneficio=ms*0.5 + 978.22

                  print(f"Valor do beneficio = R${beneficio}")     

            elif ((parcela=="c")or(parcela=="C")):

                  print("<><><><><>ETAPA FINAL<><><><><>\n")
                  us=float(input("Salário do ultimo mês.....:R$\n"))
                  ps=float(input("Salário do penúltimo mês.....:R$\n"))
                  aps=float(input("Salário do antepenúltimo mês.....:R$\n"))

                  ms=(us+ps+aps)/3
                  print(f"Média Salarial de R$ {ms}")
                  print("Total de parcelas= 5 ")
                  if (ms>2038.15):
                        beneficio= 1385.91                             
                  if (ms<=1222.77):
                        beneficio=ms*0.8
                        if(beneficio<1045.00):
                              beneficio=1045.00
                  elif (ms>=1222.78) and (ms<=2038.15):
                        beneficio=ms*0.5 + 978.22

                  print(f"Valor do beneficio = R${beneficio}")

            else:
                  print("<><><><><><><><><><>BENEFÍCIO NEGADO<><><><><><><><><><>")
      else:

            print("<><><><><><><><><><>BENEFÍCIO NEGADO<><><><><><><><><><>")

elif (tipos=="C")or(tipos=="c"):

      if((r1=="s")or(r1=="S")) and((r2=="s")or(r2=="S")) and((r3=="s")or (r3=="S")) and((r4=="n")or(r4=="N")) and((r5=="n")or(r5=="N")):

            print("<><><><><><>CALCULANDO PARCELAS...<><><><><><>\n")
            print("======Em Qual destes você se aplica?=====\n")
            print("A- (COMPROVAR)Vínculo empregatácio de no mínimo 6 meses e no máximo 11 meses,nos últimos 36 meses;\n")
            print("B- (COMPROVAR)Vínculo empregatácio de no mínimo 12 meses e no máximo 23 meses,nos últimos 36 meses;\n")
            print("C- (COMPROVAR)Vínculo empregatácio de no mínimo 24 meses,nos últimos 36 meses;\n")
            parcela= input("R: ")

            if ((parcela=="a")or(parcela=="A")):

                  print("<><><><><>ETAPA FINAL<><><><><>\n")
                  us=float(input("Salário do ultimo mês.....:R$\n"))
                  ps=float(input("Salário do penúltimo mês.....:R$\n"))
                  aps=float(input("Salário do antepenúltimo mês.....:R$\n"))

                  ms=(us+ps+aps)/3
                  print(f"Média Salarial de R$ {ms}")
                  print("Total de parcelas= 3 ")
                  if (ms>2038.15):
                        beneficio= 1385.91                             
                  if (ms<=1222.77):
                        beneficio=ms*0.8
                        if(beneficio<1045.00):
                              beneficio=1045.00
                  elif (ms>=1222.78) and (ms<=2038.15):
                        beneficio=ms*0.5 + 978.22

                  print(f"Valor do beneficio = R${beneficio}")
            
            elif ((parcela=="b")or(parcela=="B")):

                  print("<><><><><>ETAPA FINAL<><><><><>\n")
                  us=float(input("Salário do ultimo mês.....:R$\n"))
                  ps=float(input("Salário do penúltimo mês.....:R$\n"))
                  aps=float(input("Salário do antepenúltimo mês.....:R$\n"))

                  ms=(us+ps+aps)/3
                  print(f"Média Salarial de R$ {ms}")
                  print("Total de parcelas= 4 ")
                  if (ms>2038.15):
                        beneficio= 1385.91                             
                  if (ms<=1222.77):
                        beneficio=ms*0.8
                        if(beneficio<1045.00):
                              beneficio=1045.00
                  elif (ms>=1222.78) and (ms<=2038.15):
                        beneficio=ms*0.5 + 978.22

                  print(f"Valor do beneficio = R${beneficio}")     

            elif ((parcela=="c")or(parcela=="C")):

                  print("<><><><><>ETAPA FINAL<><><><><>\n")
                  us=float(input("Salário do ultimo mês.....:R$\n"))
                  ps=float(input("Salário do penúltimo mês.....:R$\n"))
                  aps=float(input("Salário do antepenúltimo mês.....:R$\n"))

                  ms=(us+ps+aps)/3
                  print(f"Média Salarial de R$ {ms}")
                  print("Total de parcelas= 5 ")
                  if (ms>2038.15):
                        beneficio= 1385.91                             
                  if (ms<=1222.77):
                        beneficio=ms*0.8
                        if(beneficio<1045.00):
                              beneficio=1045.00
                  elif (ms>=1222.78) and (ms<=2038.15):
                        beneficio=ms*0.5 + 978.22

                  print(f"Valor do beneficio = R${beneficio}")

            else:
                  print("<><><><><><><><><><>BENEFÍCIO NEGADO<><><><><><><><><><>")
      else:
            print("<><><><><><><><><><>BENEFÍCIO NEGADO<><><><><><><><><><>")

elif (tipos=="D")or(tipos=="d"):

      if((r1=="s")or(r1=="S")) and((r2=="s")or(r2=="S")) and((r3=="n")or (r3=="N")) and((r4=="s")or(r4=="S")) and((r5=="n")or(r5=="N")):

            print("<><><><><><>CALCULANDO PARCELAS...<><><><><><>\n")
            print("======Em Qual destes você se aplica?=====\n")
            print("A- (COMPROVAR)Vínculo empregatácio de no mínimo 6 meses e no máximo 11 meses,nos últimos 36 meses;\n")
            print("B- (COMPROVAR)Vínculo empregatácio de no mínimo 12 meses e no máximo 23 meses,nos últimos 36 meses;\n")
            print("C- (COMPROVAR)Vínculo empregatácio de no mínimo 24 meses,nos últimos 36 meses;\n")
            parcela= input("R: ")
            if ((parcela=="a")or(parcela=="A")):

                  print("<><><><><>ETAPA FINAL<><><><><>\n")
                  us=float(input("Salário do ultimo mês.....:R$\n"))
                  ps=float(input("Salário do penúltimo mês.....:R$\n"))
                  aps=float(input("Salário do antepenúltimo mês.....:R$\n"))

                  ms=(us+ps+aps)/3
                  print(f"Média Salarial de R$ {ms}")
                  print("Total de parcelas= 3 ")
                  if (ms>2038.15):
                        beneficio= 1385.91                             
                  if (ms<=1222.77):
                        beneficio=ms*0.8
                        if(beneficio<1045.00):
                              beneficio=1045.00
                  elif (ms>=1222.78) and (ms<=2038.15):
                        beneficio=ms*0.5 + 978.22

                  print(f"Valor do beneficio = R${beneficio}")
            
            elif ((parcela=="b")or(parcela=="B")):

                  print("<><><><><>ETAPA FINAL<><><><><>\n")
                  us=float(input("Salário do ultimo mês.....:R$\n"))
                  ps=float(input("Salário do penúltimo mês.....:R$\n"))
                  aps=float(input("Salário do antepenúltimo mês.....:R$\n"))

                  ms=(us+ps+aps)/3
                  print(f"Média Salarial de R$ {ms}")
                  print("Total de parcelas= 4 ")
                  if (ms>2038.15):
                        beneficio= 1385.91                             
                  if (ms<=1222.77):
                        beneficio=ms*0.8
                        if(beneficio<1045.00):
                              beneficio=1045.00
                  elif (ms>=1222.78) and (ms<=2038.15):
                        beneficio=ms*0.5 + 978.22

                  print(f"Valor do beneficio = R${beneficio}")     

            elif ((parcela=="c")or(parcela=="C")):

                  print("<><><><><>ETAPA FINAL<><><><><>\n")
                  us=float(input("Salário do ultimo mês.....:R$\n"))
                  ps=float(input("Salário do penúltimo mês.....:R$\n"))
                  aps=float(input("Salário do antepenúltimo mês.....:R$\n"))

                  ms=(us+ps+aps)/3
                  print(f"Média Salarial de R$ {ms}")
                  print("Total de parcelas= 5 ")
                  if (ms>2038.15):
                        beneficio= 1385.91                             
                  if (ms<=1222.77):
                        beneficio=ms*0.8
                        if(beneficio<1045.00):
                              beneficio=1045.00
                  elif (ms>=1222.78) and (ms<=2038.15):
                        beneficio=ms*0.5 + 978.22

                  print(f"Valor do beneficio = R${beneficio}")

            else:
                  print("<><><><><><><><><><>BENEFÍCIO NEGADO<><><><><><><><><><>")      
      else:
            print("<><><><><><><><><><>BENEFÍCIO NEGADO<><><><><><><><><><>")

elif (tipos=="E")or(tipos=="e"):

      if((r1=="s")or(r1=="S")) and((r2=="n")or(r2=="N")) and((r3=="n")or (r3=="N")):

            print("<><><><><><>CALCULANDO PARCELAS...<><><><><><>\n")
            print("======Em Qual destes você se aplica?=====\n")
            print("A- (COMPROVAR)Vínculo empregatácio de no mínimo 6 meses e no máximo 11 meses,nos últimos 36 meses;\n")
            print("B- (COMPROVAR)Vínculo empregatácio de no mínimo 12 meses e no máximo 23 meses,nos últimos 36 meses;\n")
            print("C- (COMPROVAR)Vínculo empregatácio de no mínimo 24 meses,nos últimos 36 meses;\n")
            parcela= input("R: ")
            if ((parcela=="a")or(parcela=="A")):

                  print("<><><><><>ETAPA FINAL<><><><><>\n")
                  us=float(input("Salário do ultimo mês.....:R$\n"))
                  ps=float(input("Salário do penúltimo mês.....:R$\n"))
                  aps=float(input("Salário do antepenúltimo mês.....:R$\n"))

                  ms=(us+ps+aps)/3
                  print(f"Média Salarial de R$ {ms}")
                  print("Total de parcelas= 3 ")
                  if (ms>2038.15):
                        beneficio= 1385.91                             
                  if (ms<=1222.77):
                        beneficio=ms*0.8
                        if(beneficio<1045.00):
                              beneficio=1045.00
                  elif (ms>=1222.78) and (ms<=2038.15):
                        beneficio=ms*0.5 + 978.22

                  print(f"Valor do beneficio = R${beneficio}")
            
            elif ((parcela=="b")or(parcela=="B")):

                  print("<><><><><>ETAPA FINAL<><><><><>\n")
                  us=float(input("Salário do ultimo mês.....:R$\n"))
                  ps=float(input("Salário do penúltimo mês.....:R$\n"))
                  aps=float(input("Salário do antepenúltimo mês.....:R$\n"))

                  ms=(us+ps+aps)/3
                  print(f"Média Salarial de R$ {ms}")
                  print("Total de parcelas= 4 ")
                  if (ms>2038.15):
                        beneficio= 1385.91                             
                  if (ms<=1222.77):
                        beneficio=ms*0.8
                        if(beneficio<1045.00):
                              beneficio=1045.00
                  elif (ms>=1222.78) and (ms<=2038.15):
                        beneficio=ms*0.5 + 978.22

                  print(f"Valor do beneficio = R${beneficio}")     

            elif ((parcela=="c")or(parcela=="C")):

                  print("<><><><><>ETAPA FINAL<><><><><>\n")
                  us=float(input("Salário do ultimo mês.....:R$\n"))
                  ps=float(input("Salário do penúltimo mês.....:R$\n"))
                  aps=float(input("Salário do antepenúltimo mês.....:R$\n"))

                  ms=(us+ps+aps)/3
                  print(f"Média Salarial de R$ {ms}")
                  print("Total de parcelas= 5 ")
                  if (ms>2038.15):
                        beneficio= 1385.91                             
                  if (ms<=1222.77):
                        beneficio=ms*0.8
                        if(beneficio<1045.00):
                              beneficio=1045.00
                  elif (ms>=1222.78) and (ms<=2038.15):
                        beneficio=ms*0.5 + 978.22

                  print(f"Valor do beneficio = R${beneficio}")

            else:
                  print("<><><><><><><><><><>BENEFÍCIO NEGADO<><><><><><><><><><>")
      else:
            print("<><><><><><><><><><>BENEFÍCIO NEGADO<><><><><><><><><><>")
            
