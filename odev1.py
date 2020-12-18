import re
mail = "ali.erbey@usak.edu.tr"
result = re.findall("^[a-z.a-z]+@+usak\.edu\.tr$",mail)

if(result):
    print("Bu bir mail adresidir.")
else:
    print("bu mail adresi değildir.")
