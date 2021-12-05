import random


class Genome:

    @staticmethod
    def generate(gen_p1, gen_p2):

        a = random.choice(gen_p1)
        b = random.choice(gen_p2)

        gen = (a, b)
        return gen

    @staticmethod
    def is_dominant(gen, dominant):
        if dominant in gen:
            return True
        else:
            return False


class Birth:
    @staticmethod
    def generate(genomes, gen_p1_lst, gen_p2_lst):
        gen_list = []
        for i in range(genomes):
            gen = Genome.generate(gen_p1_lst[i], gen_p2_lst[i])
            gen_list.append(gen)

        return gen_list
