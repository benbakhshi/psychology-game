from handlers import HomeHandler,QuestionHandler,AnswerHandler
import webapp2

app = webapp2.WSGIApplication([(r'/', HomeHandler),
                                (r'/question', QuestionHandler),
                                (r'/answer', AnswerHandler),
                                ],
                              debug=True)
