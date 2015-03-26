

# My solution

def bigrams(a):
    s = set()
    for i in range(len(a)-1):
        s.add(a[i:i+2])
    return s

print bigrams("llangardaix")
print bigrams("setze jutges d'un jutjat")