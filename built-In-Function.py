# String built in methods usecase

message = "corona vaccine is ready to use, most of them are more than 90% effective"
print(message)
print(message)

print(message.find("are"))  # it gives the starting index no of the word in our sentence

seq1 = ("1320", "168", "40", "90")
print("._".join(seq1))

seq1 = ["1320", "168", "40", "90", "34"]
seq1.append("new number")
print(seq1)
seq1.extend(["7514", "754dww6"])
print(seq1)

seq1.insert(2, "juju")
print(seq1)

print(seq1.pop())
print(seq1)

seq1.pop(3)
print(seq1)
