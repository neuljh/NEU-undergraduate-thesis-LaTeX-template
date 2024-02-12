def newton_sqrt(x, epsilon=1e-5, max_iter=100):
    cur = x ** 0.5
    for i in range(max_iter):
        next = 0.5 * (cur + x / cur)
        if abs(next - cur) < epsilon:
            return next
        cur = next
    raise Exception("Failed to converge after {} iterations".format(max_iter))