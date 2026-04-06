
import mediapipe as mp
import cv2
import time

class faceMeshDetector ():
    def __init__(self,static_mode=False,max_faces=2,minDetectioncon=.5,mintrackcon=.5):
        self.static_mode=static_mode
        self.max_faces=max_faces
        self.minDetectioncon=minDetectioncon
        self.mintrackcon=mintrackcon
        self.mpface_mesh=mp.solutions.face_mesh
        self.face_mesh = self.mpface_mesh.FaceMesh(
            static_image_mode=self.static_mode,
            max_num_faces=self.max_faces,
            min_detection_confidence=self.minDetectioncon,
            min_tracking_confidence=self.mintrackcon
        )
        self.mpDraw=mp.solutions.drawing_utils
        self.drawspec=self.mpDraw.DrawingSpec(thickness=2,circle_radius=2)
    def findMeshFaces(self,frame,draw=True):
        

        RGBimg = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(RGBimg)
        faces = []

        if results.multi_face_landmarks:
            for face in results.multi_face_landmarks:

                if draw:
                    self.mpDraw.draw_landmarks(
                        frame,
                        face,
                        self.mpface_mesh.FACEMESH_TESSELATION,
                        self.drawspec,
                        self.drawspec
                    )

                facepos = []
                ih, iw, c = frame.shape

                for lm in face.landmark:
                    x, y = int(lm.x * iw), int(lm.y * ih)
                    facepos.append([x, y])

                faces.append(facepos)
        return frame,faces



                        


def main():
    detector=faceMeshDetector()
    

    ptime = 0
    cap = cv2.VideoCapture("WIN_20260329_15_33_09_Pro.mp4")
    while True :
        success, frame = cap.read()
        if not success:
           print("error while opening the camera")
           break
        frame,positions=detector.findMeshFaces(frame,True)
        if len(positions)!=0:
            print(len(positions))



        ctime = time.time()

        fps = 1 / (ctime - ptime) if (ctime - ptime) > 0 else 0
        ptime = ctime
        cv2.putText(frame, str(int(fps)), (10, 50), 2, 1, (255, 0, 255), 3)
        cv2.imshow("faces mesh ", frame)
        if cv2.waitKey(10) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()



if __name__=="__main__":
    main()

