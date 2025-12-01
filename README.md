
##Gesture-Based Text Recognition and Vocalizer System

##  Overview
A smart glove-based system that translates hand gestures into text and speech in real-time, designed to assist deaf and mute individuals in communicating with non-sign language users. The project integrates both word-level gesture recognition using Arduino and sensors, and fingerspelling recognition using a CNN-based deep learning model.

##  Features
- Word-Level Gesture Vocalizer**: Uses flex sensors, MPU6050 accelerometer, and Arduino to detect gestures and output pre-defined words
- **Fingerspelling ASL Recognition**: CNN model trained to recognize American Sign Language (ASL) alphabets from webcam input
- **Real-Time Text & Speech Output**: Converts gestures to text and speech via Bluetooth and mobile app
- **Autocorrect Feature**: Uses Hunspell Suggest to correct spelling errors
- **High Accuracy**: Model achieves 93% accuracy with 95.19% precision

##  Technologies Used
- **Hardware**: Arduino UNO, MPU6050, HC-05 Bluetooth, Flex Sensors
- **Software**: Python, TensorFlow, Keras, OpenCV, Arduino IDE
- **Libraries**: NumPy, Matplotlib, Hunspell, scikit-learn

## Team Members
Anikate Verma 

Arghyadeep Ghosh 

Ashish Joshi 

## Guide
Dr. Astha Sharma
Associate Professor, Dept. of ECE
G.L. Bajaj Institute of Technology and Management

## References
Project Report (KEC-851), Academic Session 2021-22

American Sign Language (ASL) dataset

Research papers on gesture recognition and CNN

