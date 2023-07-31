# dictionaries

thisdict = {
  "f_name": "bhanu",
  "m_name": "prakash",
  "l_name": "reddy" }
print(thisdict)

#length of dictioanry
print(len(thisdict))

#dictionary type
print(type(thisdict))

# Accessing items
x = thisdict["f_name"]
print(x)

# Get Keys
y = thisdict.keys()   
print(y)

# Update Values
thisdict["l_name"] = "kamjula"

# Add items
thisdict["city"] = "chimakurthy"
print(thisdict)

# Remove items
thisdict.pop("city")
print(thisdict)

# loop through dictionaries
for b in thisdict:
  print(b)