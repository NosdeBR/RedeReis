from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Renderiza o arquivo templates/index.html
    return render_template('index.html')

print("vasco maior do rj")

if __name__ == '__main__':
    app.run(debug=True)