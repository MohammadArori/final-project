from flask import Flask, render_template, request, redirect, url_for
import dataset

app = Flask(__name__)
db = dataset.connect("postgres://typqlxxugqjyof:9d54ce31d149842942fc9ad81e1ffe1008c330e8b13c04a775867c3b5b3eee64@ec2-54-221-254-72.compute-1.amazonaws.com:5432/d1i3hr803iem45")


@app.route('/')
@app.route('/home')
def homepage():
	return render_template('home.html')

# TODO: route to /list

# TODO: route to /feed
@app.route('/register' , methods=["POST" , "GET"])
def register():
	contactsTable= db["contacts"]

	if request.method =="GET":
		return render_template("register.html") 
	else:
		form =request.form
		firstname = form["firstname"]
		lastname= form["lastname"]
		username= form["username"]
		hometown= form["hometown"]
		email =form["email"]
		personalwebsitelink=form["personalwebsitelink"]
		entry= {"firstname": firstname, "email":email , "username": username, "hometown":hometown , "personalwebsitelink": personalwebsitelink , "lastname":lastname}
	
		nameToCheck = username
        results = list(contactsTable.find(username = nameToCheck))
        print len(results)
        if len(results) == 0:
            taken = 0 
            contactsTable.insert(entry)
            print list(contactsTable.all())
            return redirect("/list")
        else:
            taken = 1
            return render_template ("register.html", taken = taken)	

@app.route("/list")
def ShowAll():
	contactsTable= db["contacts"]
	allContacts= list(contactsTable.all())
	print(allContacts)
	return render_template("list.html",contacts=allContacts)


# TODO: route to /error

if __name__ == "__main__":
    app.run(port=3000)











