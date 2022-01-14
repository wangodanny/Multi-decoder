from caesar import caesar
from atbash import atbash
from a1z26 import a1z26
from vigenere import vigenere
from bases import bases
from Engima import enigma

method_list={
  "1":atbash,
  "2":caesar,
  "3":a1z26,
  "4":vigenere,
  "5":bases,
  "6"
}

print("Enter decryption method(s), use spaces to separate methdos in parallel, and '-' to separate methods in series:")
print("    1: Atbash cipher")
print("    2: Caesar cipher")
print("    3: A1Z26")
print("    4: Vigenere")
print("    5: Number bases")
methods=input("> ").split(" ")
message=list(input("Enter message: ").lower())
for bit in methods:
  print("For method "+bit)
  series=bit.split("-")
  message_copy=message
  for i in series:
    message_copy=list(method_list[i](message_copy).lower())
  decoded=("".join(message_copy)).upper()
  print("Decoded message is: "+decoded+"\n")