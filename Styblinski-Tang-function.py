import random, copy, math
import matplotlib.pyplot as plt

N = 10
P = 500
m = 10
MUTRATE = 0.1
MUTSTEP = 1
loop= 100
MIN = 0
MAX = math.pi
population = []
result = []


class individual:
    def __init__(self):
        self.gene = [0]*N
        self.fitness = 0

def test_function( ind ):
    utility=0
    for i in range(N):
        utility =(utility + ((ind.gene[i] ** 4)-((16 *(ind.gene[i] )** 2)+(5* ind.gene[i]))))
          
    return (1/2) * utility
    
def sum(lst):
    sum=0
    for ind in lst:
        sum = sum+ind.fitness
    return sum

#populating the population
for x in range (0, P):
    tempgene=[]
    for y in range (0, N):
        tempgene.append( random.uniform(MIN,MAX))
    newind = individual()
    newind.gene = tempgene.copy()
    newind.fitness= test_function(newind)
    population.append(newind)

    
for itr in range(loop):
    offspring= []
    mutated_offspring= []

    worst_of_population=individual()
    worst_of_population.fitness= math.inf

    best_of_mutatedoffspring=individual()
    best_of_mutatedoffspring.fitness= - math.inf

    worst_of_mutatedoffspring=individual()
    worst_of_mutatedoffspring.fitness= math.inf


    for ind in population:
        if ind.fitness <= worst_of_population.fitness:
            worst_of_population = ind
            

    for i in range (0, P):
        parent1 = random.randint( 0, P-1 )
        off1 = copy.deepcopy(population[parent1])
        parent2 = random.randint( 0, P-1 )
        off2 = copy.deepcopy(population[parent2])
        if off1.fitness < off2.fitness:
            offspring.append( off1 )
        else:
            offspring.append( off2 )
    



    # crossover

    toff1 = individual()
    toff2 = individual()
    temp = individual()
    for i in range( 0, P, 2 ):

        toff1 = copy.deepcopy(offspring[i])
        toff2 = copy.deepcopy(offspring[i+1])
        temp = copy.deepcopy(offspring[i])
        crosspoint = random.randint(1,N) 

        for j in range (crosspoint, N):
            toff1.gene[j] = toff2.gene[j]
            toff2.gene[j] = temp.gene[j]
        offspring[i] = copy.deepcopy(toff1)
        offspring[i+1] = copy.deepcopy(toff2)
    


    # mutation
    for i in range( 0, P ):
        newind = individual()
        newind.gene = []
        for j in range( 0, N ):
            gene = offspring[i].gene[j]
            mutprob = random.random()
            if mutprob < MUTRATE:
                alter = random.uniform(-MUTSTEP,MUTSTEP)
                gene = gene + alter
                if gene > MAX:
                    gene = MAX
                if gene < MIN:
                    gene = MIN
            newind.gene.append(gene)
        
        newind.fitness= test_function(newind)
        mutated_offspring.append(newind)






    for ind in mutated_offspring:
        if ind.fitness >= best_of_mutatedoffspring.fitness:
            best_of_mutatedoffspring = ind
           
    
    
    x= mutated_offspring.index(best_of_mutatedoffspring)
    mutated_offspring[x] = (worst_of_population)

    
    population = copy.deepcopy(mutated_offspring)


    for ind in population:
        if ind.fitness < worst_of_mutatedoffspring.fitness:
            worst_of_mutatedoffspring = ind
    

    result.append(worst_of_mutatedoffspring.fitness)
    
    print(f'itr no: {itr}, result: {worst_of_mutatedoffspring.fitness}')



plt.plot(result)
plt.show()
            