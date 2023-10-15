# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 12:36:29 2023

@author: Guilherme
"""

from flask import Flask, render_template, request, redirect, url_for  
import random
from all_questions import all_questions

app = Flask(__name__)

cur_quest_idx = 0
correct = 0
question_number = 1
questions = all_questions.copy()
total_questions = len(questions)

@app.route('/')  
def index():  
   
   global cur_quest_idx, question_number, total_questions, questions
   if len(questions) > 0:
       chosen_question_index = random.randint(0, len(questions)-1)
       cur_quest_idx = chosen_question_index
       chosen_question = questions[chosen_question_index]
    
       return render_template("index.html", questions=[chosen_question], 
                          question_number = question_number, total_q = total_questions)
   else:
       acc = 100 * correct/total_questions
       corr = correct
       restart()
       return render_template("final.html", correct = corr, total_q = total_questions, acc = acc)

@app.route('/restart', methods = ["POST"])
def restart():
    global question_number, total_questions, questions, correct
    corr = correct
    total_q = total_questions
    acc = 100 * correct/total_questions
    questions = all_questions.copy()
    total_questions = len(questions)
    question_number = 1
    correct = 0
 
    return render_template("final.html", correct = corr, total_q = total_q, acc = acc)

@app.route('/submit', methods=["POST"])  
def submit():  
   user_answer = request.form.get("answer")  
   global cur_quest_idx, question_number, correct
   question = questions[cur_quest_idx]
         
   correct_answer = question["answer"]  
   questions.pop(cur_quest_idx)
   question_number += 1
   if user_answer.lower() == correct_answer.lower():  
       # return "Correct!", 200  
       correct += 1
       return render_template("results.html", answer="Correct")
   else:  
       return render_template("results.html", answer = f"Wrong! The correct answer is: {correct_answer}")
   

if __name__ == '__main__':  
   app.run()  