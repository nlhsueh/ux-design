# BMIv2
print ("Please input weight and height, press -9 to stop")
n = str(input('Please input the name '))
w = float(input('Please input the weight (kg) '))
h = float(input('Please input the height (m) '))
bmi_set = {}

while True:
  bmi = round(w/(h**2), 1)
  bmi_set[n] = bmi
  n = str(input('Please input the name '))
  if (w == -9):
     break
  w = float(input('Please input the weight (公斤) '))
  if (w == -9):
     break
  h = float(input('Please input the height (公尺) '))
  if (h == -9):
     break

print ('------')
for k,v in bmi_set.items():
 print ('The BMI of {} is {}'.format(k, v))