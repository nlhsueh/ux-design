
print ('Welcome to BetterLife BMI System')
bmi_set = {}

while True:
 go = input ('Press G/g to continue input; X/x to stop ')
 if (go == 'X' or go == 'x'):
     break
 elif (go not in ['G', 'g']):   
     continue
 n = str(input('Please input the name '))
 while True:    
     try:
       w = float(input('Please input the weight (kg) '))
     except ValueError:
       print ('Input should be a value, please re-input ')
       continue
     if (w>500 or w<10):
         print ('Weight should be in the range (10, 500), please re-input ')
         continue
     break   
 while True:
     try:   
       h = float(input('Please input the height (m) '))
     except ValueError:
       print ('Input should be a value, please re-input ')
       continue
     if (h > 2.2 or h <1):
         print ('Height should be in the range (1, 2.2), please re-input ')
         continue
     break 
 bmi = round(w/(h**2), 1)
 bmi_set[n] = bmi
 print ('{} with {}kg, {}m and BMI {} is added'.format(n, w, h, bmi))

# Just for test
# bmi_set = {'Nick':20, 'Kelly': 30, 'Jie': 17}

print ('-------------------------------')
print ('   Better Life Health Report   ')
print ('-------------------------------')

normal, over_w, under_w = {}, {}, {}

for k,v in bmi_set.items():
 # print ('The BMI of {} is {}'.format(k, v))
 if (v>= 24):
     over_w[k] = v
 elif (v<= 18.5):
     under_w[k] = v
 else:
   normal[k] = v

if (not over_w and not under_w):
 print ('Every one is good!!')

if (over_w):
 print ('Overweight people, please Exercise ⚽️⚽️!')
 for k,v in over_w.items():
   print ('The BMI of {} is {} '.format(k,v))
 print () 

if (under_w):    
 print ('Under weight people, please Eat more 🍖🍖!')
 for k,v in under_w.items():
   print ('The BMI of {} is {} '.format(k,v))

