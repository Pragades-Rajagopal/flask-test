from flask import Flask, render_template, request

app = Flask(__name__)

options = [
    'Option 1',
    'Option 2',
    'Option 3',
]

data = {
    'Option 1': [['Row 1', 'Data 1A', 'Data 1B'], ['Row 2', 'Data 1C', 'Data 1D']],
    'Option 2': [['Row 1', 'Data 2A', 'Data 2B'], ['Row 2', 'Data 2C', 'Data 2D']],
    'Option 3': [['Row 1', 'Data 3A', 'Data 3B'], ['Row 2', 'Data 3C', 'Data 3D']]
}

@app.route('/', methods=['GET', 'POST'])
def index():
    selected_option = request.form.get('options')
    table_data = data.get(selected_option, []) if selected_option else []
    return render_template('index.html', options=options, table_data=table_data)

if __name__ == "__main__":
    app.run(debug=True)
