import os, sys, datetime, random, json
from subprocess import Popen, PIPE
from flask import Flask, g, request

base_dir = os.path.abspath(os.path.dirname(__file__) + '/')
sys.path.append(base_dir)

app = Flask(__name__)

dir_path = '/home/webmaster/Web_API/API/Paraphrase_Generator'
args = [
    '{}/Paraphrase/moses'.format(dir_path), '-f',
    '{}/Working/mert-work/moses.ini'.format(dir_path),
    '-n-best-list',
    '2',
]
proc = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)


@app.route('/paraphrase', methods=['POST'])
def annotate():
    data = request.get_json()
    sentence = data['sentence'] + '\n'
    proc.stdin.write(sentence.encode())
    proc.stdin.flush()
    result = proc.stdout.readline().decode()
    result = result.replace('\n', '')
    return json.dumps({
        'result': result,
    })


if __name__ == '__main__':
    FLASK_DEBUG = os.getenv('FLASK_DEBUG', True)
    app.run(host='0.0.0.0', debug=FLASK_DEBUG, port=8081)
