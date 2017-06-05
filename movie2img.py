
import sys, datetime, os, cv2

def main(movie, dstdir):
  if not os.path.exists(dstdir):
    os.mkdir(dstdir)
  cap = cv2.VideoCapture(movie)
  ret, frame = cap.read()
  prefix = datetime.datetime.now().strftime('%Y%m%d-%H%M%S_')
  counter = 0
  while ret:
    cv2.imshow("video", frame)
    filename = dstdir + "/" + prefix + str(counter) + ".jpg"
    cv2.imwrite(filename, frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
      break
    ret, frame = cap.read()
    counter += 1
  cap.release()
  cv2.destroyAllWindows()

if __name__ == '__main__':
  main(sys.argv[1], sys.argv[2])
