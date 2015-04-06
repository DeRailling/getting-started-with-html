import sys

def generate_concept_HTML(concept_title, concept_description):
    div_concept_title = '''
    <div class="concept">
        <div class="concept-title">
        ''' + " " + concept_title
    div_concept_descr = '''
        </div>
        <div class="concept-description">
        ''' + " " + concept_description
    div_closing = '''
        </div>
    </div>'''
    full_html_text = div_concept_title + div_concept_descr + div_closing
    return full_html_text

def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)

EXAMPLE_LIST_OF_CONCEPTS = [['Python', 'Python is a Programming Language'],
                         ['For Loop', 'For Loops allow you to iterate over lists'],
                         ['Lists', 'Lists are sequences of data']]    

def make_header():
    html_header='''
<head>
  <title>My Notes</title>
  <link rel="stylesheet" href="stylesheet.css">
</head>'''
    return html_header

def make_HTML_for_many_concepts(list_of_concepts):
    html_header=""
    #stage 
    concept_lesson =''' 
<div class="concept_lesson">'''       
    HTML=''
    concept_lesson_closing='''      
</div>
    '''
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML     
    html_header=make_header()
    return html_header + concept_lesson + HTML + concept_lesson_closing
   

print (make_HTML_for_many_concepts(EXAMPLE_LIST_OF_CONCEPTS))
    