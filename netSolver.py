def solve_hedron(hedron):
    return num_children(hedron, [1])

def num_children(hedron, faces):
    total = 0
    num_unique_children = 0
    for face in faces:
        for child in hedron[face]:
            if child not in faces:
                num_unique_children += 1
                faces_temp = faces.copy()
                faces_temp.append(child)
                total += num_children(hedron, faces_temp)
    if num_unique_children == 0:
        return 1
    else:
        return total


hedron = {1: [2, 3, 4, 5], 2: [3, 1, 4, 6], 3: [1, 2, 5, 6], 4: [1, 2, 6, 5], 5: [1, 3, 6, 4], 6: [2, 3, 4, 5]}
print(solve_hedron(hedron))

