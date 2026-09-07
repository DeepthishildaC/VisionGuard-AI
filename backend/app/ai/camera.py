import cv2


def open_camera(camera_index=0):
    """
    Open webcam.
    """

    cap = cv2.VideoCapture(camera_index)

    if not cap.isOpened():
        raise Exception("Cannot open camera")

    return cap