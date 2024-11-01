import numpy as np
import random

class AntColony:
    def __init__(self, num_ants, num_iterations, decay, alpha, beta):
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.decay = decay 
        self.alpha = alpha  
        self.beta = beta 
        self.pheromone = None
        self.distances = None
        self.best_path = None
        self.best_distance = float('inf')

    def initialize(self, distances):
        self.distances = distances
        self.num_nodes = len(distances)
        self.pheromone = np.ones((self.num_nodes, self.num_nodes)) / self.num_nodes

    def run(self):
        for iteration in range(self.num_iterations):
            all_paths = self.generate_paths()
            self.update_pheromone(all_paths)
            self.best_path, self.best_distance = self.get_best_path(all_paths)
            print(f"Iteración {iteration + 1}: Mejor ruta {self.best_path} con distancia {self.best_distance}")

    def generate_paths(self):
        all_paths = []
        for _ in range(self.num_ants):
            path = self.create_path()
            all_paths.append(path)
            print(f"Hormiga ruta: {path} con distancia {self.calculate_path_distance(path)}")
        return all_paths

    def create_path(self):
        path = [0]
        visited = set(path)
        while len(path) < self.num_nodes:
            next_node = self.select_next_node(path[-1], visited)
            path.append(next_node)
            visited.add(next_node)
        path.append(0) 
        return path

    def select_next_node(self, current_node, visited):
        probabilities = []
        total_pheromone = 0.0
        for next_node in range(self.num_nodes):
            if next_node not in visited:
                pheromone = self.pheromone[current_node][next_node] ** self.alpha
                heuristic = (1.0 / self.distances[current_node][next_node]) ** self.beta
                probabilities.append(pheromone * heuristic)
                total_pheromone += pheromone * heuristic
            else:
                probabilities.append(0.0)

        probabilities = [p / total_pheromone for p in probabilities] 
        return np.random.choice(range(self.num_nodes), p=probabilities)

    def update_pheromone(self, all_paths):
        self.pheromone *= (1 - self.decay)
        for path in all_paths:
            distance = self.calculate_path_distance(path)
            for i in range(len(path) - 1):
                self.pheromone[path[i]][path[i + 1]] += 1.0 / distance

    def calculate_path_distance(self, path):
        distance = 0
        for i in range(len(path) - 1):
            distance += self.distances[path[i]][path[i + 1]]
        return distance

    def get_best_path(self, all_paths):
        best_path = None
        best_distance = float('inf')
        for path in all_paths:
            distance = self.calculate_path_distance(path)
            if distance < best_distance:
                best_distance = distance
                best_path = path
        return best_path, best_distance

    ant_colony = AntColony(num_ants = 10, num_iterations = 10, decay = 0.5, alpha = 1, beta = 1)
    ant_colony.initialize(distances)
    ant_colony.run()

    print("Mejor ruta final:", ant_colony.best_path)
    print("Mejor distancia final:", ant_colony.best_distance)
