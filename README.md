# _learnscout_

* Domain: Education for employees in companies
* Status: live, but still in development [see here] (https://learnscout.digital)

## About the project:
  Especially big companies face the challenge that their employees with high seniority of 15+ years are lacking the digital skills needed for the digital transformation of the company. While those employees have been capable in their own profession for years, they don't have a lot of time for their upskilling, they miss direction about what is relevant and they want good learning material that they can use in their daily job immediately.

  _learnscout_ offers training content for employees tailormade for their roles and proficiency level.

## Structure:
The website consists of the following parts:

* **Welcome:** A landing page with logo and one-click option to start the interaction
* **Login:** By default, the user is directed to the login-page with email-address and password as identifier for login in
* **Register:** For new users a registration page requests a username, password and email-address. Also, a link to the terms & conditions of _learnscout_ is provided before a user signs in.
* **Get Guidance:** Depending whether the user is newly registered or has already used _learnscout_ he is asked to select his professional function he works in. Based on the selection he gets training content (WIP).
* **My Upskilling Plan:** This site is WIP. The user will get an overview of tailormade content based on the professional function
* **Logout:** A logout link in the navigation bar brings the user back to the welcome page

## Technologies:
HTML, CSS, JavaScript, Python, Flask

## Deployment:
* Server: Linode Server
* Handling requests via Nginx and Gunicorn
* Encryption: the site is a secure 'HTTPS' site with Certificates provided by Let's Encrypt (Certbot)

## Installation:
1. Clone the git hub: (https://github.com/Code10965/learn_scout.git)
2. Create and activate a Virtual Environment:
```bash
  python3 -m venv
```
```bash
  source venv/bin/activate
```
3. External libraries or dependencies are used therefore requirements are recommended to be installed:
```bash
  pip install requirements.txt
```
4. Run the application with Flask
```bash
  flask run.py
```

## Todos:
 - Finalise the pages that are currently WIP
 - Write and execute tests
 - Fill the site with training content
 - Execute usability tests

## Contributing:
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgments:
I want to thank my student rectangle team from CODE university of Applied Science for our awesome feedback sessions and support.
A big thank you to Valentin Silvera, who always supported me with patience and knowledge.
My special thanks go to Fabian Volkers: his energy, expertise and positive attitude helped me to survive all the nice challenges during this project.
