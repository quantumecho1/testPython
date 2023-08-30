# Beschreibender Charakter, Länge und Klarheit verletzt
def F():
    print('\n' * 10)
F()

# Abstraktion, Klarheit und PEP8 verletzt (CamelCase für Variablen)
SFName="Keeley"
SLName="Gould"
h=SFName+" "+SLName

# PEP8 verletzt (Leerzeichen fehlen)
print(h)
print(SLName+",\t\n",SFName)
print(SLName+"\t"+SFName)
print()

# Klarheit und Beschreibender Charakter verletzt
print("A says hi!")

# Klarheit, Länge und PEP8 verletzt (CamelCase und kurze Namen)
B1="NealeMcMillan"

# PEP8 verletzt (Leerzeichen fehlen)
print(B1)
print(B1.upper())
print()

# Klarheit und Abstraktion verletzt
B2="Class X"

# PEP8 verletzt (Leerzeichen fehlen)
print(B2)
print(B2.center(35,"-"))

# Abstraktion und Klarheit verletzt, PEP8 verletzt (Variable mit reserviertem Wortnamen)
str="h\tw"
print(str)
print(str.expandtabs(tabsize=15))

# PEP8 verletzt (Leerzeichen fehlen)
print(B2[0:1])
print(B2[0:2])
print(B2[0:3])
print(B2[0:4])

# Klarheit verletzt
ti = r'c:\trash'
print(ti)

# Länge und Klarheit verletzt
x=2
