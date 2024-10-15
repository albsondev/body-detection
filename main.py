from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

# Captura de vídeo da webcam
camera = cv2.VideoCapture(0)

def gen_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            # Aqui você pode adicionar a detecção do mediapipe no frame
            # Processa o frame para detecção corporal (mediapipe)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            # Retorna o frame via streaming para o navegador
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    # Video streaming via feed
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='192.168.1.106', port=5000)
