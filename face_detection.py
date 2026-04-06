
import mediapipe as mp
import cv2
import time

class faceDetector():
    def __init__(self,  minDetectionConf=.5):
        self.minDetectionConf=minDetectionConf
        self.mpface = mp.solutions.face_detection
        self.face = self.mpface.FaceDetection(minDetectionConf)
        self.mpDraw = mp.solutions.drawing_utils
    def findfaces(self, frame, draw=True):
        RGBimg=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        self.results=self.face.process(RGBimg)
        bboxs=[]
        if self.results.detections:
            for id,detection in enumerate(self.results.detections):
            #print(id,detection)
            #mpDraw.draw_detection(frame,detection)
            #print(detection.score)
            #print(detection.location_data.relative_bounding_box)
                bboxc = detection.location_data.relative_bounding_box
                ih, iw, c = frame.shape

                bbox = (
                    int(bboxc.xmin * iw),
                    int(bboxc.ymin * ih),
                    int(bboxc.width * iw),
                    int(bboxc.height * ih)
                )

                x, y, w, h = bbox

                if draw:
                    self.draw_coreners(frame,bbox)
                    
                    cv2.putText(frame, f"{int(detection.score[0]*100)} %",
                                (x, y - 30),
                                cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)

                bboxs.append([id, bbox, detection.score[0]])
        return frame,bboxs
    
    def draw_coreners(self,frame,bbox,l=30):
        x,y,w,h=bbox

        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 255), 3)
        cv2.line(frame,(x,y),(x+l,y),(255,0,255),10)
        cv2.line(frame,(x,y),(x,y+l),(255,0,255),10)

        cv2.line(frame,(x,y+h),(x+l,y+h),(255,0,255),10)
        cv2.line(frame,(x,y+h),(x,y+h-l),(255,0,255),10)

        cv2.line(frame,(x+w,y),(x+w-l,y),(255,0,255),10)
        cv2.line(frame,(x+w,y),(x+w,y+l),(255,0,255),10)

        cv2.line(frame,(x+w,y+h),(x+w-l,y+h),(255,0,255),10)
        cv2.line(frame,(x+w,y+h),(x+w,y+h-l),(255,0,255),10)


     
        return frame

def main():
    ptime = 0
    cap = cv2.VideoCapture("WIN_20260329_15_33_09_Pro.mp4")
    obj=faceDetector(.4)
    while True:
        success, frame = cap.read()
        if not success:
            print("error while opening the camera")
            break
        frame,faces=obj.findfaces(frame)
        



        ctime = time.time()
        fps = 1 / (ctime - ptime) if (ctime - ptime) > 0 else 0
        ptime = ctime

        cv2.putText(frame, str(int(fps)), (10, 50), 2, 1, (255, 0, 255), 3)

        cv2.imshow("faces detection ", frame)
    

        if cv2.waitKey(10) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()