// ================== LANE 1 LEDs ==================
#define R1 8
#define Y1 9
#define G1 10

// ================== LANE 2 LEDs ==================
#define R2 11
#define Y2 12
#define G2 13

// ================== HC-SR04 ==================
#define TRIG1 3
#define ECHO1 4

#define TRIG2 5
#define ECHO2 6

// ================== FS-i6 ==================
#define AMBULANCE_PIN 2

// ============================================
long getDistance(int trigPin, int echoPin)
{
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);

  digitalWrite(trigPin, LOW);

  long duration = pulseIn(echoPin, HIGH, 30000);

  if(duration == 0)
    return 200;

  return duration * 0.034 / 2;
}

// ============================================
void lane1Green(int greenTime)
{
  // Lane 1 Green
  digitalWrite(R1, LOW);
  digitalWrite(Y1, LOW);
  digitalWrite(G1, HIGH);

  digitalWrite(R2, HIGH);
  digitalWrite(Y2, LOW);
  digitalWrite(G2, LOW);

  delay(greenTime);

  // Lane 1 Yellow
  digitalWrite(G1, LOW);
  digitalWrite(Y1, HIGH);

  delay(3000);

  digitalWrite(Y1, LOW);
  digitalWrite(R1, HIGH);
}

// ============================================
void lane2Green(int greenTime)
{
  // Lane 2 Green
  digitalWrite(R2, LOW);
  digitalWrite(Y2, LOW);
  digitalWrite(G2, HIGH);

  digitalWrite(R1, HIGH);
  digitalWrite(Y1, LOW);
  digitalWrite(G1, LOW);

  delay(greenTime);

  // Lane 2 Yellow
  digitalWrite(G2, LOW);
  digitalWrite(Y2, HIGH);

  delay(3000);

  digitalWrite(Y2, LOW);
  digitalWrite(R2, HIGH);
}

// ============================================
void ambulancePriority()
{
  Serial.println("AMBULANCE DETECTED");

  // Give Lane 1 priority
  digitalWrite(R1, LOW);
  digitalWrite(Y1, LOW);
  digitalWrite(G1, HIGH);

  digitalWrite(R2, HIGH);
  digitalWrite(Y2, LOW);
  digitalWrite(G2, LOW);

  delay(10000);

  digitalWrite(G1, LOW);
  digitalWrite(Y1, HIGH);

  delay(3000);

  digitalWrite(Y1, LOW);
  digitalWrite(R1, HIGH);
}

// ============================================
void setup()
{
  pinMode(R1, OUTPUT);
  pinMode(Y1, OUTPUT);
  pinMode(G1, OUTPUT);

  pinMode(R2, OUTPUT);
  pinMode(Y2, OUTPUT);
  pinMode(G2, OUTPUT);

  pinMode(TRIG1, OUTPUT);
  pinMode(ECHO1, INPUT);

  pinMode(TRIG2, OUTPUT);
  pinMode(ECHO2, INPUT);

  pinMode(AMBULANCE_PIN, INPUT);

  Serial.begin(9600);

  // Initial State
  digitalWrite(R1, HIGH);
  digitalWrite(R2, HIGH);
}

// ============================================
void loop()
{
  long lane1Distance = getDistance(TRIG1, ECHO1);
  long lane2Distance = getDistance(TRIG2, ECHO2);

  int pulseWidth = pulseIn(AMBULANCE_PIN, HIGH, 25000);

  Serial.print("Lane1=");
  Serial.print(lane1Distance);

  Serial.print("  Lane2=");
  Serial.print(lane2Distance);

  Serial.print("  PWM=");
  Serial.println(pulseWidth);

  // Ambulance Override
  if(pulseWidth > 1500)
  {
    ambulancePriority();
    return;
  }

  // Invalid readings
  if(lane1Distance == 0)
    lane1Distance = 200;

  if(lane2Distance == 0)
    lane2Distance = 200;

  // More vehicles = smaller distance
  if(lane1Distance < lane2Distance)
  {
    if(lane1Distance < 10)
      lane1Green(15000);

    else if(lane1Distance < 20)
      lane1Green(10000);

    else
      lane1Green(5000);
  }
  else
  {
    if(lane2Distance < 10)
      lane2Green(15000);

    else if(lane2Distance < 20)
      lane2Green(10000);

    else
      lane2Green(5000);
  }
}
