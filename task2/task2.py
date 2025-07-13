def read_circle(filename='dot.txt'):
    with open(filename, 'r') as f:
        x_0, y0 = map(float, f.readline().strip().split())
        rad = float(f.readline().strip())
        return x_0, y0, rad


def classify_points(filename='circle.txt', x0=0, y0=0, rad=1):
    with open(filename, 'r') as f:
        for line in f:
            if not line.strip():
                continue
            x, y = map(float, line.strip().split())
            dist2 = (x - x0) ** 2 + (y - y0) ** 2
            r2 = rad ** 2

            eps = 1e-10
            if abs(dist2 - r2) <= eps:
                print(0)
            elif dist2 < r2:
                print(1)
            else:
                print(2)


x0, y0, rad = read_circle()
classify_points(x0=int(x0), y0=int(y0), rad=int(rad))
