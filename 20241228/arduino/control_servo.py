import serial
import time
from flask import Flask, jsonify, request

app = Flask(__name__)

# Configurar la conexión serial
arduino = serial.Serial('COM6', 9600, timeout=1)
time.sleep(2)  # Esperar a que se establezca la conexión

def mover_servo(angulo):
    """
    Mueve el servo a un ángulo específico entre 0 y 180 grados
    """
    if 0 <= angulo <= 180:
        arduino.write(str(angulo).encode())
        time.sleep(0.1)  # Esperar a que el servo se mueva
        respuesta = arduino.readline().decode().strip()
        return respuesta
    else:
        return "El ángulo debe estar entre 0 y 180 grados"

@app.route('/servo/<int:angulo>', methods=['GET'])
def control_servo(angulo):
    respuesta = mover_servo(angulo)
    return jsonify({
        'status': 'success',
        'angulo': angulo,
        'respuesta': respuesta
    })

@app.route('/')
def home():
    return '''
    <h1>Control de Servomotor</h1>
    <p>Usa /servo/[angulo] para mover el servo.</p>
    <p>Ejemplo: <a href="/servo/90">/servo/90</a> para mover a 90 grados</p>
    '''

@app.route('/tamarindo')
def tamarindo():
    return '''
    <h1>Caen tamarindos</h1>
    <p>Usa /tamarindo/[numero] cuantos tamarindos caen.</p>
    <p>Ejemplo: <a href="/tamarindo/90">/tamarindo/90</a> para mover a 90 grados</p>
    '''

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    finally:
        arduino.close()  # Cerrar la conexión serial cuando se detenga el servidor
