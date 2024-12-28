// Código para Arduino
const int LED_PIN = 13;  // LED integrado en la placa

void setup() {
  Serial.begin(9600);     // Iniciar comunicación serial
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    char comando = Serial.read();
    if (comando == '1') {
      digitalWrite(LED_PIN, HIGH);
      Serial.println("LED encendido");
    }
    else if (comando == '0') {
      digitalWrite(LED_PIN, LOW);
      Serial.println("LED apagado");
    }
  }
}
