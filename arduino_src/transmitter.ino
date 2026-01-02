#include <SPI.h>
#include <RF24.h>

RF24 radio(9, 10);
const byte address[6] = "00001";

const int voltagePin = A0;
const int currentPin = A1;
const int currentPin2 = A2;

const float zeroCurrentVoltage = 2.5;
const float sensitivity = 0.100;

struct SensorData {
  float voltage;
  float current;
  float current2;
};

void setup() {
  radio.begin();
  radio.setPALevel(RF24_PA_LOW);
  radio.setDataRate(RF24_250KBPS);
  radio.setChannel(76);
  radio.openWritingPipe(address);
  radio.stopListening();
  radio.setAutoAck(true);
}

void loop() {
  SensorData data;

  int rawV = analogRead(voltagePin);
  float voltageOut = (rawV * 5.0) / 1023.0;
  data.voltage = voltageOut * 5.0;

  int rawI = analogRead(currentPin);
  float sensorVoltage = (rawI * 5.0) / 1023.0;
  data.current = (sensorVoltage - zeroCurrentVoltage) / sensitivity;

  int rawI2 = analogRead(currentPin2);
  float sensorVoltage2 = (rawI2 * 5.0) / 1023.0;
  data.current2 = (sensorVoltage - zeroCurrentVoltage) / sensitivity;

  bool ok = radio.write(&data, sizeof(data));

  delay(1000);
}
