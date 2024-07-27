def get_minimizer(iterations: int, learning_rate: float, init: int) -> float:
    for i in range(iterations):
        derivative = 2 * init
        init = init - (learning_rate * derivative)
    return round(init, 5)


print(get_minimizer(0, 0.1, 5))
print(get_minimizer(10, 0.01, 5))
