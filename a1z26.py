def a1z26(msg):
  msg="".join(msg)
  dcode=[]
  words=msg.split(" ")
  thing=[]
  for word in words:
    thing.append(word.split("-"))
  for l in thing:
    for i in l:
      dcode.append(chr(int(i)+64))
    dcode.append(" ")
  return "".join(dcode)