import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

print("Choose mode:")
print("1: Image input")
print("2: Live webcam")
choice = input("Enter 1 or 2: ")

def detect_mood(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.7, minNeighbors=20)

        if len(smiles) > 0:
            mood = "Happy"
        else:
            mood = "Neutral/Sad"

        cv2.putText(frame, mood, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    return frame

if choice == "1":
    image_path = input("Enter image path: ")
    frame = cv2.imread(image_path)
    if frame is None:
        print("Image not found!")
        exit()
    frame = detect_mood(frame)
    cv2.imshow("Mood Detection", frame)
    # Save the detected image
    output_path = "mood_detected.jpg"
    cv2.imwrite(output_path, frame)
    print(f"Image saved as {output_path}")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

elif choice == "2":
    cap = cv2.VideoCapture(0)
    save_video = input("Do you want to save the webcam output? (y/n): ").lower()
    if save_video == 'y':
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter("webcam_mood_detected.mp4", fourcc, 20.0, 
                              (int(cap.get(3)), int(cap.get(4))))
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = detect_mood(frame)
        cv2.imshow("Mood Detection", frame)
        if save_video == 'y':
            out.write(frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cap.release()
    if save_video == 'y':
        out.release()
        print("Webcam video saved as webcam_mood_detected.mp4")
    cv2.destroyAllWindows()

else:
    print("Invalid choice!")
