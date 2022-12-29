#!/usr/bin/env python3
import cv2
import mediapipe as mp
import time
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands


def status(tips):

    
    val = Twist()

    if tips[4]==1 :
      val.linear.x = 0.8
      val.angular.z= 0
      # print("forward")
      pub.publish(val)

    if tips[4] == 0:
      #  val.linear.x = -0.8
       val.angular.z= 3
      #  print("backward")
       pub.publish(val)

def arm_pose(tips):
  # Tips = String()
  pub2.publish(tips)
  

def gestureTrack(tipids,marks):
    # this function tells the tips are opened or not of fingers
    fingUp = [] 
    if marks[tipids[0]][1] < marks[tipids[0] - 1][1]:
            fingUp.append(0)
    else:
            fingUp.append(1)
    for id in range(1, 5):
            if marks[tipids[id]][2] < marks[tipids[id] - 2][2]:
                fingUp.append(1)
            else:
                fingUp.append(0)

    return fingUp

    

# For webcam input:
cap = cv2.VideoCapture(0)
global pub
pub = rospy.Publisher('/robot_base_velocity_controller/cmd_vel', Twist, queue_size=10)

pub2 = rospy.Publisher("/arm", String, queue_size=10)
rospy.init_node('talker', anonymous=True)
rate = rospy.Rate(10) # 10
with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    marks = []

    if results.multi_hand_landmarks:
        myhand = results.multi_hand_landmarks[0]
        for ids, lm in enumerate(myhand.landmark):

            h, w, c = image.shape
            cx, cy = int(lm.x * w), int(lm.y * h)

            marks.append([ids, cx, cy])
      
        for handlms in results.multi_hand_landmarks:

            mp_drawing.draw_landmarks(
                image, handlms, mp_hands.HAND_CONNECTIONS)

        if (marks != 0):
            # print(marks[4])
            # print(marks[4])
            tipids =[4,8,12,16,20] # 4 for thumb,8 for index ,12 for middle, 16 for ring finger,20 for pinky finger
            tips = gestureTrack(tipids,marks)
            # print(tips) # tips is list of fingures which a up [thumb,index finger,middle finger,ring finger,pinky finger]
                        # 0 if it is folded 1 if it is open
            status(tips)
            tips = str(tips)
            arm_pose(tips)
            # print(tips)

        
    cv2.imshow('hand control', image)
    if cv2.waitKey(1) & 0xFF == ord("q"):
      break
cap.release()
