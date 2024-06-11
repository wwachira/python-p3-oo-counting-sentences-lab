#!/usr/bin/env python3

class MyString:
  #default value of empty string
  def __init__(self, value = ''):
      self._value = value
  
  # give a value property as an attribute of this class
  def get_value(self):
    return self._value
  
  def set_value(self, stringValue):
    if(type(stringValue) == str):
      self._value = stringValue
    
    else:
      print("The value must be a string.")

  value = property(get_value, set_value)

  def is_sentence(self):
    return self._value.endswith(".")
  
  def is_question(self):
    return self._value.endswith("?")
  
  def is_exclamation(self):
    return self._value.endswith("!")
  
  # count of sentences in value
  def count_sentences(self):
    # Get the text stored in the 'value' attribute of the class instance
    value = self.value
    
    # Replacing '!' and '?' with '.'
    value = value.replace('!', '.').replace('?', '.')

    # Split the text into sentences based on period ('.') and remove empty strings
    sentences = list(filter(None, value.split('.')))

    # Return the count of sentences
    return len(sentences)
my_string = MyString("Hello, world!")
print(my_string.value)  # Output: "Hello, world!"
print(my_string.is_sentence())  # Output: False
print(my_string.is_question())  # Output: False
print(my_string.is_exclamation())  # Output: True
print(my_string.count_sentences())  # Output: 1