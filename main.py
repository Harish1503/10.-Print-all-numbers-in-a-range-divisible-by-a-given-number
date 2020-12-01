lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))
n = int(input("Enter the number to be divided by: "))
for number in range(lower, upper+1):
  if(number%n==0):
    print(number)