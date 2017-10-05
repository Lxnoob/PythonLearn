# -*- coding: utf-8 -*-

def print_scores(**kw):
    print('      Name  Score')
    print('------------------')
    for name, score in kw.items():
        print('%10s  %d' % (name, score))
    print()

print_scores(Adam=99, Lisa=88, Bart=77)

data = {
    'Adam Lee': 99,
    'Lisa S': 88,
    'F.Bart': 77
}

print_scores(**data)

def print_info(name,city='Beijing',**kw):
        print('Personal Info')
        print('---------------')
        print('   City: %s' % city)
        if 'gender' in kw:
            print(' Gender: %s' % kw['gender'])
        print('   Name: %s' % name)    
        if 'age' in kw:
            print('    Age: %s' % kw['age'])
        print()

print_info('Bob', gender='male', age=20)
print_info('Lisa', 'Shanghai',gender='female',  age=18)
