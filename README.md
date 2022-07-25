![SCREEN](https://i.postimg.cc/k4cVbbRW/banniere.jpg)

# || Branch: eibl_g || Project_ID : 963416 ||
- API_alpha

# How to install ?

For each developer, first install virtualenv.

  - pip install virtualenv

Then create a folder and activate a virtual environment.

  - virtualenv myproject source myproject/venv/bin/activate

After this, check-out the code from the code repository.

  - git clone <the_repo_url>

Now navigate to this sub-folder:

  - (venv) user@machine $ cd myproject/myrepo

Install the dependencies:

  - pip -r requirements.txt

!--- Py-Charm does this automatically when opening a new project. ---!

# Database

- Supposing you already have postgres installed, make a DB named api_alpha.
- Execute init_db.py ---> This will create you a table vins and users.
- Look in the code, you will have access to the credentials needed for DB connexion.

# Running the API

- Execute "Flask run" inside the prompted envirronnement ( need the env before )
- Register a new user
- Log in

# Api_alpha screen on date 25/07/2022 :

- Login page

![SCREEN](https://i.postimg.cc/tg81dkYQ/crud-1-login.jpg)

- Register page

![SCREEN](https://i.postimg.cc/vB940nV1/crud-2-register.jpg)

- Main page 

![SCREEN](https://i.postimg.cc/8cSj9CRZ/crud-3-main.jpg)

# Function and Endpoints :

# --- app.py

- Index

![SCREEN](https://i.postimg.cc/dtN1FnwM/index.jpg)

- Create

![SCREEN](https://i.postimg.cc/G3Qt7dfm/create.jpg)

- Update

![SCREEN](https://i.postimg.cc/8zFCzWz7/update.jpg)

- Delete

![SCREEN](https://i.postimg.cc/m2gDKKxN/delete.jpg)

# --- auth.py

- Login

![SCREEN](https://i.postimg.cc/0QbYPnBb/login.jpg)

- Register

![SCREEN](https://i.postimg.cc/W3CM3ZBS/register.jpg)

- Delete

![SCREEN](https://i.postimg.cc/8CyR29w2/delete-auth.jpg)


# Functionnality :

- Capable of adding, modifiy and delete objects in a Database.
- Login/Register/Logout.
- Authorisation.

# To add further :

- Adding image recognition 
- Adding trend calculator
- Adding wallet
- Adding trade service
