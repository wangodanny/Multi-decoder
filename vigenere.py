def vigenere(msg):
  dcode=[]
  key=list(input("Enter Vigenere key: ").lower().replace(" ", ""))
  lenMsg=0
  n=0
  for item in msg:
    if ord(item)>96 and ord(item)<123:
      lenMsg+=1
  while len(key)<lenMsg:
    key.append(key[n%(len(key)-1)])
    n+=1
  i=0
  for item in msg:
    if ord(item)>96 and ord(item)<123:
      new=((ord(item)-96)-(ord(key[i])-96))%26+97
      dcode.append(chr(new).upper())
      i+=1
    else:
      dcode.append(item)
  return "".join(dcode)
    