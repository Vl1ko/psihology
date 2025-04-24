from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
from wtforms.validators import DataRequired

class StressTestForm(FlaskForm):
    choices = [
        ('0', 'Никогда'),
        ('1', 'Редко'),
        ('2', 'Иногда'),
        ('3', 'Часто'),
        ('4', 'Постоянно')
    ]
    
    question_1 = RadioField(
        'Как часто вы чувствуете беспокойство или нервозность без явной причины?', 
        choices=choices,
        validators=[DataRequired()]
    )
    
    question_2 = RadioField(
        'Как часто у вас возникают проблемы со сном (засыпанием, ранним пробуждением)?', 
        choices=choices,
        validators=[DataRequired()]
    )
    
    question_3 = RadioField(
        'Как часто вы испытываете физическое напряжение (скованность мышц, головные боли)?', 
        choices=choices,
        validators=[DataRequired()]
    )
    
    question_4 = RadioField(
        'Как часто вы чувствуете раздражительность или вспыльчивость?', 
        choices=choices,
        validators=[DataRequired()]
    )
    
    question_5 = RadioField(
        'Как часто вам трудно сконцентрироваться на задаче?', 
        choices=choices,
        validators=[DataRequired()]
    )
    
    question_6 = RadioField(
        'Как часто вы чувствуете усталость даже после полноценного отдыха?', 
        choices=choices,
        validators=[DataRequired()]
    )
    
    question_7 = RadioField(
        'Как часто вы чувствуете, что не справляетесь с повседневными задачами?', 
        choices=choices,
        validators=[DataRequired()]
    )
    
    question_8 = RadioField(
        'Как часто вы избегаете общения с близкими или коллегами?', 
        choices=choices,
        validators=[DataRequired()]
    )
    
    question_9 = RadioField(
        'Как часто у вас возникают проблемы с аппетитом (переедание или потеря аппетита)?', 
        choices=choices,
        validators=[DataRequired()]
    )
    
    question_10 = RadioField(
        'Как часто вы испытываете чувство подавленности или безнадежности?', 
        choices=choices,
        validators=[DataRequired()]
    )
    
    submit = SubmitField('Получить результаты') 