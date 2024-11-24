from flask import Flask, render_template, request

app = Flask(__name__)

options = [
    'Option 1',
    'Option 2',
    'Option 3',
]

data = [
    { "name": "Alex", "age":30 }, 
    { "name": "Max", "age":30 },
    { "name": "George", "age":30 }
]

@app.route('/', methods=['GET', 'POST'])
def index():
    selected_option = request.form.get('options')
    # table_data = data.get(selected_option, []) if selected_option else []
    return render_template('index.html', options=options, table_data=data)

if __name__ == "__main__":
    app.run(debug=True)
