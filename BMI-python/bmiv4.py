# BMIv4 範圍防呆
print ("Please input weight and height, press -9 to stop")
bmi_set = {}

while True:
  n = str(input('Please input the name '))
  if (n == '-9'):
      break   
  w = float(input('Please input the weight (kg) '))
  if (w == -9):
      break
  elif (w>500 or w<10):
      print ('Weight should be in the range (10, 500), please re-input ')
      continue
  h = float(input('Please input the height (m) '))
  if (h == -9):
      break
  elif (h>2.2 or h <1):
      print ('Height should be in the range (1, 2.2), please re-input ')
      continue

  bmi = round(w/(h**2), 1)
  bmi_set[n] = bmi

print ('------')
for k,v in bmi_set.items():
 print ('The BMI of {} is {}'.format(k, v))

