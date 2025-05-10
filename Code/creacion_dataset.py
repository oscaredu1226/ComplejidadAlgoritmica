import pandas as pd
import random

prefijos = ["El Buen", "Don", "Señor", "La Gran", "Súper", "Pollos", "Brasa", "La Casa", "Rincón", "Tradición"]
sufijos = ["Sabor", "Pollo", "Brasas", "Familia", "Delicia", "Pechuga", "Punto", "Real", "Lima", "Andina"]

lat_min, lat_max = -12.20, -11.90
lon_min, lon_max = -77.15, -76.90

pollerias = set()  

while len(pollerias) < 1500:
    nombre = f"Pollería {random.choice(prefijos)} {random.choice(sufijos)}"
    lat = round(random.uniform(lat_min, lat_max), 6)
    lon = round(random.uniform(lon_min, lon_max), 6)
    

    pollerias.add((nombre, lat, lon))


pollerias = list(pollerias)


resultados = []
for i in range(len(pollerias) - 1):
    nombre_a, lat_a, lon_a = pollerias[i]
    nombre_b, lat_b, lon_b = pollerias[i + 1]
    
    distancia_km = round(random.uniform(1.0, 10.0), 2)
    tiempo_min = round(distancia_km * 60 / 30, 2)  
    
    resultados.append({
        "restaurante_inicio": nombre_a,
        "restaurante_final": nombre_b,
        "restaurante_tiempo": tiempo_min,
        "lat_inicio": lat_a,
        "lon_inicio": lon_a,
        "lat_final": lat_b,
        "lon_final": lon_b,
        "distancia_km": distancia_km
    })

df = pd.DataFrame(resultados)
df.to_excel("rutas_pollerias_lima_1500_UNICAS.xlsx", index=False)
print("Dataset generado correctamente: rutas_pollerias_lima_1500_UNICAS.xlsx")
