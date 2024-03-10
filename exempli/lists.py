unknown_elements = []
known_elements = ['oxygen', 'sodium', 'carbon', 'hydrogen']
elements = input('What elements do you know? ').split() # splits x in parenthessi
for element in elements:
    if element not in known_elements:
        unknown_elements.append(element)
print(f"I don\'t know {', '.join(unknown_elements[:-1])} and {unknown_elements[-1]}")
