def get_input():
    with open("inp-day2.txt", "r") as f:
        return [(c.split()[0], int(c.split()[1])) for c in f.read().splitlines()]



input = get_input()

# ------------------ #
# ------------------ #
'''
def forward(pos, n):
    pos[0] += n

def down(pos, n):
    pos[1] += n

def up(pos, n):
    pos[1] -= n

commands = {
    "forward" : forward,
    "down" : down,
    "up" : up
}


pos = [0, 0]

for step in input:
    commands[step[0]](pos, step[1])

print(f"Final position => ({pos[0]}, {pos[1]})")
print(f"SOLUTION <{pos[0]*pos[1]}>")
'''


def forward(pos, aim, n):
    pos[0] += n
    pos[1] += aim[0]*n

def down(_, aim, n):
    aim[0] += n

def up(_, aim, n):
    aim[0] -= n

commands = {
    "forward" : forward,
    "down" : down,
    "up" : up
}

pos = [0, 0]
aim = [0]

for step in input:
    commands[step[0]](pos, aim, step[1])

print(f"Final position => ({pos[0]}, {pos[1]})")
print(f"Final aim => {aim}")
print(f"SOLUTION <{pos[0]*pos[1]}>")