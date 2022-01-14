def enigma(msg):
  rotor1 = int(input("Enter the starting shift for the first rotor: "))

  rotor2 = int(input("Enter the starting shift for the second rotor: "))

  rotor3 = int(input("Enter the starting shift for the third rotor: "))
  text = list(text)
  dcode = []

  rotor1 = 26 - rotor1
  rotor2 = 26 - rotor2
  rotor3 = 26 - rotor3
	for i in range(0, len(text)):
	  dcode.append(encrypt(text[i], rotor1))
		rotor1 -= 1
		if rotor1 < 0:
			rotor2 -= 1
			dcode[i] = (encrypt(text[i], rotor2))
		if rotor2 < 0:
			rotor3 -= 1
			dcode[i] = (encrypt(text[i], rotor3))
		i+=1
	
  return "".join(dcode)
