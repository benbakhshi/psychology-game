from questions import list_of_qa
import jinja2
import os
import webapp2
import random

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates")
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(TEMPLATE_PATH))

QUESTION = list_of_qa("qanda.txt")


class HomeHandler(webapp2.RequestHandler):
    def get(self):
        
        template_values = { }
        template = jinja_environment.get_template('index.html')
        self.response.write(template.render(template_values))


class QuestionHandler(webapp2.RequestHandler):
    def get(self):
        qn = random.randrange(0,len(QUESTION))
        q = QUESTION[qn]
        text = '<div class="question" data-q="%d">%s</div><ul class="options">' % (qn, q.question)
        for n in range(len(q.option)):
            text += '<li><button class="opt" data-opt="%d">%s</button></li>' % (n + 1,q.option[n])
        text += '</ul>'
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(text)


class AnswerHandler(webapp2.RequestHandler):
    def get(self):
        if "q" not in self.request.GET or "a" not in self.request.GET or int(self.request.GET['q']) >= len(QUESTION):
            self.redirect('./')
            return
        q = int(self.request.GET['q'])
        a = int(self.request.GET['a'])
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(QUESTION[q].answer == a)