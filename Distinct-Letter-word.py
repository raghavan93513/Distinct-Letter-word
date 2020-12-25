a = input()
b = []
for i in a:
    if i in b:
        b.append(i)
    else:
        l = -1
if l != -1:
    print("Good")
else:
    print("Bad")