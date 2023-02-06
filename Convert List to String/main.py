List = ["Coding", "is", "Fun", 76, 10]

# Iteration

def List_to_str(L):
    string = ""

    for i in L:
        string += i

    return string

print(List_to_str(List))

# .join method

string = ""
string = string.join(List)

print(string)

# .map method

string = ""
string = string.join(map(str, List))

print(string)
