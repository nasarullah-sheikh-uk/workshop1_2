from flask import Flask, render_template, request


def fileratings():
    #########################################
    # Open and dump the file in a list
    #########################################
    gotofile =  open ('filmratings.csv')
    file_content = gotofile.read()

    # replacing end splitting the text 
    # when newline ('\n') is seen.
    ratings = []
    file_into_list = file_content.split("\n")
    for line in file_into_list:
        name, stars = line.split(",")
        item = { 'name': name, 'star': stars }
        ratings.append(item)
    return ratings
    gotofile.close()


app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return "Hello World!"


@app.route('/films/list')
def filmlist():
    return render_template('files.html')

@app.route('/films/table')
def filmrating():  
    stars = request.values.get("stars", "")
    rat = fileratings()
    if ( stars == "" ):
        return render_template('filmrating.html', items=rat)
    else:
        orat = [ { 'name': 'Default', 'star': 0 } ]
        for ss in rat:
            if ss['star'] == stars:
                orat.append(ss)
                print (orat)
                break
        return render_template('filmrating.html', items=orat)


@app.route("/show-message")
def echo():
    name = request.values.get("name", "")
    message = request.values.get("message", "")
    return f"Hey there {name}! You said {message}"



