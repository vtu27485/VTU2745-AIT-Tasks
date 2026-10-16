def move(x1, x2):
    return f"Move monkey from {x1} to {x2}"

def push_box(x1, x2):
    return f"Push box from {x1} to {x2}"

def climb_box(x):
    return f"Climb box at {x} up"

def have_banana(x):
    return f"Have banana at {x}"


monkey, box, banana = 0, 2, 4

actions = [
    move(monkey, box),
    push_box(box, banana),
    move(box, banana),
    climb_box(banana),
    have_banana(banana)
]

print("Plan:")
for action in actions:
    print(action)


"""
INPUT:
Monkey = 0
Box = 2
Banana = 4

OUTPUT:
Plan:
Move monkey from 0 to 2
Push box from 2 to 4
Move monkey from 2 to 4
Climb box at 4 up
Have banana at 4
"""
