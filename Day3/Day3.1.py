def get_points_from_moves(moves):
    points = []
    previous_point = (0, 0)
    points.append(previous_point)
    for move in moves:
        direction = move[0:1]
        step = int(move[1:])
        if direction == "U":
            new_point = [(previous_point[0], previous_point[1] + (inc + 1)) for inc in range(step)]
        if direction == "D":
            new_point = [(previous_point[0], previous_point[1] - (inc + 1)) for inc in range(step)]
        if direction == "R":
            new_point = [(previous_point[0] + (inc + 1), previous_point[1]) for inc in range(step)]
        if direction == "L":
            new_point = [(previous_point[0] - (inc + 1), previous_point[1]) for inc in range(step)]
        points.extend(new_point)
        previous_point = points[-1]

    return points


def print_points(points1, points2):
    # importing two required module
    import numpy
    from matplotlib import pyplot as plt
    # Creating a numpy array
    X1 = numpy.array([x for (x, y) in points1])
    Y1 = numpy.array([y for (x, y) in points1])
    # Plotting point using sactter method
    plt.scatter(X1, Y1)

    X2 = numpy.array([x for (x, y) in points2])
    Y2 = numpy.array([y for (x, y) in points2])
    # Plotting point using sactter method
    plt.scatter(X2, Y2)
    plt.show()


def find_cross_points(points1, points2):
    a_set = set(points1)
    b_set = set(points2)
    if a_set & b_set:
        cross_points = list(a_set & b_set)
        cross_points.remove((0, 0))
        return cross_points


def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


with open("inputDay3.txt") as f:
    moves = f.readline().split(",")
    points1 = get_points_from_moves(moves)
    print(points1)

    moves = f.readline().split(",")
    points2 = get_points_from_moves(moves)
    print(points2)

    cross = find_cross_points(points1, points2)
    distances = [distance((0, 0), p) for p in cross]
    print(cross)
    print(distances)
    print(min(distances))

    print_points(points1, points2)
