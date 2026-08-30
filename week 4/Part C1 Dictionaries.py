#dictionaries_1
students={1:'Akhila',
              2:'Darani',
              3:'Ishwarya',
              4:'Sanvi',
              5:'Sai',
              }
print('students:',students)

'''sample output:
students: {1:'Akhila',2:'Darani',3:'Ishwarya',4:'Sanvi',5:'Sai'}
  '''
#dictionaries_2
students={1:'Akhila',2:'Darani',3:'Ishwarya'}
students[4]='Sanvi'
students[5]='Sai'
students[6]='Roshini'
print('final dict:',students)

'''sample output:
final dict: {1:'Akhila',2:'Darani',3:'Ishwarya',4:'Sanvi',5:'Sai',6:'Roshini'}  '''

#dictionaries_3
dict={1:'key', 2:'lock', 3:'solution'}
print('before update:',dict)
dict[2]='problem'
print('after update:',dict)

'''sample output:
before update: {1: 'key', 2: 'lock', 3: 'solution'}
after update: {1: 'key', 2: 'problem', 3: 'solution'}  '''

#dictionaries_4
keys=['name','place','color']
values=['mirchi','guntur','red']
zip()
data=dict(zip(keys,values))
print('dictionary:',data)

'''sample output:
dictionary: {'name': 'mirchi', 'place': 'guntur', 'color': 'red'} '''

#dictionaries_5
employees={
    1:{'name':'priya','department':'CSE','salary':100000},
    2:{'name':'shankar','departmrnt':'mechanical','salary':100000},
    3:{'name':'maheswar','department':'EEE','salary':100000}
    }
print('employees:',employees)

'''sample output:
employees: {1: {'name': 'priya', 'department': 'CSE', 'salary': 100000}, 2: {'name': 'shankar', 'departmrnt': 'mechanical', 'salary': 100000}, 3: {'name': 'maheswar', 'department': 'EEE', 'salary': 100000}} '''
    
#dictionaries_6

