#dictionary {}
#dictionary_semicolon {};
#tuple ()
#tuple_semicolon ();
#simple_line 


class Data:
    
    def __init__(self, t='line', n='', d=''):
        self.type = t
        self.name = n
        self.data = d

    def show(self, stream, indent=0):
        if self.type == 'dictionary':
            stream.write('{}{} \n'.format(' '*indent, self.name))
            stream.write('{} {{ \n'.format(' '*indent))
            for tmp in self.data:
                tmp.show(stream, indent + 4)
            stream.write('{} }} \n'.format(' '*indent))
        elif self.type == 'dictionary_semicolon':
            stream.write('{}{} \n'.format(' '*indent, self.name))
            stream.write('{} {{ \n'.format(' '*indent))
            for tmp in self.data:
                tmp.show(stream, indent + 4)
            stream.write('{} }}; \n'.format(' '*indent))
        elif self.type == 'tuple':
            stream.write('{}{} \n'.format(' '*indent, self.name))
            stream.write('{}( \n'.format(' '*indent))
            for tmp in self.data:
                tmp.show(stream, indent + 4)
            stream.write('{}) \n'.format(' '*indent))
        elif self.type == 'tuple_semicolon':
            stream.write('{}{} \n'.format(' '*indent, self.name))
            stream.write('{}( \n'.format(' '*indent))
            for tmp in self.data:
                tmp.show(stream, indent + 4)
            stream.write('{}); \n'.format(' '*indent))
        elif self.type == 'simple_line':
            stream.write('{}{} {}; \n'.format(' '*indent, self.name, self.data))
        elif self.type == 'line':
            stream.write('{} {} \n'.format(' '*indent, self.data))

file_ = open('test.txt', 'w')
Data(t='dictionary', n='bar', 
        d=(Data(t='simple_line', n='bar1', d=1), 
            Data(t='tuple_semicolon', n='bar2',
                d=(Data(d=('(1 2 3)')),)
                ))).show(file_, 0)
file_.close()
