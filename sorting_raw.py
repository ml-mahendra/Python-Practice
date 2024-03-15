def sort4(x,y,z,u):
    if x > y:
        x,y = y,x
    if z>u:
        z,u = u,z
    if y>u:
        y,u = u,y
    if x>z:
        x,z = z,x
    if y>z:
        y,z = z,y

    return x,y,z,u

print(sort4(2,23,45,9))
