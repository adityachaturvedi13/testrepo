"""
for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()
    """
"""row=5
for i in range(row):
    for j in range(row-i-1):
        print(" ",end="")
    for k in range(2*i+1):
        print("*",end="")
    print()
for i in range(row-2,-1,-1):
    for j in range(row-i-1):
        print(" ",end="")
    for k in range(2*i+1):
        print("*",end="")
    print()
    
"""

str="python"
i=0
for i in range(str):
    i+=1
    print(i)
