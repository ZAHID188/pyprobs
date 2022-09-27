# Write code using find() and string slicing  to extract the number
#  at the end of the line below. 
# Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"
pos=text.find(".")
res=text[pos-1:]
# print(float(res))
print(res)

# x='asd'
# y="asda"
# w=x+y
# print(w)


x = "From marquard@uct.ac.za"
print(x[8])
print(x[14:17])

greet = 'Hello Bob'
print(greet.upper())

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])