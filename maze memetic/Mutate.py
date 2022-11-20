from random import choice

class Mutation:

    def __init__(self, genes: str):
        self.genes = genes
    # Random Resetting Mutation
    def mutate_genes(self) -> str:
        gene = choice(self.genes)
        return gene
