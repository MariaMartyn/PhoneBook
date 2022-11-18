from model import printDict


def create():

    res = printDict()
      
    style = 'style="font-size:15px;"'
    html = '<html>\n  <head></head>\n  <body>\n'
   
    for i in res.keys():
       
        html += '    <p {}>Surname: {} </p>\n'\
            .format(style, i)
        html += '    <p {}>Phone: {} </p>\n'\
            .format(style, res.get(i))
        
    html += '  </body>\n</html>'
    
    with open('index.html', 'w') as page:
        page.write(html)

    return html



