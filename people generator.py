import itertools
# n = 30000
#
# while n > 0:
#
#     n -= 1
#
#     if n == 150:
#
#         continue
#
#     print(n)
#
# print('Loop ended.')

n = 25
t = 0
for x in itertools.repeat(2, times=20):
    if t > n:
        print(t)
    else:
        t += x


"""
p = itertools.product(one_name, one_name2)
pk = list(p)
print(len(pk))

to know every possible combination (length of names)
"""

class Ccharacter:
    def __init__(self, name, age, job, life_exp):
        self.name = name
        self.age = age
        self.job = job
        self.life_exp = life_exp

    def name(self):
        yield generate_name()

    def age(self):
        int(random.randint(12, 102))

    def job(self):
        return generate_job()

    def life_exp(self):
        return int(math.ceil(((105 - self.age) / 3 * 2) + random.randint(0, 8)))

    @staticmethod
    def random_character():
        return Ccharacter

    def __str__(self):
        return '{} {}'.format(self.name, self.age)