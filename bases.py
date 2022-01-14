def bases(msg):
  msg=("".join(msg)).split(" ")
  base_no=int(input("Enter number base: "))
  dcode=[]
  for i in msg:
    dcode.append(chr(int(i, base=base_no)))
  decoded=("".join(dcode)).upper()
  return decoded