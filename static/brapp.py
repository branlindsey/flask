from browser import document, ajax
import json

def get_input_coefficients():
    a = document['a'].value
    b = document['b'].value
    c = document['c'].value
    d = document['d'].value
    
    return {'a': float(a),
            'b': float(b),
            'c': float(c),
            'd': float(d)}

def display_solutions(req):
    result = json.loads(req.text)
    # note the syntax for setting the child text of an element
    document['solution'].html = f"{result['prediction']}"

def send_coefficient_json(coefficients):
    req = ajax.Ajax()
    req.bind('complete', display_solutions)
    req.open('POST',
                '/solve',
                True)
    req.set_header('Content-Type', 'application/json')
    req.send(json.dumps(coefficients))

def click(event):
    coefficients = get_input_coefficients()
    send_coefficient_json(coefficients)

document['solve'].bind('click', click)


</script>