🧠 Learning Journal – Exercise 2.1: Preparing Django Development Environment

📌 Overview
In this exercise, I prepared my system for Django development by ensuring Python, virtual environments, and VSCode were properly installed and configured. I also researched Django’s popularity, identified companies that use it, and evaluated scenarios where Django is or isn’t the right choice. Finally, I created and activated a new virtual environment, installed Django, and verified the installation.

🛠️ What I Did

- Researched why Django is popular and listed five major companies using it:
- Instagram (social media, scalability)
- Pinterest (visual discovery, large-scale data handling)
- Mozilla (web apps, community platforms)
- Disqus (comment hosting, moderation tools)
- Dropbox (cloud storage, web interface)

- Answered scenario-based questions on when Django is suitable:
- ✅ Multiple users → Yes (authentication/session support)
- ✅ Fast deployment → Yes (MVT + DRY principles)
- ❌ Very basic app → No (overkill, Flask better)
- ❌ Full control from scratch → No (Django enforces strict structure)
- ✅ Big project with support → Yes (community + documentation)

- Verified Python installation with py --version and documented with a screenshot.
- Created a new virtual environment named achievement2-practice using mkvirtualenv.
- Activated the environment successfully ((achievement2-practice) appeared in
- prompt).
- Installed Django with py -m pip install Django.
- Verified installation using django-admin --version and captured a screenshot.
- Compiled all answers and screenshots into a PDF for submission.
- Organized files in GitHub under Achievement 2/Exercise 2.1.

✅ What I Learned

- Django’s popularity comes from its batteries-included features, scalability, and strong community support.
- Different frameworks suit different project sizes: Django for complex apps, Flask for lightweight apps.
- How to reliably set up and activate virtual environments on Windows using virtualenvwrapper-win.
- Importance of quoting paths with spaces (e.g., "C:\Users\Saguna Nathani\...") when activating environments.
- How to install and verify Django inside a virtual environment for isolated project development.
- Reinforced the value of documenting each step with screenshots for clarity and reproducibility.

📸 Deliverables

- PDF file: Achievement2_Exercise2.1_DjangoSetup.pdf
- Screenshots:
  - Python version check
  - Activated virtual environment
  - Django installation and version check
- Updated Learning Journal entry (this file)

💬 Reflection
This exercise helped me bridge research with practical setup. I now understand not only why Django is widely used but also how to prepare my system to work with it. The strict “Django way” initially felt limiting, but I see how it enforces consistency and speeds up development. Setting up the environment and resolving path issues gave me confidence in troubleshooting. I feel ready to move forward with building my first Django project in the next exercise.
