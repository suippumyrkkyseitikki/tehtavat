from flask import Flask

app = Flask(__name__)
@app.route('/alkuluku/<number>')

def alkuluku(number):

    number= int(number)

    alkuluku = True

    if number < 2:
        alkuluku = False
    else :
        for i in range(2, number):
            if number % i == 0:
                alkuluku = False
                break

    vastaus = {
        "Number" : number,
        "isPrime": alkuluku
    }

    return vastaus


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)