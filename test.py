temp = 0
for num in range(101):
  if num%2 == 0:
    if temp%2 == 0:
      print('Boleh')
      temp += 1
    else :
      print('Cemerlang')
      temp += 1     
  else:
    print('SK')