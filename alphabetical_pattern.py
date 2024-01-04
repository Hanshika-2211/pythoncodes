start = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
n = int(input("Enter the range: "))

for i in range(n):
    for j in range(i + 1):
        to_print = start[i]
        print(to_print, end=" ")
    
    print()