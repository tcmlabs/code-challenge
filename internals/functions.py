from hypothesis import strategies as st

def fn(a):
  return a

any_function = lambda _: st.functions(like=any_function)