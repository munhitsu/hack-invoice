from flask import Flask, render_template
from flask_flatpages import FlatPages

app = Flask(__name__)
app.config.from_pyfile('settings.cfg')
pages = FlatPages(app)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    total = {
        'total_net': 0,
        'vat_amount': 0,
        'total_gross': 0,
    }
    for item in page.meta['items']:
        total['total_net'] += item['total_net']
        total['vat_amount'] += item['vat_amount']
        total['total_gross'] += item['total_gross']
    total['total_gross_words'] = "One thousand PLN 0/100" #TODO: update next time

    return render_template('invoice.html', page=page, total=total)

if __name__ == '__main__':
    app.run()
