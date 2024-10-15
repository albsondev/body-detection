import cv2
import mediapipe as mp

# Inicializa o MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Inicializa o desenho para os landmarks
mp_drawing = mp.solutions.drawing_utils

# Acessar a webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Falha ao capturar a imagem.")
        break

    # Converte a imagem de BGR para RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Processa o frame para detectar os pontos do corpo
    results = pose.process(rgb_frame)

    # Desenha os pontos do corpo e as conexões
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # Exibe o frame com os pontos do corpo
    cv2.imshow('Detecção de Curvas do Corpo', frame)

    # Pressione 'q' para sair do loop
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# Libera a webcam e fecha as janelas
cap.release()
cv2.destroyAllWindows()
