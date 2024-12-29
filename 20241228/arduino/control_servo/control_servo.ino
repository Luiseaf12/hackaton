#include <Servo.h>

Servo miServo;  // Crear objeto servo
int pinServo = 9;  // Pin PWM para el servo

void setup() {
  miServo.attach(pinServo);  // Conectar el servo al pin 9
  Serial.begin(9600);  // Iniciar comunicación serial
}

void loop() {
  if (Serial.available() > 0) {
    int angulo = Serial.parseInt();  // Leer el ángulo desde Python
    if (angulo >= 0 && angulo <= 180) {
      miServo.write(angulo);  // Mover el servo al ángulo especificado
      Serial.println("Movido a: " + String(angulo) + " grados");
    }
  }
}
