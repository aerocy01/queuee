from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

queue = Queue()
deque = Deque()

@app.route('/')
def index():
    return render_template('index.html', queue=queue.display(), deque=deque.display())

@app.route('/enqueue', methods=['POST'])
def enqueue():
    try:
        item = request.form['item']
        queue.enqueue(item)
    except Exception as e:
        return str(e)
    return redirect(url_for('index'))

@app.route('/dequeue', methods=['POST'])
def dequeue():
    try:
        queue.dequeue()
    except Exception as e:
        return str(e)
    return redirect(url_for('index'))

@app.route('/add_front', methods=['POST'])
def add_front():
    try:
        item = request.form['item']
        deque.add_front(item)
    except Exception as e:
        return str(e)
    return redirect(url_for('index'))

@app.route('/add_rear', methods=['POST'])
def add_rear():
    try:
        item = request.form['item']
        deque.add_rear(item)
    except Exception as e:
        return str(e)
    return redirect(url_for('index'))

@app.route('/remove_front', methods=['POST'])
def remove_front():
    try:
        deque.remove_front()
    except Exception as e:
        return str(e)
    return redirect(url_for('index'))

@app.route('/remove_rear', methods=['POST'])
def remove_rear():
    try:
        deque.remove_rear()
    except Exception as e:
        return str(e)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
