montant_initial= float(input("Entrez votre montant: "))
taux= float(input("le taux en pourcentage"))
gain_annuel = montant_initial * (taux/ 100)
print( f"montant initial : {montant_initial} euros")
print(f"taux : {taux}%")
print(f"gain annuel : {gain_annuel :.2f} euros")
capital=5000
montant_initial += capital
taux_augmenté=2
taux += taux_augmenté
gain_annuel_nouveau=montant_initial*(taux/100)
print(f"augmentation capital et taux:")
print(f"montant initial:{montant_initial}euros")
print ( f"taux:{taux}%")
print(f"nouveau gain:{gain_annuel_nouveau:.2f}euros")
retrait=0.1*montant_initial
montant_initial-=retrait
taux_diminué=1
taux-=taux_diminué
montant_final=montant_initial*(1+taux/100)
print(f"diminution du taux :")
print(f"montant final:{montant_final:.2f}euros")
print(f"taux :{taux}%")