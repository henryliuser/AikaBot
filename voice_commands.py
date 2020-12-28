import random, linecache
# l & r are dummy args

def length(l=None, r=None) -> str:
    rand = random.randint(0, 20)
    measurements = ['inches', 'feet', 'miles', 'meters', 'centimeters',
                    'kilometers', 'lightyears', 'millimeters', 'yards',
                    'football fields', 'astronomical units']
    return f"{rand} {random.choice(measurements)}"

def ss_insult(l, name: str) -> str:
    ra = [random.randint(0,61) for _ in range(3)]
    for x in range(3):
        ra[x] = linecache.getline('shakespeare_insults.txt', ra[x]).rstrip().split()[x]
    return f"{name} is a {' '.join(ra)}"

def pls_pp(l, name: str) -> str:
    return f"{name} is sporting {length()}"

commands = {'please pp':pls_pp, 'insult':ss_insult, 'how long is':length}



