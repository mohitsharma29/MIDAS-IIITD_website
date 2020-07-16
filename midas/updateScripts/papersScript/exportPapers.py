from getPaperResponses import load_sheet

responses = load_sheet().fillna('')

def getOutputString(data, index):
    string = ''
    string += '---\n'
    string += 'layout: paper\n'
    string += 'title: \"' + data['Paper Title'][index].strip().rstrip() + '\"\n'
    string += 'year: \"' + data['Acceptance Date/Year'][index].strip().rstrip().split('/')[-1] + '\"\n'
    string += 'shortref: \n'
    string += 'nickname: \n'
    string += 'journal: ' + data['Journal/Conference'][index].strip().rstrip() + '\n'
    string += 'volume: ' + data['Volume'][index].strip().rstrip() + '\n'
    string += 'issue: ' + data['Issue'][index].strip().rstrip() + '\n'
    string += 'pages: ' + data['Pages'][index].strip().rstrip() + '\n'
    string += 'authors: \"' +  data['Authors'][index].strip().rstrip() + '\"\n'
    string += 'image: /assets/images/papers/default-paper.svg\n'
    string += 'pdf: \n'
    string += 'pdflink: ' + data['PDF Link'][index].strip().rstrip()  + '\n'
    string += 'github: \n'
    string += 'pmid: \n'
    string += 'pmcid: \n'
    string += 'f1000: \n'
    string += 'figshare: \n'
    string += 'doi: ' + data['DOI'][index].strip().rstrip() + '\n'
    string += 'category: paper\n'
    string += 'published: true\n'
    string += 'peerreview: false\n'
    string += 'review: false\n'
    string += 'tags: ' + data['Tags(if available)'][index].strip().rstrip() + '\n'
    string += '---\n\n'
    string += '{% include JB/setup %}\n\n'
    string += '# Abstract\n\n'
    string += data['Abstract'][index].strip().rstrip()

    return string

for i in responses.index:
    string = getOutputString(responses, i)
    temp = responses['Acceptance Date/Year'][i].strip().rstrip().split('/')
    fileName = temp[2] + '-' + temp[0] + '-' + temp[1] + '-' + responses['Paper Title'][i].strip().rstrip().replace(' ', '-') + '.md'
    with open('../../MIDAS-IIITD_website/papers/_posts/' + fileName, 'w') as f:
        f.write(string)
