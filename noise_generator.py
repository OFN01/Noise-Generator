import random

def noise(x:float, y:float) -> float:
    random.seed(x*y)
    x1 = int(x/10) * 10 + random.randint(-4, 4)
    random.seed(x+1*y+1)
    x2 = (int(x/10) + 1) * 10 + random.randint(-4, 4)
    random.seed(x+2*y+2)
    y1 = int(y/10) * 10 + random.randint(-4, 4)
    random.seed(x+3*y+3)
    y2 = (int(y/10) + 1) * 10 + random.randint(-4, 4)
    random.seed(x1*y1)
    x1y1 = random.randint(1, 100) / 80
    random.seed(x1*y2)
    x1y2 = random.randint(1, 100) / 80
    random.seed(x2*y1)
    x2y1 = random.randint(1, 100) / 80
    random.seed(x2*y2)
    x2y2 = random.randint(1, 100) / 80
    x1y1D, x1y2D = x1y1 * ((x - x1)*(y - y1)), x1y2 * ((x - x1)*(y - y2))
    x2y1D, x2y2D = x2y1 * ((x - x2)*(y - y1)), x2y2 * ((x - x2)*(y - y2))
    return ((x1y1D * x1y2D * x2y1D * x2y2D) * (x1y1D * x1y2D * x2y1D * x2y2D)) / 4000000000