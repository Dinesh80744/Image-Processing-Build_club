#Task 2 
#Opening web cam
import cv2
cam = cv2.VideoCapture(0)
width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cam.get(cv2.CAP_PROP_FPS))
output_file = 'recording.MP4' 
output = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*'MJPG'), fps,(width, height))

while True:
 _ , frame = cam.read() 
 cv2.imshow('Webcam', frame) 
 print('resolution:',width, 'x', height, '| frames per second:', fps)
 if cv2.waitKey(1) & 0xff == ord('q'):
    break
cam.release()
output.release()
cv2.destroyAllWindows()