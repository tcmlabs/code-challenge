from hypothesis import strategies as st
from internal import any_function

# ---------------
# Première partie
# ---------------
#
# Considérant la définition suivante d'un monoïde :
# - un ensemble E
# - une opération binaire, associative, dans cet ensemble
# - un élément neutre, dans cet ensemble E
#
# Trouver les opérations et/ou les éléments neutres manquant dans les monoides suivants (remplacer les valeurs None).
# Le premier monoïde est donné comme exemple.

# Dans l'ensemble des nombres entiers
# Pour tout a et b appartenant aux entiers, a + 0 = a.
integer_monoid_a = {
  'set': st.integers,
  'operation': lambda a, b: a + b,
  'neutral_element': 0
}

integer_monoid_b = {
  'set': st.integers,
  'operation': lambda a, b: None,
  'neutral_element': None
}

# Dans l'ensemble des chaines de caractères
string_monoid = {
  'set': st.text,
  'operation': lambda a, b: None,
  'neutral_element': None
}

# Dans l'ensemble des listes (tableaux)
list_monoid = {
  'set': lambda _: st.lists(st.randoms()),
  'operation': lambda a, b: None,
  'neutral_element': None
}

# Dans l'ensemble des booléens
boolean_monoid_a = {
  'set': st.booleans,
  'operation': lambda a, b: a and b,
  'neutral_element': None
}

boolean_monoid_b = {
  'set': st.booleans,
  'operation': lambda a, b: a or b,
  'neutral_element': None
}

# Functions
def function_composition(f, g):
  return lambda x: g(f(x))

function_monoid = {
  'set': any_function,
  'operation': function_composition,
  'neutral_element': None
}
