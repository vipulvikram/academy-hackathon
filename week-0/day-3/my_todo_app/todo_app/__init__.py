import os

from flask import Flask, render_template, request


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    def todo_view(todo):
        the_view = 'List of my todos:' + '<br/>'
        for to in todo:
            the_view += to +'<br/>'
        the_view += '__LIST ENDS__'
        return the_view;

    def functio(name):
        if name == 'depo':
            return ['Go for run', 'ohyes']
        else:
            return ['vipul', 'vikram']


    @app.route('/vip')
    def vip():
        name = request.args.get('name')
        print(name)
        my_todos = functio(name)
        
        return todo_view(my_todos)


    @app.route('/raj')
    def raj():
        return render_template('index.html')

    @app.route('/depo')
    def depo():
        todo = ['Go for run', 'ohyes']
        return todo_view(todo)

    # a simple page that list my todos
    @app.route('/shivang')
    def shivang():
        return ('Wake Up' + '<br/>' +
            'Drink Coffee' + '<br/>' +
            'Read Non-fiction Novel' + '<br/>'
        )

    return app

