from app import app

counter = 0

@app.route('/')
@app.route('/index')
def index():
    return 'Hello, world'

@app.route('/info')
def info():
    global counter
    counter += 1
    return 'Hello, times: {}'.format(counter)


