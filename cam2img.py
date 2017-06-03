import os
import sys
import cv2
import time
from datetime import datetime, timedelta

def main(destdir):
  winname = "camera view"
  cv2.namedWindow(winname, cv2.WINDOW_AUTOSIZE)
  cap = cv2.VideoCapture(0)
  cap.set(3, 640)
  cap.set(4, 480)
  if not os.path.exists(destdir):
    os.mkdir(destdir)
  prefix = datetime.now().strftime('%Y%m%d-%H%M%S_')
  counter = 0
  lastupdate = datetime.now()
  while True:
    ret, frame = cap.read()
    if ret == False:
      break
    cv2.imshow(winname, frame)
    if datetime.now() - lastupdate > timedelta(seconds=2):
      filename = destdir + "/" + prefix + str(counter) + ".jpg"
      cv2.imwrite(filename, frame)
      print(filename)
      lastupdate = datetime.now()
      counter += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  cap.release()
  cv2.destroyWindow(winname)

if __name__ == '__main__':
  main(sys.argv[1])
