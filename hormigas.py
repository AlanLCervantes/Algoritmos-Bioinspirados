import numpy as np # Usaremos arrays
import matplotlib.pyplot as plt # Para pintar resultados
import ants as ants # Aquí están los objetos del algoritmo

map1 = ants.Mapa(10)
map1.draw_distances()
map1.swarm_create(100)
map1.swarm_show()

map1.show_distances_matrix()
map1.show_feromones_matrix()

map1.swarm_generation()

map1.show_feromones_matrix()
map1.draw_feromones()

for i in range(50):
    print(i, end = '·')
    map1.swarm_generation()
map1.show_feromones_matrix()
map1.draw_feromones()

map1.draw_best_path()

for j in range(3):
    map1.feromone_reset()
    print()
    print('Ejecución', j+1, ', generación: ')
    for i in range(50):
        print(i+1, end = '·')
        map1.swarm_generation()
    map1.draw_feromones()

map1.draw_best_path()

map1.draw_results()

map2 = ants.Mapa(40)
map2.swarm_create(200)
map2.swarm_generation()
map2.show_feromones_matrix()
map2.draw_feromones()

map2.feromone_fine_tune()

map2.swarm_generation()
map2.show_feromones_matrix()
map2.draw_feromones()

for i in range(25):
    print(i, end = '·')
    map2.swarm_generation()
map2.show_feromones_matrix()
map2.draw_feromones()
map2.draw_best_path()
map2.draw_results()