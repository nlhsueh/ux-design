# BMIv1
print ("Please input weight and height, -999 to stop")
w = input('Please input the weight (kg) ')
h = input('Please input the height (m) ')
w, h = float(w), float(h)
bmi_set = []
while w != -999 and h != -999:
  bmi = round(w/(h*h),1)
  bmi_set.append(bmi)
  w = float(input('Please input the weight (kg) '))
  h = float(input('Please input the height (m) '))

for b in bmi_set:
 print ('BMI:', b)
