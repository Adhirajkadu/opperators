amount=int(input("enter amount in multiples of ten: "))

#calculating number of notes
note1=amount//100
note2=(amount%100)//50
note3=((amount%100)%50)//10

print("note of 100 rupees: ",note1)
print("note of 50 rupees: ",note2)
print("note of 10 rupees: ",note3)