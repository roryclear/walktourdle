import pyemoji
print("making form? 🇳🇪")

with open('flags.txt', 'r') as file:
    data = file.read().replace('\n', '')
print(data)

arr = []
while "data-src" in data:
    data = data[data.index("data-src")+1:]
    data = data[data.index(">")+1:]
    #flag = data[0:2]
    data = data[data.index("Flag:")+6:]
    name = data[:data.index("<")]
    #print(name,flag)
    #print(f"<option value=\"{name}{flag}\">")
    arr.append(f"<option value=\"{name}\">")
arr = sorted(arr)
print(arr)
for a in arr: print(a)
print(len(arr))