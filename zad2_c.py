text_input = input("Wpisz tekst")

words_to_remove = ["się", "i", "oraz", "nigdy", "dlaczego"]

# for word in words_to_remove:
#     text_input = text_input.replace(word, "")

print(text_input)

words_to_replace = {"i": "oraz", "oraz": "i", "nigdy": "prawie nigdy", "dlaczego": "czemu"}

input_table = text_input.split()
replaced_table = input_table[:]

for word in words_to_replace.keys():
    for idx, element in enumerate(replaced_table):
        if element in words_to_replace.keys() and input_table[idx] == element:
            print(element)
            replaced_table[idx] = words_to_replace.get(element)

print(" ".join(element for element in replaced_table))
