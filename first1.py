
while True:

  print('Simple Calculator is ready for work:')
  num1 = int(input("Enter First no: "))
  num2 = int(input("Enter Second no: "))
  Symbol =  input("Enter Symbol like- +,-,*,/ : " )
  if Symbol == '+':
    print('Ans: ',num1 + num2)
  elif Symbol == '-':
    print('Ans: ',num1-num2)
  elif Symbol == '*':
    print('Ans: ',num1*num2)
  elif Symbol == '/':
    print('Ans: ',num1/num2)
  else:
    print('Wrong Symbol')
