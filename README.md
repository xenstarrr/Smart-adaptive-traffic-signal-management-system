# 🚦 Smart Adaptive Traffic Signal Management System with Ambulance Priority

##TEAM NAME
[ Schrodinger's coders]

##TEAM MEMBERS
Shraddha Binish
Mehal Ramesh
Subhash Raj 
Meghana S
Tanoj S

## 📌 Overview

The Smart Adaptive Traffic Signal Management System is an intelligent traffic control solution designed to reduce traffic congestion and improve emergency vehicle response time. The system dynamically adjusts traffic signal timings based on real-time traffic density using HC-SR04 ultrasonic sensors and provides priority access to ambulances using a FlySky FS-i6 wireless communication system.

This project demonstrates how low-cost embedded systems can be used to develop efficient traffic management solutions for smart cities.

---

## 🎯 Problem Statement

Traditional traffic signals operate on fixed timing schedules regardless of the actual traffic conditions. This leads to:

* Increased traffic congestion
* Unnecessary waiting time
* Fuel wastage
* Increased pollution
* Delays for emergency vehicles

An intelligent traffic management system is required to optimize signal timing according to traffic density and provide priority for emergency vehicles.

---

## 💡 Proposed Solution

The proposed system uses:

* HC-SR04 ultrasonic sensors to estimate traffic density in each lane.
* Arduino Uno as the central controller.
* Traffic signal LEDs to represent traffic lights.
* FlySky FS-i6 transmitter and receiver for ambulance detection and priority control.

The controller continuously monitors traffic density and dynamically allocates green signal duration to the lane with higher traffic density. In case of an emergency vehicle, the system immediately overrides normal operation and creates a green corridor.

---

## ⚙️ Features

✅ Adaptive Traffic Signal Control

✅ Real-Time Traffic Density Monitoring

✅ Ambulance Priority System

✅ Dynamic Green Signal Timing

✅ Low Cost and Easy Implementation

✅ Scalable Smart City Solution

---

## 🛠 Hardware Components

| Component                 | Quantity    |
| ------------------------- | ----------- |
| Arduino Uno               | 1           |
| HC-SR04 Ultrasonic Sensor | 2           |
| FlySky FS-i6 Transmitter  | 1           |
| FlySky Receiver           | 1           |
| Red LEDs                  | 2           |
| Yellow LEDs               | 2           |
| Green LEDs                | 2           |
| Breadboard                | 1           |
| Jumper Wires              | As Required |
| 220Ω Resistors            | 6           |

---

## 🔌 Pin Connections

### Traffic Signals

| Component         | Arduino Pin |
| ----------------- | ----------- |
| Red LED Lane 1    | D8          |
| Yellow LED Lane 1 | D9          |
| Green LED Lane 1  | D10         |
| Red LED Lane 2    | D11         |
| Yellow LED Lane 2 | D12         |
| Green LED Lane 2  | D13         |

### Ultrasonic Sensors

#### Lane 1

| HC-SR04 Pin | Arduino Pin |
| ----------- | ----------- |
| TRIG        | D3          |
| ECHO        | D4          |

#### Lane 2

| HC-SR04 Pin | Arduino Pin |
| ----------- | ----------- |
| TRIG        | D5          |
| ECHO        | D6          |

### Ambulance Detection

| FS-i6 Receiver Pin | Arduino Pin |
| ------------------ | ----------- |
| Signal             | D2          |
| VCC                | 5V          |
| GND                | GND         |

---

## 🏗 System Architecture

```text
Lane 1 Vehicles
       │
       ▼
HC-SR04 Sensor 1
       │
       ▼

                Arduino Uno
                     │
                     ▼

HC-SR04 Sensor 2
       ▲
       │
Lane 2 Vehicles

                     │
                     ▼

            Traffic Signals

                     ▲
                     │

         FS-i6 Receiver
                     ▲
                     │

         FS-i6 Transmitter
               (Ambulance)
```

---

## 🔄 Working Principle

### Traffic Density Detection

The ultrasonic sensors measure the distance between the sensor and the nearest vehicle.

* Smaller Distance = Higher Traffic Density
* Larger Distance = Lower Traffic Density

The Arduino compares the density values of both lanes and allocates green signal timing accordingly.

---

### Adaptive Signal Timing

| Density Level  | Green Time |
| -------------- | ---------- |
| High Density   | 15 Seconds |
| Medium Density | 10 Seconds |
| Low Density    | 5 Seconds  |

Yellow signal duration:

* 3 Seconds

---

### Ambulance Priority

The FlySky FS-i6 transmitter is used to simulate an ambulance.

When the ambulance approaches:

1. The transmitter sends a wireless signal.
2. The receiver detects the signal.
3. The Arduino overrides normal traffic operation.
4. The ambulance lane receives a green signal.
5. Other lanes receive a red signal.
6. After the ambulance passes, normal operation resumes.

---

## 💻 Software

### Programming Language

* Arduino C++

### Development Environment

* Arduino IDE

### Libraries Used

* Standard Arduino Functions
* pulseIn()
* digitalWrite()
* pinMode()

---

## 📂 Project Structure

```text
Smart-Adaptive-Traffic-Signal-System/
│
├── README.md
├── Arduino_Code/
│   └── traffic_signal.ino
│
├── Circuit_Diagram/
│   └── circuit.png
│
├── Images/
│   ├── setup.jpg
│   ├── working1.jpg
│   └── working2.jpg
│
└── Presentation/
    └── Project_Presentation.pptx
```
#Source Code
[View Source Code](code/main.py)

---

## 🚀 Future Enhancements

* AI-Based Vehicle Detection
* Camera-Based Traffic Monitoring
* GPS Ambulance Tracking
* IoT-Based Monitoring System
* Cloud Analytics Dashboard
* Four-Way Junction Implementation
* Automatic Number Plate Recognition

---

## 🌍 Applications

* Smart Cities
* Urban Traffic Management
* Emergency Vehicle Routing
* Highway Intersections
* Intelligent Transportation Systems

---

## ✅ Advantages

* Reduces Traffic Congestion
* Minimizes Waiting Time
* Improves Emergency Response
* Cost Effective
* Easy to Implement
* Energy Efficient
* Scalable Design

---

## 📊 Results

The system successfully:

* Detects traffic density using ultrasonic sensors.
* Dynamically adjusts signal timing.
* Provides ambulance priority.
* Reduces unnecessary waiting time.
* Improves overall traffic flow efficiency.

---

## 📜 License

This project is developed for educational and hackathon purposes.

---

## 🙏 Acknowledgement

We would like to thank our faculty mentors, institution, and teammates for their guidance and support throughout the development of this project.

---

### Smart Traffic Today, Smarter Cities Tomorrow 🚦
