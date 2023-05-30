from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_sgpa', methods=['POST'])
def calculate_sgpa():
    
    physics_marks = int(request.form['physicsfill'])
    maths_marks = int(request.form['mathfill'])
    elea_marks = int(request.form['eleafill'])
    eleb_marks = int(request.form['elebfill'])
    pop_marks = int(request.form['popfill'])

   
    physics_credit = 4
    maths_credit = 3
    elea_credit = 3
    eleb_credit = 3
    pop_credit = 4

    
    total_marks = (physics_marks * physics_credit) + (maths_marks * maths_credit) + \
                  (elea_marks * elea_credit) + (eleb_marks * eleb_credit) + \
                  (pop_marks * pop_credit)
    
    total_credits = physics_credit + maths_credit + elea_credit + eleb_credit + pop_credit

    
    sgpa = total_marks / total_credits

    return render_template('index.html', sgpa=sgpa, total=total_marks)

if __name__ == '__main__':
    app.run()
