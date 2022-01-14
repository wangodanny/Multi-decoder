def caesar(msg):
  key=int(input("Enter Caesar shift: "))
  dcode=[]
  for item in msg:
    if ord(item)>96 and ord(item)<123:
      thing=ord(item)-key
      if thing<97:
        thing+=26
      dcode.append(chr(thing))
    else:
      dcode.append(item)
  return ("".join(dcode)).upper()
