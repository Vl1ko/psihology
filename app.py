from flask import Flask, render_template, request, redirect, url_for, flash
from forms import StressTestForm
from stress_calculator import calculate_stress_level

app = Flask(__name__)
app.config['SECRET_KEY'] = 'stress-assessment-app-key'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = StressTestForm()
    result = None
    
    if form.validate_on_submit():
        answers = {
            'question_1': form.question_1.data,
            'question_2': form.question_2.data,
            'question_3': form.question_3.data,
            'question_4': form.question_4.data,
            'question_5': form.question_5.data,
            'question_6': form.question_6.data,
            'question_7': form.question_7.data,
            'question_8': form.question_8.data,
            'question_9': form.question_9.data,
            'question_10': form.question_10.data,
        }
        stress_level, recommendation = calculate_stress_level(answers)
        result = {
            'level': stress_level,
            'recommendation': recommendation
        }
    
    return render_template('index.html', form=form, result=result)

if __name__ == '__main__':
    app.run(debug=True, port=5001) 