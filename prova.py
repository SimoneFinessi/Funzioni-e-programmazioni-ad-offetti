from flask import Flask
app = Flask(__name__)
def addizione(a,b):#PARAMETRO modo che l'utente a per passare valori tra le funzioni
    risultato=a+b
    return risultato
@app.route('/', methods=['GET'])
def ciao():
    risultato=addizione(15,5)
    return(str(risultato))
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)