
produit="steak"
prix_unitaire=10.01
stock=20
print(f"Produit: {produit} \n Prix unitaire: {prix_unitaire} \n stock {stock}")
quantite_ajoutee = int(input("Entrez la quantité de produits à ajouter en stock : "))
stock += quantite_ajoutee
print(f'stock: {stock}')
prix_unitaire *= 1.1
print("\nInformations mises à jour du produit après ajout en stock et augmentation de prix")
print(f"Nom du produit : {produit}")
print(f"Prix unitaire : {prix_unitaire:.2f} euros") 
print(f"Quantité: {stock}")