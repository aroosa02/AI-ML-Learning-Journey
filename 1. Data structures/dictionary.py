#A dictionary in Python is a data type used to store data in key–value pairs.
#real life dictionart--- word-meaning, key-value pair
# Ordered 
# Mutable (Can change)
# Keys must be unique
# Keys must be immutable (string, number, tuple)
# Values can be anything

#Creating a dictionary
student = {
    "name": "Aroosa",
    "age": 21,
    "course": "Computer Science"
}
print(student)
print(type(student))

#empty dictionary
empty = {}
print(type(empty))
#or
empty = dict()
print(type(empty))

#Accessing values in a dictionary
print(student["name"]) # Accessing value using key
print(student.get("age")) # Accessing value using get() method
#The get() method is safer than using square brackets because it returns None if the key is not found, instead of raising a KeyError.
print(student.get("grade")) # returns None since "grade" key is not present in the dictionary
print(student.get("dept" , "Dept not available"))  #we can also give msg if key doesn't exist -- > .get(key, msg)

#Modifying values in a dictionary   
student["age"] = 22 # Modifying value using key
print(student)
#Adding new key-value pairs to a dictionary
student["grade"] = "A" # Adding new key-value pair using key
print(student)
#Updating multiple key-value pairs using update() method
student.update({"name": "Aroosa Jabeen", "course": "Python Programming"}) 
#removing item by key
student.pop("age")
print(student)
student.popitem() #removes the last inserted item
print(student)
del student["age"] #removes the item with the specified key (raises KeyError if key doesn't exist)
print(student)
student.clear() #removes all items from the dictionary
print(student)
print(student.keys()) #returns all keys in the dictionary
print(student.values()) #returns all values in the dictionary
print(student.items()) #returns all key-value pairs in the dictionary as a list of tuples
#looping through a dictionary
for key in student:
    print(key) # prints all keys in the dictionary
for key, value in student.items():
    print(key, value) # prints all key-value pairs in the dictionary
for key, value in student.items():
    print(key, ":", value)
#checking if a key is in the dictionary
print("name" in student)
print("age" in student)

#Nested dictionaries
students = {
    "student1": {
        "name": "Aroosa",
        "age": 21,
        "course": "Computer Science"
    },
    "student2": {
        "name": "Alina",
        "age": 21,
        "course": "Python"
    }
 }
print(students["student1"]["name"])

