Amount = int(input("Please Enter The Amount Of Withdraw: "))
note_2 = (Amount %100)//50
note_3 = ((Amount %100)%50)//10
print("Notes of 100 pound" ,note_1)
print("Notes of 50 pound" , note_2)
print("Notes of 10 pound" , note_3)