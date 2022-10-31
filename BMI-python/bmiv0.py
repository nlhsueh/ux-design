w = input('Please input the weight ')
h = input('Please input the height ')
bmi_set = []
while w != -999 and h != -999:
 bmi = w/(h*h)
 bmi_set.add(bmi)
for b in bmi_set:
 print (b)
