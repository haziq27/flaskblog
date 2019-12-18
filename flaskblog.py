from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Haziq',
        'title': 'First Title',
        'content': 'First content',
        'date_posted': '1st January 2019'
    },
    {
        'author': 'Afiq',
        'title': 'Second Title',
        'content': 'Second content',
        'date_posted': '1st February 2019'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


# can run like a normal python file
if __name__ == '__main__':
    app.run(debug=True)
