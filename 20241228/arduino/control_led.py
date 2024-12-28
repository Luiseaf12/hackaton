import serial
import time

# Configura el puerto serial (ajusta 'COM3' según tu puerto)
arduino = serial.Serial('COM6', 9600, timeout=1)
time.sleep(2)  # Espera a que se establezca la conexión

def controlar_led(estado):
    if estado:
        arduino.write(b'1')  # Envía '1' para encender
    else:
        arduino.write(b'0')  # Envía '0' para apagar
    
    # Lee la respuesta del Arduino
    respuesta = arduino.readline().decode().strip()
    print(f"Arduino dice: {respuesta}")

try:
    while True:
        comando = input("Escribe '1' para encender, '0' para apagar, 'q' para salir: ")
        if comando == 'q':
            break
        elif comando in ['0', '1']:
            controlar_led(comando == '1')
        else:
            print("Comando no válido")

except KeyboardInterrupt:
    print("\nPrograma terminado")
finally:
    arduino.close()  # Cierra la conexión serial
