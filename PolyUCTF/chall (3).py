from Cryptodome.Util.number import getRandomInteger
# from flag import flag, m, a, c

m = 1
a = 1
c = 1


class Rand:
    def __init__(self, seed):
        self.m = m
        self.a = a
        self.c = c
        self.seed = seed
        print(m, a, c, seed)
        if seed % 2 == 0:
            self.seed += 1

    def rand(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed

# seed = (a*seed + c) % m


def main():
    rng = Rand(getRandomInteger(32))

    print("I give you the past, can you predict the future?")
    for _ in range(10):
        print(rng.rand())

    for _ in range(10):
        x = int(input('input next number> '))
        if x != rng.rand():
            print("You should study Tong Ling More")
            return

    print("You are Tong Ling master")
    print(flag)


if __name__ == "__main__":
    main()
