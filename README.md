# MultiApps
a django site!

## #References
- [Model field](https://docs.djangoproject.com/en/3.1/ref/models/fields/#textfield)<br>

### `heroku`
- [Heroku-deploy-tutorial](https://devcenter.heroku.com/articles/getting-started-with-python#introduction)
	- Suggestions:<br>
		Error in `git push heroku master` refer [here](https://stackoverflow.com/a/63573388/8614751)<br>
		Error in `heroku ps:scale web=1` refer [here](https://stackoverflow.com/a/63584726/8614751)<br>
	- Follow the pattern when using `heroku cli`, once the first time setup is finished<br>
		`git add` (add changes to local git)<br>
		`git commit -m "<msg>"` (commit changes)<br>
		`git push -u origin master` (optional- if you also manage your git repo)<br>
		`git push heroku master` (push changes to heroku)<br>
		`heroku open` (open web-app)<br>

**Tip**:  
- to add your dependencies to requirement.txt<br>
`pip freeze > requirement.txt`<br>

# `site preview here`:
- [Multiapps](https://multi-app-django.herokuapp.com/)<br>
- Deployed on [Heroku](https://www.heroku.com)<br>

**`local login`**<br>
```
username: user1
password: ab12cd34
```
