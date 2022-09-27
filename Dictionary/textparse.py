import string
count={}
fname=open("file1.txt")
for line in fname:
    ln=line.rstrip()
    # lin = ln.translate(line.maketrans('', '', string.punctuation))
    lin=ln.lower()
    words=lin.split()
    for word in words:
        if word not in count:
            count[word]=1
        else:
            count[word] += 1
print(count)
    