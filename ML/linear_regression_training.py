import numpy as np
from numpy.typing import NDArray


class Solution:
    # given
    # the get_derivative function is getting the derivative of the MSE with respect to desired_weight.
    # This is so we can update the weights in a way such that the loss (MSE) is minimized.
    # The intuition behind this is that minimal error = a model that is less wrong = a more accurate model.
    def get_derivative(
        self,
        model_prediction: NDArray[np.float64],
        ground_truth: NDArray[np.float64],
        N: int,
        X: NDArray[np.float64],
        desired_weight: int,
    ) -> float:
        # note that N is just len(X)

        # Ensure X is a NumPy array
        X = np.asarray(X)

        # Ensure that X is at least 2D
        if X.ndim == 1:
            X = X.reshape(-1, 1)

        return -2 * np.dot(ground_truth - model_prediction, X[:, desired_weight]) / N

    # given
    def get_model_prediction(
        self, X: NDArray[np.float64], weights: NDArray[np.float64]
    ) -> NDArray[np.float64]:
        return np.squeeze(np.matmul(X, weights))

    # given
    learning_rate = 0.01

    def train_model(
        self,
        X: NDArray[np.float64],
        Y: NDArray[np.float64],
        num_iterations: int,
        initial_weights: NDArray[np.float64],
    ) -> NDArray[np.float64]:

        # you will need to call get_derivative() for each weight
        # and update each one separately based on the learning rate!
        # return np.round(your_answer, 5)

        for _ in range(num_iterations):
            model_prediction = self.get_model_prediction(X, initial_weights)

            # need to call 3 times for the derivative because each weight needs a derivative
            derivative1 = self.get_derivative(model_prediction, Y, len(X), X, 0)
            derivative2 = self.get_derivative(model_prediction, Y, len(X), X, 1)
            derivative3 = self.get_derivative(model_prediction, Y, len(X), X, 2)

            # update rule: new_weight = old_weight - derivative * learning_rate
            initial_weights[0] -= derivative1 * self.learning_rate
            initial_weights[1] -= derivative2 * self.learning_rate
            initial_weights[2] -= derivative3 * self.learning_rate

        return np.round(initial_weights, 5)


X: NDArray[np.float64] = [[1, 2, 3], [1, 1, 1.0]]
Y: NDArray[np.float64] = [6, 3.0]
num_iterations: int = 10
initial_weights: NDArray[np.float64] = [0.2, 0.1, 0.6]
sol = Solution()
print(sol.train_model(X, Y, num_iterations, initial_weights))
