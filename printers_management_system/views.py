from flask import render_template

from printers_management_system import app


@app.route('/')
def index():
    app.logger.warning('sample message')
    return render_template('index.html')
