# tally the models of cars driven

tally = {}
model = input("Enter car model: ")
while model:
    if model in tally:
        tally[model] += 1
    else:
        tally[model] = 1
    model = input("Enter car model: ")
print(tally)
print()
for model in tally:  ## when interating through a dictionary we iterate over the keys
    print(f"{model} was seen {tally[model]} times.")
