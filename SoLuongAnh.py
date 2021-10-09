import os
import cv2
import matplotlib.pyplot as plt

"""Số lượng ảnh của các label"""
number_WTest_list_Butterfly = len(os.listdir('Train\Butterfly')) # dir is your directory path
number_WTest_list_Chicken = len(os.listdir('Train\Chicken'))
number_WTest_list_Hourse = len(os.listdir('Train\Horse'))
number_WTest_list_Lizard = len(os.listdir('Train\Lizard'))
number_WTest_list_Spider = len(os.listdir('Train\Spider'))

number_WTrain_list_Butterfly = len(os.listdir('Val\Butterfly')) # dir is your directory path
number_WTrain_list_Chicken = len(os.listdir('Val\Chicken'))
number_WTrain_list_Hourse = len(os.listdir('Val\Horse'))
number_WTrain_list_Lizard = len(os.listdir('Val\Lizard'))
number_WTrain_list_Spider = len(os.listdir('Val\Spider'))


print (number_WTest_list_Butterfly)