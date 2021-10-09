import matplotlib.pyplot as plt
import numpy as np
import os
labels = ['Butterfly', 'Chicken', 'Hourse', 'Lizard', 'Spider']

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


test_means = [number_WTest_list_Butterfly, number_WTest_list_Chicken, number_WTest_list_Hourse, number_WTest_list_Lizard, number_WTest_list_Spider]
train_means = [number_WTrain_list_Butterfly, number_WTrain_list_Chicken, number_WTrain_list_Hourse, number_WTrain_list_Lizard, number_WTrain_list_Spider]

x = np.arange(len(labels))  # lập list thứ tự các lable
#print(x)
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, test_means, width,color = 'blue', label='Test') 
rects2 = ax.bar(x + width/2, train_means, width,color = 'orange', label='Val')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Số lượng ảnh')
ax.set_title('Các loại động vật')
ax.set_xticks(x)# đánh dấu nhãn theo list x
ax.set_xticklabels(labels)#đánh dấu các trục bằng tên list labels
ax.legend() #hiện chú giải cho sơ đồ theo 2 rect

ax.bar_label(rects1, padding=3) #Đánh dấu số lượng ảnh trên cột với khoảng cách với cột = 3
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()