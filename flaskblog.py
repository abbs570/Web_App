from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
{
    'author': 'Abbey Noyes',
    'title' : 'Blog Post 1',
    'content' : 'First post content',
    'date_posted' : 'June 1, 2023'
},
{
    'author': 'Allie Noyes',
    'title' : 'Blog Post 1',
    'content' : 'First post content',
    'date_posted' : 'June 1, 2023'
}
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)


@app.route("/about")
def about():
    return render_template('about.html')



if __name__ == '__main__':
    app.run(debug=True)