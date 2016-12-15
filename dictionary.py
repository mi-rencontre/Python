people = {

    'Alice': {
        'phone':'123456',
        'addr':'beijing'
        },

    'Beth':{
        'phone':'455768',
        'addr':'America'
        },

    'Cecil':{
        'phone':'126898',
        'addr':'shannxi'
        }
    }

labels = {
    'phone':'phone number',
    'addr':'address'
    }
name = raw_input('Name:')

request = raw_input('Phone number (p) or address (a)?')

key = request

if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

#if name in people: print "%s's %s is %s." % \
#   (name, labels[key], people[name][key])

person = people.get(name,{})
label = labels.get(key, key)
result = person.get(key, 'not avaliable')
print "%s's %s is %s." %(name, label, result)
