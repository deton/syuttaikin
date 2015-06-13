#include <Servo.h> 
const int SERVOPIN = 3;
Servo servo;

// accept command from MPU for Arduino Yun/Linino ONE
#define CMD_FROM_MPU 1
#ifdef CMD_FROM_MPU  // accept command from MPU for Arduino Yun/Linino ONE
#include <Console.h>
#define Serial Console
#endif

void setup() {
#ifdef CMD_FROM_MPU
  Bridge.begin(115200);
  Console.begin();
#else
  Serial.begin(9600);
#endif
  servo.attach(SERVOPIN);
}

void loop() {
  if (Serial.available()) {
    int c = Serial.read();
    switch (c) {
    case '0':
      Serial.println("0");
      servo.write(5); // 0-3 is not silent
      break;
    case '1':
      Serial.println("1");
      servo.write(90);
      break;
    default:
      break;
    }
  }
}
