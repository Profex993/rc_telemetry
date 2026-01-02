#include <SPI.h>
#include <RF24.h>

RF24 radio(9, 10);
const byte address[6] = "00001";

struct SensorData {
  float voltage;
  float current;
  float current2;
};

void setup() {
  Serial.begin(9600);
  radio.begin();
  radio.setPALevel(RF24_PA_LOW);
  radio.setDataRate(RF24_250KBPS);
  radio.setChannel(76);
  radio.openReadingPipe(0, address);
  radio.startListening();
}

void loop() {
  if (radio.available()) {
    SensorData data;
    radio.read(&data, sizeof(data));
    Serial.print(data.voltage); Serial.print(",");
    Serial.print(data.current); Serial.print(",");
    Serial.println(data.current2);
  }
}
