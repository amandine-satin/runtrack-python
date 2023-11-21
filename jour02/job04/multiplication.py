N=int(input("Entrez un entier superieur à zero (N)"))
print(N)
if N>0:
    for i in range (1,N +1):
       print(f"table de multiplicationde {i}:") 
       for j in range (1,11):
           print(f"{i}x{j}={i*j}")
           print()

           
       