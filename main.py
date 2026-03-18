import sys

tareas = []
with open("tareas.txt") as f:
    for linea in f.readlines():
        partes = linea.strip().split(",")
        tareas.append((partes[0], int(partes[1]), partes[2]))

recursos = []
with open("recursos.txt") as f:
    for linea in f.readlines():
        partes = linea.strip().split(",")
        recursos.append((partes[0], set(partes[1:])))

tareas_ordenadas = sorted(tareas, key=lambda t: t[1], reverse=True)

tiempo_recurso = {}
for rid, cats in recursos:
    tiempo_recurso[rid] = 0

resultado = []

for tarea_id, duracion, categoria in tareas_ordenadas:
    mejor_recurso = None
    menor_tiempo = 999999
    for rid, cats in recursos:
        if categoria in cats:
            if tiempo_recurso[rid] < menor_tiempo:
                menor_tiempo = tiempo_recurso[rid]
                mejor_recurso = rid
    inicio = tiempo_recurso[mejor_recurso]
    fin = inicio + duracion
    tiempo_recurso[mejor_recurso] = fin
    resultado.append((tarea_id, mejor_recurso, inicio, fin))

with open("output.txt", "w") as f:
    for tarea_id, rid, inicio, fin in resultado:
        f.write(tarea_id + "," + rid + "," + str(inicio) + "," + str(fin) + "\n")