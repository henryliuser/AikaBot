import random, linecache

def length() -> str:
    r = random.randint(0, 20)
    measurements = {'inches', 'feet', 'miles', 'meters', 'centimeters',
                    'kilometers', 'lightyears', 'millimeters', 'yards',
                    'football fields', 'astronomical units'}
    return f"{r} {random.choice(measurements)}"

def ss_insult(name: str) -> str:
    r = [random.randint(0,61) for _ in range(3)]
    for x in range(3):
        r[x] = linecache.getline('shakespeare_insults.txt', r[x]).rstrip().split()[x]
    return f"{name} is a {' '.join(r)}"

def pls_pp(name: str) -> str:
    return f"{name} is sporting {length()}"

commands = {'please pp':pls_pp, 'insult':ss_insult, 'how long is':length()}



