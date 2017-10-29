from lab02.common import *


class GradientDescent:
    def __init__(self, alpha: float, iterations: int):
        self.theta: np.ndarray = np.asarray([])
        self.alpha: float = alpha
        self.iterations: int = iterations

    def fit(self, x: np.ndarray, y: np.ndarray):
        theta: np.ndarray = np.ones(x.shape[1])

        for i in range(self.iterations):
            hypothesis = np.dot(x, theta)
            loss = hypothesis - y
            gradient = np.dot(x.transpose(), loss) / x.shape[0] * 2
            theta = theta - self.alpha * gradient

        self.theta = theta

    def predict(self, x: np.ndarray):
        return np.dot(x.transpose(), self.theta)


if __name__ == '__main__':
    x, y = read_split_data()
    x = (x - x.mean()) / x.std()

    g = GradientDescent(0.1, 5000)
    g.fit(x, y)

    compute_error_for_all(g, x, y)

    while False:
        raw_str = input("Input 'q' to exit or 3 number: \n")
        if raw_str.lower() == 'q':
            break

        arr = [int(num) for num in raw_str.replace(',', ' ').split(' ')]

        predict = g.predict(np.asarray(arr[:2]))
        error = compute_error(np.asarray([predict]), np.asarray([arr[2]]))
        print("Value = {}, Error = {}\n".format(predict, error))
