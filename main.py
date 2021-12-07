from flask import Flask, redirect, render_template
import os
from forms.solver import SolverForm
from numpy import roots, isreal

app = Flask(__name__)
app.config['SECRET_KEY'] = 'flask_secret_key'


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SolverForm()
    if form.validate_on_submit():
        answ = []
        coeff = [int(form.a.data), int(form.b.data), int(form.c.data), int(form.d.data), int(form.e.data)]
        answ = roots(coeff)
        answ = answ.real[abs(answ.imag) < 1e-5]
        return render_template('index.html', check=True, form=form, answer=answ)
    print(form.errors)
    print('tuta')
    return render_template('index.html', form=form, check=False)


def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()
