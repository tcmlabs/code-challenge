from hypothesis import strategies as st
from functions import any_function

# Integers
integer_monoid_one = {
  'set': st.integers,
  'operation': lambda a, b: a + b,
  'neutral_element': 0
}

integer_monoid_two = {
  'set': st.integers,
  'operation': lambda a, b: a * b,
  'neutral_element': 1
}

# Strings
string_monoid = {
  'set': st.text,
  'operation': lambda a, b: a + b,
  'neutral_element': ''
}

list_monoid = {
  'set': lambda _: st.lists(st.randoms()),
  'operation': lambda a, b: a + b,
  'neutral_element': []
}

# Booleans
boolean_monoid_one = {
  'set': st.booleans,
  'operation': lambda a, b: a and b,
  'neutral_element': True
}

boolean_monoid_two = {
  'set': st.booleans,
  'operation': lambda a, b: a or b,
  'neutral_element': False
}

# Functions
def function_composition(f, g):
  return lambda x: g(f(x))

function_monoid = {
  'set': any_function,
  'operation': function_composition,
  'neutral_element': lambda x: x
}

# Property-based-testing
def integer_addition_property_one(a, b):
  return a + b == b + a

def integer_addition_property_two(a, b):
  return a + 0 == a

def integer_multiplication_property_one(a, b):
  return a * b == b * a

def integer_multiplication_property_two(a, b):
  return a * 1 == a
