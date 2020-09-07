from flask import Flask, render_template,request
from decimal import Decimal


app = Flask(__name__)


@app.route('/')
def hello_world() :
    return render_template('index.html')

@app.route('/rsa', methods=['GET', 'POST'])
def rsa():
    if (request.method == 'POST') :
        p=int(request.form.get('p'))
        q=int(request.form.get('q'))
        no=int(request.form.get('r'))
        print(p,q,no)

        def gcd(a, b) :
            if b == 0 :
                return a
            else :
                return gcd(b, a % b)

        n = p * q
        t = (p - 1) * (q - 1)

        for e in range(2, t) :
            if gcd(e, t) == 1 :
                break

        for i in range(1, 10) :
            x = 1 + i * t
            if x % e == 0 :
                d = int(x / e)
                break
        ctt = Decimal(0)
        ctt = pow(no, e)
        ct = ctt % n

        dtt = Decimal(0)
        dtt = pow(ct, d)
        dt = dtt % n

        print('n = ' + str(n) + ' e = ' + str(e) + ' t = ' + str(t) + ' d = ' + str(d) + ' cipher text = ' + str(
            ct) + ' decrypted text = ' + str(dt))
        # a={
        #     'nn':n,
        #     'ee':e,
        #     'cy':ct
        # }
        cypher=[n,e,no,ct]

    return render_template("op.html",data=cypher)

if __name__ == '__main__' :
    app.run()
