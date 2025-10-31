import sympy as sy
from utils import greek_alphabet

x = sy.Symbol(greek_alphabet['omega'])

f = 1/(x+1)**2
integrated = sy.integrate(f, (x,1,sy.oo))
print(integrated)
