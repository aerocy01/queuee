from flask import Flask, render_template, request, redirect, url_for
from queue import Queue 

app = Flask(__name__)

queue = Queue()

@app.route('/')
def index():
    return render_template('queue.html', queue=queue.print_queue())

@app.route('/update', methods=['POST'])
def update():
    operation = request.form['operation']
    data = request.form.get('data', None)

    if operation == "enqueue" and data:
        queue.enqueue(data)
    elif operation == "dequeue":
        queue.dequeue()

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)