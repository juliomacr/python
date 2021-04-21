# Create a `Test` class and add test methods
class Test(object):
  # Define a function `count_vowels()`
  def count_vowels(self, testText):
    data = str(testText)
    vowels = "aeiou"
    total = 0
    for char in data:
        if char in vowels:
            total += 1
    return(total)

  # Define a function `factorial()`  
  def factorial(self, number):
    n = number
    fact = 1  
    for i in range(1,n+1):
        fact = fact * i
    return(fact)

  # Define a function `relation_to_luke()`
  def relation_to_luke(self, name):
    person_relation = {'Darth Vader' : 'father', 'Leia' : 'sister', 'Han' : 'brother in law', 'R2D2' : 'droid'}
    search_key = name   

    # list out keys and values separately
    key_list = list(person_relation.keys())
    val_list = list(person_relation.values())
    
    # print key with val name
    position = key_list.index(search_key)
    print("Luke I am your ",val_list[position])

# Instantiate `Test` class
testInstance = Test()

#test cases
vowels_total = testInstance.count_vowels("holagato")
factorial_result = testInstance.factorial(4)
testInstance.relation_to_luke("Leia")
print(vowels_total, factorial_result)