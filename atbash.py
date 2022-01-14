def atbash(msg):
  dcode=[]
  for item in msg:
    if ord(item)>96 and ord(item)<123:
      dcode.append(chr(219-ord(item)))
    else:
      dcode.append(item)
  return ("".join(dcode)).upper()