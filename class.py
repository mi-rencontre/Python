#__metaclass__ = type
#
#class Person:
#    def setName(self, name):
#        self.name = name
#
#    def getName(self):
#        return self.name
#
#    def greet(self):
#        print "Hello, world! I'm %s." %self.name
        
class Filter:
    def init(self):
        self.blocked = []

    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter):
    def init(self):
        self.blocked = ['SPAM']
