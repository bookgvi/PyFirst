from time import time


class Prng(object):
    def __init__(self, seed=time()):
        self.seed = int(seed)
        self.random_list = []
        pass

    def random(self, count) -> None:
        if count > 0:
            self.seed = self.seed * 3 % 19
            self.random_list.append(self.seed)
            count -= 1
            self.random(count)
        return


if __name__ == '__main__':
    prng = Prng()
    prng.random(10)
    print(prng.random_list)
