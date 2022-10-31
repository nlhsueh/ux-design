# BMIv3 簡化與統一
print ("Please input weight and height, press -9 to stop")
bmi_set = {}

while True:
  n = str(input('Please input the name '))
  if (n == '-9'):
     break   
  w = float(input('Please input the weight (kg) '))
  if (w == -9):
     break
  h = float(input('Please input the height (m) '))
  if (h == -9):
     break
  bmi = round(w/(h**2), 1)
  bmi_set[n] = bmi

print ('------')
for k,v in bmi_set.items():
 print ('The BMI of {} is {}'.format(k, v))

