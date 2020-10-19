from flask import send_from_directory, render_template
import markdown.extensions.fenced_code
from app import app

# Serve Svelte apps
@app.route("/<path:path>")
def svelte_client(path):
    return send_from_directory('../svelte/public/', path)


@app.route('/<int:slide>')
def show_slide(slide):
    test_tree = list([
        {
            'type': 'folder',
            'name': 'app',
            'files': [
                {
                    'type': 'folder',
                    'name': 'templates',
                    'files': [
                        { 'type': 'file', 'name': 'base.html' },
                        { 'type': 'file', 'name': 'hello.html' }
                    ]
                },
                { 'type': 'file', 'name': '__init__.py' },
                { 'type': 'file', 'name': 'routes.py' }
            ]
        },
        {
            'type': 'folder',
            'name': 'svelte',
            'files': [
                {
                    'type': 'folder',
                    'name': 'src',
                    'files': [
                        { 'type': 'file', 'name': 'App.svelte' },
                        { 'type': 'file', 'name': 'File.svelte' },
                        { 'type': 'file', 'name': 'Folder.svelte' }
                    ]
                },
                {
                    'type': 'folder',
                    'name': 'public',
                    'files': [
                        { 'type': 'file', 'name': 'COMPILED_SVELTE_FILES' },
                    ]
                },
                { 'type': 'file', 'name': 'package.json' },
                { 'type': 'file', 'name': 'rollup.config.js' }
            ]
        },
        { 'type': 'file', 'name': 'config.py' },
        { 'type': 'file', 'name': 'flask-svelte.py' }
    ])

    md_file = open("slides/" + str(slide) + ".md",'r')
    md_text = md_file.read()

    return render_template('slide.html', data=test_tree, slide=md_text)
