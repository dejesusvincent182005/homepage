from flask import Flask, render_template, request, redirect, url_for

   app = Flask(_name_)

   # In-memory list to store tasks (each task is a dict with 'id', 'text', and 'completed')
   tasks = []
   task_id_counter = 1

   @app.route('/')
   def index():
       return render_template('index.html', tasks=tasks)

   @app.route('/add', methods=['POST'])
   def add_task():
       global task_id_counter
       task_text = request.form.get('task')
       if task_text:
           tasks.append({'id': task_id_counter, 'text': task_text, 'completed': False})
           task_id_counter += 1
       return redirect(url_for('index'))

   @app.route('/complete/<int:task_id>')
   def complete_task(task_id):
       for task in tasks:
           if task['id'] == task_id:
               task['completed'] = not task['completed']  # Toggle completion
               break
       return redirect(url_for('index'))

   @app.route('/delete/<int:task_id>')
   def delete_task(task_id):
       global tasks
       tasks = [task for task in tasks if task['id'] != task_id]
       return redirect(url_for('index'))

   if _name_ == '_main_':
       app.run(debug=True)