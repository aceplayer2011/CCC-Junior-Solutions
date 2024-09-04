v=['a', 'e', 'i', 'o', 'u', 'y']
c=['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']

q = False
while q == False:
  a = input()
  if a == "quit!":
    break
  if 4 < len(a):
    if a[-3] in c:
      if a[-2] == v[3]:
        if a[-1] == c[13]:
          for i in range(0, len(a)- 2):
            print (a[i], end = "")
          print('our')
        else:
          print(a)
      else:
        print(a)
    else:
      print(a)
  else:
   print(a)