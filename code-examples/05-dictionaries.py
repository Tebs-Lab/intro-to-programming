# Dictionaries are the second main built in way to handle
# collections of data. Instead of an ordered collection
# like the list, dictionaries are unordered key/value pairs.

# To make a dictionary we use curly braces: {}
empty_dictionary = {}

# Many types of data can be keys, and ANY type of data can be a value
key_examples = {
    "tyler": 75,
    1: "24",
    None: [1,2,3]
}

# We can fetch an item from a dictionary using bracket notation
# similar to lists. We can also use a built in function called 
# get, which returns None if no element in the dictionary matches.

print(key_examples['tyler'] == key_examples.get('tyler')) # True

# We can also add a new key/value pair using bracket notation:
key_examples['new_key'] = 'new value'

# If we try to access a non-existant key with bracket notation
# we get an error, which is a good reason to use .get

# key_examples[7] # error, terminates program
print(key_examples.get(7)) # prints None

# We can also loop through dictionaries, but the order is decided
# arbitrarily so remember not to rely on an order when doing so.

print('\n===looping===')
for key, value in key_examples.items():
    print(key, value)