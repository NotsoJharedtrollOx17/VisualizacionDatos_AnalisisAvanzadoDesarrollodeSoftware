import random
import numpy as np
import seaborn as sns
import matplotlib.cm as cm
import matplotlib.pyplot as plt

#sns.set(context="talk")

def get40RespuestasReactivos(n, total):
    if n <= 0 or total <= 0:
        return None
    
    lista = []
    for _ in range(n - 1):
        num = random.randint(1, total - (n - len(lista)) + 1)
        lista.append(num)
        total -= num
    lista.append(total)
    
    return lista

def getListaReactivos():
    
    reactivos = [
        ['a)', 'b)', 'c)', 'd)'],
        ['a)', 'b)', 'c)', 'd)'],
        ['a)', 'b)', 'c)'],
        ['a)', 'b)'],
        ['a)', 'b)'],
        ['a)', 'b)'],
        ['a)', 'b)', 'c)', 'd)'],
        ['a)', 'b)'],
        ['a)', 'b)'],
        ['a)', 'b)', 'c)', 'd)', 'e)']
    ]
    
    return reactivos

def getHistograma(idx, cantidades_respuestas, incisos_respuestas, max_yval):
    nombre_archivo = f"histograma_pregunta{idx+1}"
    
    print(f"INICIO Histograma {nombre_archivo}")
    colores = [cm.viridis(v) for v in np.linspace(0, 1, len(incisos_respuestas))]
    fig, axes = plt.subplots(figsize=(10, 6))
    bars = axes.bar(incisos_respuestas, cantidades_respuestas, alpha=0.7, color=colores)
    axes.set_xlabel("Inciso de respuesta", fontsize=11)
    axes.set_ylabel("Cantidad", fontsize=11)
    axes.set_title(f"Histograma Pregunta {1}", fontsize=12)
    axes.set_ylim(0, max_yval) # * Limite de escala
    axes.yaxis.set_major_locator(plt.MaxNLocator(integer=True)) # * Forzar la escala vertical a números enteros
    
    # * Agregar números en las barras
    for bar, count in zip(bars, cantidades_respuestas):
        axes.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            str(count),
            ha="center",
            va="bottom",
        )
        
    plt.savefig(f"./plots/{nombre_archivo}")
    plt.close()
    print(f"GRAFICA {nombre_archivo} realizada con éxito!")
    print(f"FIN Histograma {nombre_archivo}")

def main():
    CUARENTA = 40
    
    reactivos = getListaReactivos()
    
    print("Generación de respuestas de preguntas")
    for idx, respuestas in enumerate(reactivos):
        cantidad_respuestas = get40RespuestasReactivos(len(respuestas), CUARENTA)
        
        print(f"\nPregunta {idx+1}: ")
        print(f"Respuestas: {cantidad_respuestas}")
        for id_inciso, inciso in enumerate(respuestas):
            print(f"{inciso}: {cantidad_respuestas[id_inciso]}")
        getHistograma(idx, cantidad_respuestas, respuestas, CUARENTA)
        
if __name__ == '__main__':
    main()