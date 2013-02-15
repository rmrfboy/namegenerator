import random

def generate_name():
    lst = open('/usr/share/dict/american-english','r').read().splitlines()
    word = lst[random.randrange(1,len(lst))]
    while (('\'' in word)==False):
        word = lst[random.randrange(1,len(lst))]
    return word[0: word.index('\'')]

#@app.route('/generate')
def index():
    generate_name() + ' ' + generate_name()


if __name__ == '__main__':
    print generate_name() + ' ' + generate_name()
    
