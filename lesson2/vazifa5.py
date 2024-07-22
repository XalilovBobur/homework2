import random

class RandomSimvols:
    
    def rand(self):
        return random.randint(1, 100)


randomsimvols = RandomSimvols()

print(randomsimvols.rand())