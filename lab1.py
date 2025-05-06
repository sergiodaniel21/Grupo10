
import streamlit as st
import random

def f(x):
    return -35/961 * (x - 31) ** 2 + 40

def binary_to_decimal(binary):
    return int(binary, 2)

def decimal_to_binary(n, length):
    return format(n, f'0{length}b')

def generate_chromosome(length):
    return ''.join(random.choice('01') for _ in range(length))

def evaluate_population(population):
    return [(chromosome, f(binary_to_decimal(chromosome))) for chromosome in population]

def select_parents(evaluated):
    sorted_evaluated = sorted(evaluated, key=lambda x: x[1], reverse=True)
    return [sorted_evaluated[0][0], sorted_evaluated[1][0]]

def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]

def mutate(chromosome, mutation_probability):
    chromosome = list(chromosome)
    for i in range(len(chromosome)):
        if random.random() < mutation_probability:
            chromosome[i] = '0' if chromosome[i] == '1' else '1'
    return ''.join(chromosome)

def mostrar():    
    try:
        with open('docs/lab1.md', 'r', encoding='utf-8') as file:
            st.markdown(file.read())
    except FileNotFoundError:
        st.error("Archivo 'lab1.md' no encontrado.")

    population_size = st.slider("Tamaño de población", 2, 20, 4)
    chromosome_length = st.slider("Longitud del cromosoma", 4, 10, 6)
    max_generations = st.slider("Generaciones", 10, 500, 100)
    mutation_probability = st.slider("Probabilidad de mutación", 0.0, 1.0, 0.2)

    if st.button("Ejecutar algoritmo"):
        population = [generate_chromosome(chromosome_length) for _ in range(population_size)]
        best_overall = ("", -float("inf"))
        resultados = []

        for generation in range(1, max_generations + 1):
            evaluated = evaluate_population(population)
            best_gen = max(evaluated, key=lambda x: x[1])
            resultados.append({
                "Generación": generation,
                "Gen": best_gen[0],
                "x": binary_to_decimal(best_gen[0]),
                "f(x)": round(best_gen[1], 4)
            })
            if best_gen[1] > best_overall[1]:
                best_overall = best_gen
            parents = select_parents(evaluated)
            children = []
            while len(children) < population_size:
                p1, p2 = random.choices(parents, k=2)
                c1, c2 = crossover(p1, p2)
                children.extend([
                    mutate(c1, mutation_probability),
                    mutate(c2, mutation_probability)
                ])
            population = children[:population_size]

        st.success("Mejor gen encontrado")
        st.write(f"Gen (binario): {best_overall[0]}")
        st.write(f"x (decimal): {binary_to_decimal(best_overall[0])}")
        st.write(f"f(x): {best_overall[1]:.4f}")

        st.subheader("Evolución por generación")
        st.dataframe(resultados, use_container_width=True)
