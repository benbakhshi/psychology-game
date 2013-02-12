import codecs

class Question(object):
    """ represents a question """

    def __repr__(self):
        return "<Question: %s>" % self.question


def parts(l):
    q = Question()
    q.question = l[0]
    q.option = l[1:5]
    q.answer = int(l[5])
    return q

def list_of_qa(filename):
    temp = []
    result = []
    lines = 0

    with codecs.open(filename, 'r', 'utf-8-sig') as f:
        for line in f:
            lines += 1
            temp.append(line.strip())
            if lines == 6:
                lines = 0
                result.append(parts(temp))
                temp = []
    return result

