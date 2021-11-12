from hypothesis import strategies as st
from internal import any_function

# ---------------------------------
# Première partie -- les monoïdes !
# ---------------------------------
#
# Considérant la définition suivante d'un monoïde :
# - un ensemble E
# - une opération binaire, associative, dans cet ensemble
# - un élément neutre, dans cet ensemble E
#
# Trouver les opérations et/ou les éléments neutres manquant dans les monoides suivants (remplacer les valeurs None).
# Le premier monoïde est donné comme exemple (Integer, addition, 0)
#

# Exemple:
# Dans l'ensemble des nombres entiers:
# Pour tout a et b appartenant aux entiers, a + 0 = a.
integer_monoid_a = {
  'set': st.integers,
  'operation': lambda a, b: a + b,
  'neutral_element': 0
}

# Trouver une opération autre que l'addition, et son élément neutre correspondant
integer_monoid_b = {
  'set': st.integers,
  'operation': lambda a, b: a * b,
  'neutral_element': 1
}

# Dans l'ensemble des chaines de caractères, trouver une opération et
# son élément neutre
string_monoid = {
  'set': st.text,
  'operation': lambda a, b: a + b,
  'neutral_element': ''
}

# Dans l'ensemble des listes (tableaux), trouver une opération et son
# élément neutre
list_monoid = {
  'set': lambda _: st.lists(st.randoms()),
  'operation': lambda a, b: a + b,
  'neutral_element': []
}

# Dans l'ensemble des booléens, pour l'opération 'and' &&, trouver
# l'élément neutre
boolean_monoid_a = {
  'set': st.booleans,
  'operation': lambda a, b: a and b,
  'neutral_element': True
}

# Dans l'ensemble des booléens, pour l'opération 'or' ||, trouver
# l'élément neutre
boolean_monoid_b = {
  'set': st.booleans,
  'operation': lambda a, b: a or b,
  'neutral_element': False
}

# Dans l'ensemble des fonctions, et pour l'opération de composition
# de fonction g . f (cf. la fonction 'function_composition' ci-après)
# trouver l'élément neutre (ne pas oublier que cet élément neutre est
# doit lui-même être une fonction).
def function_composition(f, g):
  return lambda x: g(f(x))

function_monoid = {
  'set': any_function,
  'operation': function_composition,
  'neutral_element': lambda x: x
}

# ---------------------------------------------
# Deuxième partie - le property-based testing !
# ---------------------------------------------
#
# Trouver deux propriétés mathématiques de l'addition des entiers
# qui sont toujours vraies, quels que soient les entiers a et b
def integer_addition_property_x(a, b):
  #return None
  return a + b == b + a

def integer_addition_property_y(a, b):
  #return None
  return a + 0 == a

# Trouver deux propriétés mathématiques de la multiplication des
# entiers qui sont toujours vraies, quels que soient a et b
def integer_multiplication_property_x(a, b):
  #return None
  return a * b == b * a

def integer_multiplication_property_y(a, b):
  #return None
  return a * 1 == a
