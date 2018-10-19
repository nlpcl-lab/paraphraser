import os, sys, datetime, random, json
from subprocess import Popen, PIPE
from flask import Flask, g, request

base_dir = os.path.abspath(os.path.dirname(__file__) + '/')
sys.path.append(base_dir)

app = Flask(__name__)

if __name__ == '__main__':
    FLASK_DEBUG = os.getenv('FLASK_DEBUG', True)
    app.run(host='0.0.0.0', debug=FLASK_DEBUG, port=8081)

    dir_path = '/home/webmaster/Web_API/API/Paraphrase_Generator'
    args = [
        '{}/moses'.format(dir_path), '-f',
        '{}/Working/mert-work/moses.ini'.format(dir_path),
        '-n-best-list',
        'output.txt',
        2,
    ]

    with Popen(args, stdin=PIPE, stdout=PIPE) as proc:
        proc.stdin.write('what is your name ?')
        proc.stdin.flush()

        out, err = proc.communicate()
        print('out :', out)

        @app.route('/paraphrase', methods=['POST'])
        def annotate():
            data = request.get_json()
            sentence = data['sentence']

            return json.dumps({
                'result': '',
            })
