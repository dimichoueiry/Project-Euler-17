import inflect

p = inflect.engine()
MyNumber = []
addition = 0

def num_word(number):
   return p.number_to_words(number)

for i in range(1, 1001):
    replcd = num_word(i).replace(" ", "")
    MyNumber.append(replcd.replace("-", ""))

for i in MyNumber:
    i
    addition += len(i)

print(addition)