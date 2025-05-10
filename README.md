# **Optimización de Rutas de Distribución de Pollos Hermanos en Lima**

## **Descripción del Proyecto**

Este proyecto tiene como objetivo **optimizar el sistema de distribución** de **Pollos Hermanos** en la ciudad de Lima, mediante el uso de técnicas de **optimización de rutas** y **análisis de grafos**. El sistema modela las pollerías y las rutas de distribución entre ellas utilizando un **grafo disperso**. A través de la optimización de las rutas, buscamos **reducir el tiempo de entrega**, **minimizar los costos operativos**, **asegurar la frescura del producto** y **mejorar la eficiencia logística**.

## **Estructura del Proyecto**

### **1. Grafo de Distribución**
El grafo creado en este proyecto representa la red de distribución entre **pollerías** en Lima. Las pollerías están representadas como **nodos** y las rutas de distribución entre ellas son las **aristas** del grafo. Se ha utilizado una representación **dispersa** para mostrar cómo están distribuidas las pollerías y sus conexiones.

### **2. Algoritmos Utilizados**
Para optimizar las rutas de distribución, se utilizaron los siguientes algoritmos y técnicas:
- **Técnicas de Recorrido y Búsquedas en Grafos (Dijkstra o A\*)**: Para encontrar las rutas más cortas entre pollerías.
- **Programación Dinámica (Problema del Viajante de Comercio - TSP)**: Para calcular la ruta más corta que pase por todas las pollerías.
- **Bellman-Ford**: Para optimizar rutas desde un único origen hacia todas las pollerías en la red.

### **3. Datos Generados**
El dataset contiene **1500 pollerías** distribuidas por Lima, con las siguientes características:
- **Nombres de las pollerías**: Combinación única de prefijos y sufijos para generar nombres de pollerías.
- **Coordenadas geográficas**: Generadas aleatoriamente dentro de los límites de Lima (latitud entre -12.20 y -11.90, longitud entre -77.15 y -76.90).
- **Distancias entre pollerías**: Calculadas aleatoriamente para simular las distancias de distribución.

### **4. Salida**
El proyecto genera un archivo Excel llamado **"rutas_pollerias_lima_1500_UNICAS.xlsx"** que contiene la siguiente información:
- **restaurante_inicio**: Nombre de la pollería de inicio.
- **restaurante_final**: Nombre de la pollería de destino.
- **restaurante_tiempo**: Tiempo estimado de entrega entre las pollerías.
- **lat_inicio** y **lon_inicio**: Coordenadas de la pollería de inicio.
- **lat_final** y **lon_final**: Coordenadas de la pollería de destino.
- **distancia_km**: Distancia entre las pollerías.

### **5. Visualización del Grafo**
La red de distribución entre las pollerías se puede visualizar como un **grafo disperso**. Cada pollería es un nodo, y las aristas representan las rutas de distribución entre ellas.

## **Tecnologías Utilizadas**
- **Python**: Lenguaje de programación utilizado para la implementación.
- **Pandas**: Para la manipulación y almacenamiento de los datos generados en formato Excel.
- **Matplotlib**: Para la visualización de grafos y distribución de pollerías (si es necesario).
- **Random**: Para la generación de nombres únicos y coordenadas aleatorias.
