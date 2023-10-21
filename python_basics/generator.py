"""
After execution it does not destroy the
value inside the function and it also remember the last state
"""


def remote_control_next():
    yield "cnn"
    yield "espn"
    yield "HBO"


itr = remote_control_next()
print(next(itr))
print(next(itr))
print(next(itr))

for c in remote_control_next():
    print(c)
