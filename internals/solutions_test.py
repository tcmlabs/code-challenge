from hypothesis import given
from hypothesis import strategies as st

from solutions import string_monoid, integer_monoid_one, integer_monoid_two, boolean_monoid_one, boolean_monoid_two, list_monoid, function_monoid, integer_addition_property_one, integer_addition_property_two,  integer_multiplication_property_one,integer_multiplication_property_two


# Integers
@given(integer_monoid_one.get('set')())
def test_integer_monoid_a(s):
    binary_operation = integer_monoid_one.get('operation')
    neutral_element = integer_monoid_one.get('neutral_element')
    
    assert(binary_operation(s, neutral_element)) == s

@given(integer_monoid_two.get('set')())
def test_integer_monoid_b(s):
    binary_operation = integer_monoid_two.get('operation')
    neutral_element = integer_monoid_two.get('neutral_element')
    
    assert(binary_operation(s, neutral_element)) == s

# Strings
@given(string_monoid.get('set')())
def test_string_monoid(s):
    binary_operation = string_monoid.get('operation')
    neutral_element = string_monoid.get('neutral_element')
    
    assert(binary_operation(s, neutral_element)) == s

# Lists
@given(list_monoid.get('set')(1))
def test_list_monoid(s):
    binary_operation = list_monoid.get('operation')
    neutral_element = list_monoid.get('neutral_element')
    
    assert(binary_operation(s, neutral_element)) == s

# Booleans
@given(boolean_monoid_one.get('set')())
def test_boolean_monoid_a(s):
    binary_operation = boolean_monoid_one.get('operation')
    neutral_element = boolean_monoid_one.get('neutral_element')
    
    assert(binary_operation(s, neutral_element)) == s

@given(boolean_monoid_two.get('set')())
def test_boolean_monoid_b(s):
    binary_operation = boolean_monoid_two.get('operation')
    neutral_element = boolean_monoid_two.get('neutral_element')
    
    assert(binary_operation(s, neutral_element)) == s

# Functions
@given(function_monoid.get('set')(1), st.randoms())
def test_function_monoid(func, random_value):
    binary_operation = function_monoid.get('operation')
    neutral_element = function_monoid.get('neutral_element')
    
    assert(binary_operation(func, neutral_element)(random_value)) == func(random_value)

## PBT addition
@given(st.integers(), st.integers(), st.integers())
def test_integer_property_x(a, b, c):
    assert(integer_addition_property_one(a, b))
    
@given(st.integers(), st.integers(), st.integers())
def test_integer_property_y(a, b, c):
    assert(integer_addition_property_two(a, b))

## PBT multiplication
@given(st.integers(), st.integers(), st.integers())
def test_multiplication_property_x(a, b, c):
    assert(integer_multiplication_property_one(a, b))
    
@given(st.integers(), st.integers(), st.integers())
def test_multiplication_property_y(a, b, c):
    assert(integer_multiplication_property_two(a, b))
