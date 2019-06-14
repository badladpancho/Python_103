#       Dictionaries are useful in python:
#       Dictionary in Python is an unordered collection of data values,
#       used to store data values like a map, which unlike other Data
#       Types that hold only single value as an element
#       creating a program will convert 3 letter months to the full name
#       example jan --> january

monthConversion = {
    "Jan" : "January",
    "Feb" : "February",     #keys have to be unique, and they can be numbers also!
    "Mar" : "March",
    "Apr" : "April",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December",
    12 : "December",        #   Intiger example
}
# now we can Acces them by refering to the key
print(monthConversion["Oct"])
#Or we can do this both are valid
print(monthConversion.get("Dec"))
print(monthConversion.get(12))
# Some times keys are not valid and you get none but you can pass a value
print(monthConversion.get("fake", "This is not a valid key"))

