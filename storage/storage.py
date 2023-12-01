from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/images/<path:filename>')
def download_file(filename):
    return send_from_directory('images', filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)