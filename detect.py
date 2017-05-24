import cv2
import tensorflow.contrib.keras as keras
from keras.models import model_from_json
from sense_hat import SenseHat

def main(cascade_path='/home/pi/opencv-3.1.0/data/haarcascades/haarcascade_frontalface_alt.xml'):
  sense = SenseHat()
  fp = open('./model.json', 'r')
  buf = fp.read()
  fp.close()
  print(buf)
  model = model_from_json(buf)
  model.load_weights('./weights.hdf5')
  cascade = cv2.CascadeClassifier(cascade_path)
  winname = "camera"
  cv2.namedWindow(winname, cv2.WINDOW_AUTOSIZE)
  cap = cv2.VideoCapture(0)
  cap.set(3, 640)
  cap.set(4, 480)
  while True:
    found = False
    ret, frame = cap.read()
    if ret == False:
      break
    frect = cascade.detectMultiScale(frame, minSize=(32, 32))
    if len(frect) > 0:
      for r in frect:
        x, y, w, h = r[0], r[1], r[2], r[3]
        face = frame[y:y+h, x:x+w]
        if len(face) != 0:
          if w > 0 and h > 0:
            face = cv2.resize(face, (32, 32))
            face = cv2.cvtColor(face, cv2.COLOR_RGB2GRAY)
            face = face.reshape(1,32, 32, 1) / 255.
            score = model.predict_on_batch(face)
            print(score)
            color = (255, 0, 0)
            width = 2 
            if score[0][1] > 0.5:
              color = (0, 0, 255)
              width = 8
              found = True
            cv2.rectangle(frame, (x,y),(x+w,y+h), color, width)
    cv2.imshow(winname, frame)
    if found:
      sense.show_message("manattan", scroll_speed=0.01)
    else:
      sense.clear()
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  cap.release()
  cv2.destroyWindow(winname)

if __name__ == '__main__':
  main()
