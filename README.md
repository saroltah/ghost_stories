# Ghost stories

Live website: https://ghost-stories-072f21228a45.herokuapp.com/

## Goal of the website

A community of short story writers specified on horror genres (ghost, vampire, etc.). The website is for amateur writers to show off their works, and for editors, who would like to find new talents.

### Wireframe

### Design

- **Colors:** I wanted to keep it simple, so I used only grays, one type of red and white. I chose the grey from the default profile picture. I Stored everything in CSS variables.

- **Fonts:** I used 4 types of font families. 
  - For the logo: **Permanent Marker, cursive**
  - The written font for the heading is beautiful: **Julee, cursive**
  - Light Written font mostly for names and titles, because it looks handwritten:**"Allura", cursive**
  - Simple font for long texts - more readable: **Karla, sans-serif **
- I styled mobile first design, then made it responsive.
### User experience

## Epics and user stories

I divided my user stories into different categories and also labeled them.

1. Epic:

### Existing features
**Authentication**:
- Sign up with username (email optional)

- Password repetition
- Log in with the “remember me” option
- Password reminder in email
- Sign out - with confirmation
- Only about and terms can be seen without signing in
- Sign-in - sign-out messages
- Authentication links in the menu

**Profile**

- Own profile link in the menu

- View and edit option (edit only for your own profile)
- Edit: name, image, About me (with text editor), choose goal: writer/editor, email, and phone number.
- Important messages can be read under the username: Email address and phone number can only be seen by the EDITORS! and image size can be a max of 10MB!
- Hide profile option: If a profile is hidden, no one can see it.
- Editor status doesn’t show the added story but shows the phone number and email on profiles. 
- Writers have added a story option, and can not see personal details on profiles (email and phone).
- On the profile and also in comments you can see if people are editors or writers.
- Automatic profile creation with the registered username


_NOTE: In the future, I will add the writer/editor option choice to the registration form, not to edit the profile, so the user can not change between._

**Add stories**

- Only for Writers

- Add the Title, teaser, keywords, and story text in a text editor.
- Edit option only for writers - can edit all the fields.
- Delete the story option.
- Message, when the story is published or edited, or deleted.

**View stories**

- Only logged-in users can read stories: In the story list - with title, author, and teaser. Option to read more button, to see the whole story.

- Filter story option: Enter a keyword, and it will give the links for the stories with those keywords. It is not case-sensitive.
- From the story list: edit/delete option for the authors, see all authors' profiles (by clicking their names)
- Clicking the title - read the whole story and - the authors’ profiles’ link, date (last edited), and like button - with the number of likes. Comments with name, text, and creation date, and add comment button.
- The newest story is on the top

_NOTE: The like button will be replaced in the future, now the page gets refreshed._


**Admin functions**

- View, edit, and delete users.
- View, edit, and delete profiles.
- View, edit, and delete Stories.
- View, edit, and delete Comments.


### Future features

#### In progress (I had no time for it)

- I planned to make different models for writers and editors - in the end, I used only one - so it is called writers. I will rename it to users…

- Add writer and editor options to sign up form and user table, so the user can not change it on their profile.
- Replace the LIKE button - right now it refreshes the page.
- Show all stories on the profile of the writer - using the filter method: queryset = Stroy.objects.filter.. and the author’s name should match the writer’s name.
- Log in with a social media account - Allauth gives the option for it
- Creating admin supervision conditions, so admin needs to approve stories before they are published.
- Add the number of comments the same way as I added the number of likes
- Add dislike button

#### Ideas:

- See the number of views, how many times the post has been open by other users

- Showing the editing history

 - The writer can choose, to share the story with a username or real name.

 - Program to be unable to add the same titles

- Inside chat for users

- Notification board for seeing likes or comments

## Deployment and forking

- **Github forking:**

1. Go to the selected repository, and click on Fork on the top right side.

2. Select an owner of the forked repository on the dropdown
3. Write a description and select the Default branch only for open-source projects.
4. Click on Create fork.
5. Go to your forked repository.
6. Click on Code, and copy the URL / or open with your Github desktop.
7. With the URL open your terminal, and write git clone and paste it. Enter.

<br>

- **Heroku deployment:**

1. On Heroku dashboard create new app with unique name
2. Settings - reveal the config vars - Add key DISABLE_COLLECTSTATIC with value 1 (later with staticfiles we delete it, but we add cloudinary details: CLOUD_NAME, API_KEY, SECRET_KEY.
3. Update our code: install gunicorn, and refresh requirement.txt
4. Create Procfile in the root directory, and add: web: gunicorn your_project_name.wsgi

5. In settings.py set Debug = False, and add ,'.herokuapp.com' to ALLOWED_HOSTS

6. Git add, commit, push to GitHub

7. On Heroku’s page click on Deploy tab, and connect your app with your GitHub repository.

8. Click on deploy branch - manually or you can set it up automatically. 

9. On the resources tab choose your plan (eco dinos). Verify that there is no existing Postgres database add-on, if so, click on Delete Add on.

10. After having static files, always run collectstatic command before deployment.

11. If any error occurs, can see the deployment log - on the top right side click on more, and chose view vlogs. Otherwise view app.


## Work progress

As my first Django project, I was not able to guess the time frame for the different tasks, but with more practice, I will be able to follow categories better.

I followed the agile methods, and MoSCoW labeling - must have, should have, could have, and won't have. I was prioritizing, and did first what was most important, then left the not important things to the end, set up the won't have features as future features.

I was making notes continuously, so I wrote down new ideas, what was working what was not, and where I needed to go back. Where I met with an error I couldn't handle, rather moved on due to the time frame I had, and decided to return later.

I worked on more user stories simultaneously.

### Set up the project: 

1. Set up my django, and set up .env file before publishing with my secret code.  

2. Publish the site on Heroku. I used an example page just to see if it was working.

3. Write epics and user stories.

4. Create the URL connections.


_NOTE These I did not make:
- https://gs/contact
- https://gs/user/username/change_password
- https://gs/user/username/stories
- https://gs/stories/storytitle/edit_comment
- https://gs/stories/storytitle/delete_comment 

 For these comment URL-s I need comment ID - or make it on page, so no extra URL needed

5. Create the model relationship tables.

6. Create the database.

### Create the body of the project: 

1. Add models (according to my Excel sheet): profiles, stories, and comments.

2. Import elements to the administration site, log in, and check if everything is working.

3. Add methods to classes.

4. Add comments and like classes to the stories. (_Note: later I united like with story class_)

5. Add story and profile views. I used generic views, so they can inherit from it. I added templates and URLs. I set up a test page, to make sure the template, the URLs, the views, and models are connected right.

6. Add stories through the admin panel, so I can see how the page will look.

7. Set up the homepage with a template and view.

8. Create basic HTML pages for index, stories, and profiles, to see, if it is working.  - I deployed it also and checked if everything was working.

9. Set up the authentication, and install all folders and files.

10. Add basic styling - base.html, so I added the rest of the links, buttons, etc to the right place, and can create more templates with visuals.

11.  Add edit and delete story view.

 ### Add details, functions and optimization:

1. Fix authentication

2. Filter comments to be seen only under their commented story

3. Add block titles

4. Add autoslug

5. Add summernote

6. Add forms.py

7. Add pagination.

8. Add signals.

9. Match username and writer name to edit and delete the story. 

10. Add JavaScript code to add value automatically to Author input. I found the input’s ID in the source code. Then I hide the author field. 'author': forms.HiddenInput,

11. Add an absolute URL as a link to the profile page.

12. Add forms to the profile (so the user can edit it)

13. Put CSS into their folders

14. Add images

15. Add likes

16. Add messages

17. Add filter story function

18. Add back buttons. Since there are some pages they can open directly from the menu, the JS back button makes more sense, than a link.

19. adding CSS variables

20. add profiles, stories, and photos.

21. Add styling

22. Testing and Error handling

23. Add writer-editor functionality with if statements.

24. Add hide profile functionality.

25. Deploy

26. Add Cloudinary

27. Testing, correcting errors, writing readme

### Languages

- HTML
- CSS
- Python
- JavaScript

### Libraries and frameworks:

- Django 4.2.10
- Django Allauth 0.57.2
- Whitenoise 5.3.0
- Django autoslug 1.9.9.
- Cloudinary 1.36.0, django-cloudinary-storage 0.3.0
- Django-summernote 0.8.20.0
- Django-heroku 0.3.1
- Gunicorn 20.1.0
- Pillow 10.3.0
- Slugify

imports: 

- from django.contrib import messages
- from django.views import generic
- from django.db import models
- from django.db.models.signals import post_save
- from django.dispatch import receiver
- from django.utils import timezone
- from django.utils.text import signify
- from django.urls import reverse, reverse_lazy, path
- from django.shortcuts import render, get_object_or_404, redirect
- from django.http import HttpResponseRedirect
- from django import forms
- from django_summernote.widgets import SummernoteWidget, - SummernoteInplaceWidget
- from django_summernote.fields import SummernoteTextFormField, SummernoteTextField
- from cloudinary.models import CloudinaryField
- from autoslug import AutoSlugField

### Tools, programs and technologies

- VSCode
- [Shecodes shadow and gradient generators](https://generators.shecodes.io/css-box-shadow-generator)
- GitHub projects
- GitHub Desktop
- ElephantSQL
- Bootstrap
- Heroku
- [Chrome color picker](https://chrome.google.com/webstore/detail/color-picker-for-chrome/clldacgmdnnanihiibdgemajcfkmfhia)

### Validating
- [Am I responsive](https://ui.dev/amiresponsive)
- [W3C CSS validator](https://jigsaw.w3.org/css-validator/)
- [W3C HTML validator](https://validator.w3.org/)
- [JS Hint](https://jshint.com/)
- [Python Validator](https://pep8ci.herokuapp.com/)

## Testing and validation
Lighthouse check for desktop devices:
Desktop:
Mobile:

### Error handling and bugs

1.  Added  env.py instead of .env to git ignore.. so published my secret key accidentally. I made a new secret key. Stopped following .env with this code:
git rm --cached .env

2. After adding models, I made a couple of mistakes and ran the terminal, which showed the errors one by one. Mistake 1: Blank should be blank. Mistake 2: I can not put onDelete on CharField.

3. Error while setting up writer view, 'Generic detail view Writer must be called with either an object pk or a slug in the URLconf.' - so I added slug.

4. Story with this Author already exists… It was a migration error, and I cleaned my migration data and migrated everything again

5. Comments were not displayed.Solution: Add get_context_data to one_story view: 
def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(commented_story=self.object)

6. Slug was empty...I didn’t refer to the author + writer ForeignKey relation. My code was: writer.slug - changed to: story.author.slug 

7. Refused to apply style from '<URL>' because its MIME type ('text/html') is not a supported stylesheet MIME type, and strict MIME checking is enabled.

So I changed CSS link in HTML: <link rel="stylesheet" href="{% static '/profiles/css/profiles.css' %}">
and add static source in settings.py also:
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),
                    os.path.join(BASE_DIR, 'profiles/static'), ]

8. I can only upload photos from admin. Solution: add  enctype="multipart/form-data" to form

9. The search engine is case-sensitive. Solution: I put both input values in lowercase: 
In forms.py the keywords:  'keywords': forms.TextInput(attrs={'placeholder': 'keyword1, keyword2, keyword3','style': 'text-transform:lowercase;'}),
in views.py the search field input: searched_keyword = request.POST['searched_keyword'].lower() 
10. Summernote editor is not responsive. Solution: I found the ID in the source code, so I could style it.

11. The back button of auth had a different color.. because it was inside the section. I put it outside, but I wanted the border around it, so I created a div around the section. 

12. Deployment error: slugify was not recognized.. - I refreshed requirement.txt.

13.  Exception Value: Must supply cloud_name in tag or in configuration. Solution: Add CLOUD_NAME, API_KEY, SECRET_KEY in config vars.

## Credits and sources

- git rm --cached .env: [dev.to](https://dev.to/dailydevtips1/removing-a-env-file-from-git-history-3gao)

- onClick="javascript:history.go(-1)" class=" edit": [Stack overflow](https://stackoverflow.com/questions/67360498/how-to-make-a-django-return-button-point-to-the-correct-previous-page)

-  enctype="multipart/form-data”: [Stack Overflow](https://stackoverflow.com/questions/45912825/image-upload-field-works-in-django-admin-but-not-working-in-template)

- from django.contrib import messages: [Stack overflow](https://stackoverflow.com/questions/67366138/django-display-message-after-creating-a-post )

- get context data: [Son’t repeat yourself](https://dontrepeatyourself.org/post/django-blog-tutorial-part-4-posts-and-comments/)
- putting menu to the left side: [Stack overflow](https://stackoverflow.com/questions/19733447/bootstrap-navbar-with-left-center-or-right-aligned-items)

- tutorial to add autoslug: [Django-autoslug](https://django-autoslug.readthedocs.io/en/latest/)

- signals tutorial: [Medium](https://medium.com/@abdullafajal/automating-user-profile-creation-with-default-data-using-django-signals-50abef9ce529)

- Django images tutorial:
[Dave Gray’s YouTube video](https://www.youtube.com/watch?v=GNsuF4xB80E&ab_channel=DaveGray)

- Django search engine tutorial [Codemy YouTube video](https://www.youtube.com/watch?v=AGtae4L5BbI&ab_channel=Codemy.com)

- read about block titles: [Zappycode](https://zappycode.com/tutorials/default-and-specific-titles-using-django-blocks)

- learned more about model qualities:
 [Official Django documentation](https://docs.djangoproject.com/en/5.0/ref/models/options/)

 - learned more about slug urls:
 [Learn django]( https://learndjango.com/tutorials/django-slug-tutorial) and [Stack overflow](https://stackoverflow.com/questions/71483831/django-how-to-add-slug-as-arguments-in-url-tag-using-django)

- learned more about model relationships: [Geeks for geeks](https://www.geeksforgeeks.org/textfield-django-models/)

- learned more about authentication: [Learndjango](https://learndjango.com/tutorials/django-allauth-tutorial)

- To solve migration errors, I used these websites for solution:
[Simple is better than complex](https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html),  [Stack overflow](https://stackoverflow.com/questions/48548878/psycopg2-dataerror-invalid-input-syntax-for-integer-test-getting-error-when), [another Stack overflow](https://stackoverflow.com/questions/29830928/django-db-utils-programmingerror-relation-already-exists), [Code.django project](https://code.djangoproject.com/ticket/29345)

- [ChatGPT](https://chat.openai.com): Throughout the project I used chat GPT to explain functionalities, what certain code snippets mean, how they work or don’t work. I learned a lot from it. 

-[John Elder, Codemy, Create a simple django blog playlist](https://www.youtube.com/playlist?list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi) : I watched the whole series, learned a lot from these videos!


### Content
 - All stories, about and terms text, and profile details were created by:
 [chatgpt](https://chat.openai.com/)

### Images, fonts

**images:**
- default profile photo: [unspalsh](https://unsplash.com/photos/a-black-and-white-photo-of-a-mannequins-head-doEEsAb890c)

- Other profile photos:
[unspalsh, Tomás Robertson](https://unsplash.com/photos/woman-in-white-crew-neck-shirt-HpyHow3ERS0), 
- [unspalsh, Euthah Mizushima](https://unsplash.com/photos/woman-in-white-elbow-sleeved-shirt-standing-near-white-train-in-subway-2TlAsvhqiL0)
- [unsplash, Vikor Talashuk](https://unsplash.com/photos/head-bust-form-bhoj9tHlsiY)

**fonts**:
- [google fonts Allura](https://fonts.google.com/?query=allura)
- [google fonts Julee](https://fonts.google.com/?query=julee)
- [google fonts Karla](https://fonts.google.com/?query=karla)
- [google fonts Permanent marker](https://fonts.google.com/?query=permanent+marker)

Special thanks to Code Institute and my mentor Ronan McClelland for reviewing, helping and answering all my questions.
