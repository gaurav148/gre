from flask import Flask
from flask import render_template, request
import random, copy

app = Flask(__name__)
#For beginner level quiz
original_questions = {
 #Format is 'question':[options]
 'If the roots of the equation x2−16x−612=0 are a and b, what is the value of a+b?':['16','-16','0','-612'],
 'If x and y are non-negative integers such that 2x+3y=8 and z=x2+y2, what is the maximum value of z?':['16','0','5','20'],
 'If |x|=|y|, which of the following must be true?':['x4=y4','x>y','x<y','x3=y3'],
 'If −1<h<0, which of the following has the greatest value?':['1-1/h','1+1/h','1-h','1+h'],
 'If the average (arithmetic mean) of five distinct positive integers is 10, what is the difference between the largest possible value of the greatest integer and the least possible value of the greatest of the five integers?':['28','0','5','40'],
 'If a/b>c/d, and none of a, b, c, and d is equal to 0, which of the following must be true?':['(−a/b)<(−c/d)','−a/b<c/d','|a/b|>|c/d|','(b/a)<(d/c)'],
 'What could be the value of integer from 180 to 300, inclusive, that leave the remainder 2 when divided by 15 and by 9?':['182','191','197','242'],
 'A computer companys featured laptop cost $800 last year. This year, the laptop sold for 15 percent less than it did last year. Next year, after updates are made to the model, there will be a 25% price increase over this years price. What will be the price next year?':['$850','$810','$840','$845'],
 'Pipe A can fill a tank in 3 hours. If pipe B can fill the same tank in 2 hours, how many minutes will it take both pipes to fill 2/3 of a tank?':['54','30','48','60'],
 'How many milliliters of acid are ther in 350 mililiters of 4 percent acid?':['87.5','10','14','35']
}
#For advanced level quiz
original_question = {
 #Format is 'question':[options]
 'Astrid wrote down all the different three-digit numbers that can be written using each of the numeral 1, 2 and 3 exactly once. What is the median of the numbers Astrid wrote down?':['231','213','222','233'],
 'If a bookstore owner buys 15 books less for $900 when the price of each book goes up by $3, then find the original price of book.':['$12','$15','$18','$20'],
 'If m and n are the roots of the equation a2 - 6a + 8 = 0, then find the value of (m+n)(m-n)':['12','8','16','4'],
 'A train takes 10 seconds to cross a pole and 20 seconds to cross a platform of length 200 m. What is the length of train?':['200m','400m','600m','800m'],
 'The price of a pair of sneakers was $80 for the last six months of last year. On January first, the price increased 20%. After the price increase, an employee bought these sneakers with a 10 percent employee discount. What price did the employee pay?':['$86.40','$83.33','$82.00','$88.00'],
 'If 6k^2 + k = 2 and k > 0, then k must equal which of the following?':['1/2','1','3/2','2'],
 'In how many different ways can 3 identical green shirts and 3 identical red shirts be distributed among 6 children such that each child receives a shirt?':['20','40','216','720'],
 'If x > 0 which of the following expressions are equal to 3.6 percent of (5x)/12?':['x percent of 3/2','3 percent of 20x','3x percent of 0.2','0.05 percent of 3x'],
 'A popular website requires users to create a password consisting of digits only. If no digit may be repeated and each password must be at least 9 digits long, how many passwords are possible?':['2 × 10!','9! + 10!','9! × 10!','19!'],
 'In a certain shop, notebooks that normally sell for 59 cents each are on sale at 2 for 99 cents. How much can be saved by purchasing 10 of these notebooks at the sale price? ':['$0.95','$0.85','$1.00','$1.05']
}

practice_questions={
 'If 6k^2 + k = 2 and k > 0, then k must equal which of the following?':['1/2','1','3/2','2'],
 'A tower casts a shadow of 6 meters at a certain time of the day. If at exactly the same time, a man stands at the top of the tower, the length of the shadow increases by 2 meters. What is the height of the man if the tower is 5 meters high?':['1.66','1.5','1','2'],
 'If x2 + 6x = –9, how many values of x are possible?':['one','none','two','infinite'],
 'In a certain parallelogram, the size of one interior angle exceeds that of another interior angle by D degrees. Which of the following expressions represents the degree measure of the smaller angle?':['90-D/2','90-D','180-D','120-D'],
 'The lengths of two sides of a triangle are 5 and 7. Which of the following could be the perimeter of the triangle?':['22','14','24','27'],
 'If a/b>c/d, and none of a, b, c, and d is equal to 0, which of the following must be true?':['(−a/b)<(−c/d)','−a/b<c/d','|a/b|>|c/d|','(b/a)<(d/c)'],
 'What could be the value of integer from 180 to 300, inclusive, that leave the remainder 2 when divided by 15 and by 9?':['182','191','197','242'],
 'A computer companys featured laptop cost $800 last year. This year, the laptop sold for 15 percent less than it did last year. Next year, after updates are made to the model, there will be a 25% price increase over this years price. What will be the price next year?':['$850','$810','$840','$845'],
 'Pipe A can fill a tank in 3 hours. If pipe B can fill the same tank in 2 hours, how many minutes will it take both pipes to fill 2/3 of a tank?':['54','30','48','60'],
 'How many milliliters of acid are ther in 350 mililiters of 4 percent acid?':['87.5','10','14','35']
}



questions = copy.deepcopy(original_questions)

question = copy.deepcopy(original_question)

practice = copy.deepcopy(practice_questions)


def shuffle(q):
 
 selected_keys = []
 i = 0
 while i < len(q):
  current_selection = random.choice(list(q.keys()))
  if current_selection not in selected_keys:
   selected_keys.append(current_selection)
   i = i+1
 return selected_keys

def shuffles(q):
 
 selected_key = []
 i = 0
 while i < len(q):
  current_selection = random.choice(list(q.keys()))
  if current_selection not in selected_key:
   selected_key.append(current_selection)
   i = i+1
 return selected_key

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/quant')
def quant():
    return render_template('quant.html')



@app.route('/quant/quant_quiz_home')
def quant_quiz():
    return render_template('quant_quiz_home.html')
    

@app.route('/quant/quant_quiz_home/quant_quiz1')
def quant_quiz1():
    questions_shuffled = shuffle(questions)
    for i in questions.keys():
        random.shuffle(questions[i])
    return render_template('quant_quiz1.html', q = questions_shuffled, o = questions)

@app.route('/quant/quant_quiz_home/quant_quiz1/score', methods=['POST'])
def quiz1_answers():
 correct = 0
 for i in questions.keys():
  answered = request.form[i]
  if original_questions[i][0] == answered:
   correct = correct+1
 return render_template('score.html',s=correct)
#'<h1>Correct Answers: <u>'+str(correct)+'</u></h1>'

@app.route('/quant/quant_quiz_home/quant_quiz2')
def quant_quiz2():
    question_shuffled = shuffles(question)
    for i in question.keys():
        random.shuffle(question[i])
    return render_template('quant_quiz2.html', q = question_shuffled, o = question)

@app.route('/quant/quant_quiz_home/quant_quiz2/score', methods=['POST'])
def quiz2_answers():
 correct = 0
 for i in question.keys():
  answered = request.form[i]
  if original_question[i][0] == answered:
   correct = correct+1
 return render_template('score.html',s=correct)


@app.route('/quant/quant_prac')
def quant_prac():
  practice_shuffled = shuffle(practice)
  for i in practice.keys():
    random.shuffle(practice[i])
  return render_template('quant_prac.html', q = practice_shuffled, o = practice)


@app.route('/quant/quant_prac/score', methods=['POST'])
def prac_answers():
 correct = 0
 for i in practice.keys():
  answered = request.form[i]
  if original_question[i][0] == answered:
   correct = correct+1
 return render_template('score.html',s=correct)