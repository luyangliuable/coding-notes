def get_gradient_at_b(x, y, m, b):
    N = len(x)
    diff = 0
    for i, enum_x in enumerate(x):
      diff += (y[i] - (m*enum_x+b))
    return -2/N*diff;
