# ALUNO1: Edward A. Fernandes N6247G8     
         
# LPA e IPE                               
# Prof.Eliane
#CC2A39                             

#variáveis
branco =0
branco_pref =0
nulo =0
nulo_pref =0
psb =0
pdb =0
falta =0
pa =0
pb =0
maior =0
maior_pref =0
va =0
vb =0
vc =0
vd =0
ve =0
vf =0
vg =0
ele = 1
eltr=int(input("Quantos eleitores no total?"))

while (ele <= eltr):       
   print(f"Eleição para Prefeito e Vereador. Olá, eleitor {ele},continue para")
   print(" exercer seu direito de voto.")
   print("Nesse momento, está em aberto os cargos políticos dos partidos:")
   print("PSB: ")
   print(" 01 - CANDIDATO PREFEITO 1")
   print("      20 - Candidato vereador A")
   print("      21 - Candidato vereador B")
   print("      22 - Candidato vereador C")
   print("PDB: ")
   print(" 02 - CANDIDATO PREFEITO 2")
   print("      23 - Candidato vereador D")
   print("      24 - Candidato vereador E")
   print("      25 - Candidato vereador F")
   print("      26 - Candidato vereador G")
   print("Para votar em branco digite: 10")
   print("Para anular o voto digite: 11")
   print("OBS: Caso o eleitor não tenha comparecido, digitar zero")
   voto=int(input("Escreva o respectivo número do seu (sua) vereador(a)"))
   votop=int(input("Escreva o respectivo número do seu (sua) prefeito (a)"))

   ele+=1
#votos vereador
   if (voto==0):
      falta+=1
   elif (voto==10):
      branco+=1
   elif (voto==11):
      nulo+=1
   elif(voto==20):
      psb+=1
      va+=1
   elif(voto==21):
      psb+=1
      vb+=1
   elif(voto==22):
      psb+=1
      vc+=1
   elif(voto==23):
      pdb+=1
      vd+=1  
   elif(voto==24):
      pdb+=1
      ve+=1
   elif(voto==25):
      pdb+=1
      vf+=1
   elif(voto==26):
      pdb+=1
      vg+=1
   else:
      print("Número inválido !!!")
      ele-=1   
#voto prefeito
   if(votop==10):
      branco_pref+=1
   elif(votop==11):
      nulo_pref+=1
   elif(votop==1):
      pa+=1
      psb+=1   
   elif(votop==2):
      pb+=1
      pdb+=1                 
   elif(votop==0):
      falta+=1
   else:
      print("Número inválido !!!")
      ele-=1
#candidatos mais votados(vereador)
maior = va
ver="Candidato A"
if (vb>va):
   maior = vb
   ver="Candidato B"    
elif (vc>vb):
   maior = vc
   ver="Candidato C"
elif (vd>vc):
   maior = vd
   ver="Candidato D"
elif (ve>vd):
   maior = ve
   ver="Candidato E"
elif (vf>ve):
   maior = vf
   ver="Candidato F"
elif (vg>vf):
   maior = vg
   ver="Candidato G"
#candidato mais votado(prefeito)
maior_pref=pa
pref=("Candidato 1")
if (pb>pa):
   maior_pref=pb
   pref=("Candidato 2")

print(f"Números de votos para o partido PSB {psb}")
print(f"Números de votos para o partido PDB {pdb}")
print(f"Números de votos para o Candidato A {va}")
print(f"Números de votos para o Candidato B {vb}")
print(f"Números de votos para o Candidato C {vc}")
print(f"Números de votos para o Candidato D {vd}")
print(f"Números de votos para o Candidato E {ve}")
print(f"Números de votos para o Candidato F {vf}")
print(f"Números de votos para o Candidato G {vg}")
print(f"Votos em Branco para vereador {branco}")
print(f"Votos nulos para vereador {nulo}")
print(f"Votos em Branco para prefeito {branco_pref}")
print(f"Votos nulos para prefeito  {nulo_pref}")
print(f"Maior número de votos para vereador(a):  {ver}, com {maior} votos.")
print(f"Maior número de votos para prefeito(a):  {pref}, com {maior_pref} votos.")   
