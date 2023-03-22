RESPONSES_KEY = "responses"
RESPONSES_LENGTH = "responseslength"
SURVEY_LENGTH = "surveylength"
QUESTION = ""
CHOICES = ""
from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)



@app.route('/')
def index():
    """Return homepage."""

    return redirect('/home')

@app.route('/home', methods=["POST", "GET"])
def index1():
    """Return homepage."""
    if request.method == 'POST':
        session[RESPONSES_KEY] = []
        session[QUESTION] = survey.questions[0].question
        session[CHOICES] = survey.questions[0].choices
        RESPONSES_LENGTH = 0
        SURVEY_LENGTH = 0
        
        return redirect('/smile')
    return render_template("home.html", survey=survey)





@app.route('/smile', methods=["POST", "GET"])
def smile():
    """Return homepage."""
    
    if session[RESPONSES_LENGTH] < 1:
            session[QUESTION] = survey.questions[0].question
           
    
    
    
    if request.method == 'POST':
        our_request = request.form['radio']
        responses = session[RESPONSES_KEY]
        responses.append(our_request)
        session[RESPONSES_KEY] = responses
        #import pdb
        #pdb.set_trace()
        session[RESPONSES_LENGTH] = len(responses)
        session[SURVEY_LENGTH] = len(survey.questions)
        
        
        
        

        
        if session[RESPONSES_LENGTH] >= session[SURVEY_LENGTH]:
            session[RESPONSES_LENGTH] = 0
            return redirect('/thankyou')
        #our_response = request.form.get('radio', 'affirmative')
        #negative = request.form.get('radio')
        
        #return redirect("/ans", request=our_request)
        session[QUESTION] = survey.questions[session[RESPONSES_LENGTH]].question
        flash(f"You answered {our_request}!")
        return redirect('/ans')
    
    return render_template("test.html", survey=survey, responses=session[RESPONSES_KEY], responseslength=session[RESPONSES_LENGTH], surveylength=session[SURVEY_LENGTH], question=session[QUESTION])


@app.route('/ans', methods=["POST", "GET"])
def ans():
    """Return homepage."""
    question = survey.questions[0]
    #import pdb
    #pdb.set_trace()
    if request.method == 'POST':
       
        return redirect('/smile')

    return render_template("question.html", survey=survey, question=question)


@app.route('/thankyou', methods=["POST", "GET"])
def ans10():
    """Return homepage."""
    question = survey.questions[0]
    #import pdb
    #pdb.set_trace()
    if request.method == 'POST':
        session[RESPONSES_LENGTH] = 0
        return redirect('/home')
    return render_template("thankyou.html", survey=survey, question=question)



@app.route('/showinfo')
def ans1():
    """Return homepage."""
    question = survey.questions[0]
    #import pdb
    #pdb.set_trace()
    return render_template("answer.html", survey=survey, question=question)