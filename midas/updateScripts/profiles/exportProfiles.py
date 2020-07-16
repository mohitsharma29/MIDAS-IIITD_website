from getProfileResponses import load_profile_sheet
import os

responses = load_profile_sheet().fillna('')

print(responses)

def getImageLink(value, path='/assets/images/team/'):
    finalStr = ''
    temp = value.split(' ')
    temp1 = temp[0].split('/')
    temp2 = temp[1].split(':')
    for i in temp1:
        finalStr = finalStr + i
    for i in temp2:
        finalStr = finalStr + i
    finalStr = finalStr + '.jpg'
    return path+finalStr

def getOutputString(data, index):
    string = ''
    string += '---\n'
    string += 'layout: member\n'
    string += 'title: \"' + data['Name'][index].strip().rstrip() + '\"\n'
    string += 'position: ' + data['Your position in lab'][index].strip().rstrip() + '\n'
    string += 'type: ' + data['Type'][index].strip().rstrip() + '\n'
    string += 'nickname: ' + data['nickname'][index].strip().rstrip() + '\n'
    string += 'organization: ' + data['Organization'][index].strip().rstrip() + '\n'
    string += 'handle: ' + data['handle'][index].strip().rstrip() + '\n'
    string += 'email: ' + data['email'][index].strip().rstrip() + '\n'
    string += 'profile_link: ' + data['profile_link'][index].strip().rstrip() + '\n'
    string += 'twitter: ' +  data['twitter'][index].strip().rstrip().replace('@','') + '\n'
    string += 'image: ' + getImageLink(data['Timestamp'][index].strip().rstrip()) + '\n'
    string += 'cv: ' + data['CV URL'][index].strip().rstrip() + '\n'
    string += 'github: ' + data['github'][index].strip().rstrip() + '\n'
    string += 'scholar: ' + data['Google scholar'][index].strip().rstrip() + '\n'
    string += 'alum: ' + data['Alumna?'][index].strip().rstrip().lower() + '\n'
    string += '---\n\n'
    #string += '# Abstract\n\n'
    string += data['Description'][index].strip().rstrip()

    return string

for i in responses.index:
    string = getOutputString(responses, i)
    temp = responses['Timestamp'][i].strip().rstrip().split(' ')[0].split('/')
    fileName = temp[2] + '-' + temp[0] + '-' + temp[1] + '-' + responses['Name'][i].strip().rstrip().replace(' ', '-') + '.md'
    firstName = responses['Name'][i].strip().rstrip().split(' ')[0]
    curPath = os.getcwd()
    with open(curPath + '/../../team/_posts/' + fileName, 'w') as f:
        f.write(string)
