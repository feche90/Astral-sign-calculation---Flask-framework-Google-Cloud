from flask import Flask, render_template, request
app=Flask(__name__)

@app.route('/h')
def hello_world():
    return render_template('index.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/')
def zodiac():
    return render_template('zodiac.html')


@app.route('/result')
def result():
    
    main_dict={
        0:"Monkey",
        1:"Rooster",
        2:"Dog",
        3:"Pig",
        4:"Rat",
        5:"Ox",
        6:"Tiger",
        7:"Rabbit",
        8:"Dragon",
        9:"Snake",
        10:"Horse",
        11:"Sheep"
    }
    your_name=request.args.get("yname")
    birth_year=int(request.args.get("byear"))
    your_zodiac=birth_year%12
    birth_animal=main_dict[your_zodiac]
    p_animal=birth_animal+".png"
    return render_template('result.html', yname=your_name, byear=birth_year, yzodiac=your_zodiac, banimal=birth_animal, p_animal=p_animal)

@app.route('/list_animals')
def list_animals():
    return render_template('list_animals.html')

@app.route('/more_cosmo')
def more_cosmo():
    return render_template('more_cosmo.html')


if __name__=="__main__":
    app.run(debug=True)
