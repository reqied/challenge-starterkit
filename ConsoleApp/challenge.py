import numpy as np

string = "15.9*x^2 + 19.1*x + (-14.799999999999999)"
terms = string.split("+")
coefs = []
for term in terms:
    partTerms = term.split("*")
    coefs.append(float(partTerms[0].replace('(', '').replace(')', '').replace(' ', '').replace('  ', '').replace('   ', '')))


solve = np.roots(coefs)
print(solve)



