INPUT_FILE = 'input.txt'

def count():
    c = 0
    with open(INPUT_FILE, 'r') as file:
                for line in file:
                    f, s = [(list(map(int,l.split('-')))) for l in line.strip('\n').split(',')]
                    if(((f[0]>=s[0])&(f[1]<=s[1]))|((f[0]<=s[0])&(f[1]>=s[1]))):c+=1
    return(c)

print(count())


