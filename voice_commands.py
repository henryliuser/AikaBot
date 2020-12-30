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
        try:
            ra[x] = linecache.getline('shakespeare_insults.txt', ra[x]).rstrip().split()[x]
        except:
            print(f'x: {x}\nra: {ra}')  # debug
    return f"{name} is a {' '.join(ra)}"

def quote(l=None, r=None) -> str:
    aika_quotes = ["The beginning is the end, and the end is the beginning. \
    Well then, let us begin again. And to each, their own tale.",
                   "The subtle light that is born when people's feelings come together. \
That light embraces felicity, evil, sin, and happiness. The light blazes forth... \
illuminating the whole truth.",
                   "Just because it's illogical, that doesn't make it wrong.",
                   "Summer stars are so unscrupulous. They shine without thought or care. \
They try so hard to display their radiance. Trying to let us know they exist before they disappear. \
I admire that simple, honest wish.",
                   "Everything happens for a reason. The daily tragedies and misfortunes are all \
meaningful events, leading toward an ideal conclusion. With that in mind, there probably isn't \
really any meaningless misfortune.",
                   "The actors on stage cannot ignore their scripts and do as they wish. If they \
make a beautiful exit, I feel they fulfill their role.",
                   "It might be for the better if there are amusing people around me. Because \
any tragedy may seem a comedy, as long as I am with them.",
                   "The beginning is the end, and the end is the beginning. Well then, \
let us begin again. And to each, their own tale."
                   ]
    return random.choice(aika_quotes).replace('.', ',')

def goodbye(l=None, r=None) -> str:
    return 'farewell'

def stop(l=None, r=None) -> str:
    return 'stop'

def apology(l=None, r=None) -> str:
    return "i'm sorry, you were the one who programmed me."

def pls_pp(l, name: str) -> str:
    return f"{name} is sporting {length()}"

commands = {'please pp':pls_pp, 'insult':ss_insult, 'how long is':length,
            'farewell':goodbye, 'goodbye':goodbye, 'stop eavesdropping':stop,
            'stop listening':stop, 'you suck':apology, 'read me a quote':quote,
            "sometimes you stop working and i don't know why":apology}



