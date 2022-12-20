import cv2
vidcap = cv2.VideoCapture('sample_file/big_buck_bunny_720p_5mb.mp4')

success, image = vidcap.read()
count = 0

while success:
  cv2.imwrite("frame%d.jpg" % count, image)
  success, image = vidcap.read()
  print('Read a new Frame: ', success)
  count += 1
