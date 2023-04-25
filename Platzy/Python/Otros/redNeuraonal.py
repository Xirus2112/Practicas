import tensorflow as tf
import numpy as np


# Declarando los arreglos con los grados celsius y fahrenheit
celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

# Keras para crear la red neural de manera simple
# Espesificando la capa de salida nada mas ahorrandonos un paso con Keras
capa = tf.keras.layers.Dense(units=1, input_shape=[1])
modelo = tf.keras.Sequential([capa])

#modelo de capa para probar el nivel de error que mostrara
modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)

print("Comenzando entrenamiento..!")
historial = modelo.fit(celsius, fahrenheit, epochs=1000, verbose=False)
print("Modelo entrenado..!")


#Imprimiendo la grafica
import matplotlib.pylot as plt
plt.xlabel("# Epoca")
plt.ylabel("Magnitud de pérdida")
plt.plot(historial.history["loss"])
