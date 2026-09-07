import cv2

from app.ai.camera import open_camera


cap = open_camera()

while True:

    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("VisionGuard Camera", frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

cap.release()

cv2.destroyAllWindows()