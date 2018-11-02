import requests


def paraphrase(sentence):
    url = 'http://credon.kaist.ac.kr:8082/paraphrase'
    data = {'sentence': sentence}
    res = requests.post(url, json=data)
    return res.text


if __name__ == '__main__':
    print(paraphrase('apple trees are beginning to blossom .'))
    # {"result": "apple tree are starting to blossom . "}
