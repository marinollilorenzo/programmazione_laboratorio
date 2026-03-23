nums = [i for i in range(1,1001)]
string = "Stringa per l'esercizio pratico di list comprehension."


print([n for n in nums if n%8 == 0], "\n\n\n")

print([n for n in nums if "6" in str(n)], "\n\n\n")

print(len([s for s in string if s == " "]), "\n\n\n")

print("".join([s for s in string if not s in "aeiou"]), "\n\n\n")

print([parola for parola in string.split(" ") if len(parola) < 5], "\n\n\n")

print({x for x in nums for div in range(2,10) if x % div == 0}, "\n\n\n")

print([x for x in nums if any(x % div == 0 for div in range(2,10))], "\n\n\n")
