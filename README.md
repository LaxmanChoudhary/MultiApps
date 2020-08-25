# MultiApps
a django site!

#### References
* [model field](https://docs.djangoproject.com/en/3.1/ref/models/fields/#textfield)  
* [Heroku-deploy-tutorial](https://devcenter.heroku.com/articles/getting-started-with-python#introduction)
	* Suggestions:  
		Error in `git push heroku master` refer [here](https://stackoverflow.com/a/63573388/8614751)  
		Error in `heroku ps:scale web=1` refer [here](https://stackoverflow.com/a/63584726/8614751)  
	* Follow the pattern, once basic is done.
		`git add . `  (add changes to local git)
		`git commit -m "msg"`  (commit changes)
		`git push -u origin master` (optional- if you also manage your git repo)
		`git push heroku master`  (push changes to heroku)
		`heroku open`  (open web-app)

> Tip: to add your dependencies to requirement.txt  
	pip freeze > requirement.txt