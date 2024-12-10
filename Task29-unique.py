# pro vstup Shrek Transformers WhiteChrismas
#print("Shrek Transformers WhiteChrismas")
# pro vstup Shrek Shrek Shrek
#print("Shrek")
# pro vstup 5 3 3
#print("{'5', '3'}")
import sys
print({sys.argv[1],sys.argv[2],sys.argv[3]})
#Alternativa
unikatni_hodnoty = set()
unikatni_hodnoty.add(sys.argv[1])
unikatni_hodnoty.add(sys.argv[2])
unikatni_hodnoty.add(sys.argv[3])
print(unikatni_hodnoty)
#Alternativa
filmy = set(sys.argv[1:])
print(filmy)