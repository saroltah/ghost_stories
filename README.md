# Ghost stories

Live website: 

## Goal of the website

A community of short story writers specified on horror genres (ghost, vampire, etc.). The website is for amatour writers to show off their works, and for editors, who would like to find new talents.

## Planning

1. I draw wireframe, how the website should look like, what pages should have
2. Created user stories
3. Planned my URL paths
4. Made a model relationship diagram

### Wireframe

### Design

- Colors:
- Fonts:

### User experience

## Epics and user storys

I divided my user stories to different categories, and also labelled them. 

1. Epic: 

### Existing features
### Future features

 - Writer can chose, to share the story with username or real name.

 - Program to be unable to add the same titles

## Deployment and forking

- Github:

- Heroku

## Work progress

As my first django project, I was not able to guess the time frame for the different tasks, but with more practice I will be able to follow categories better.

I followed the agile methos, and MoSCOw labelling - must have, should have, could have and won't have. I was prioritizing, and did first what was most important, than left the not important things to the end, set up the won't have features as future future feature.

I was making notes continuosly, so I wrote down new ideas, what is working what is not, where I need to go back. Where I met with an error couldn't handle, rather moved on due to the time frame I have, and decided to return later.

I worked on more user stories simultaneously.

1. Set up my django, and set up .env file before publishing with my secret code.  
bug: I added env.py instead of .env to gitignore.. so published my secret key accidentally. I made a new secret key. Stopped following .env with this code:
git rm --cached .env

2. I published the site on Heroku. I used an example page just to see if it was working.

3. I wrote epics and user stories.

4. I created the URL connections.

5. I created the model relationship tables.

6. I created the database.

7. I installed the authentication, all auth.

8. I worked on my models (according to my Excel sheet): profiles, stories, and comments.

9. I imported elements to the administration site, logged in, and checked if everything was working.

10. I added methods to classes.

11. I added comments and like classes to the stories.

12. I added stories views. I used generic views, so it can inherit from it. I added a template and URL. I set up a test page, to make sure the template, the URL, the views, and models are connected right. 

13. I added the same files views and urls to to profiles - (I named the url users, that sounds better). Added slugs also.

14. I added stories through admin panel, so I can see how page will look.

15. I set up homepage with template and view.

16. I created basic html pages for index, stories and profiles, to see, it is working.  - I deployed it also, and check if everything is working.

17. I set up the authentication (I already have downloaded before) - installed all folders and files.

18. (so far: we had user site, stories site, can log in and out), I Styled the website - base.html, so I add the rest of the links, buttons, etc to the right place, and can create more templates with visuals.

19.  Add edit and delete view. Style them. 

### Languages

### Tools

### Technologies

- all auth

## Testing and validation

### Error handling and bugs

1. ERROR: ImportError: cannot import name 'Stories' from partially initialized module 'stories.models' (most likely due to a circular import) 

2. After adding models, I had couple of mistakes, run the terminal, which showed the erors one by one. Mistake 1: Blank should be blank. Mistake 2: I can not put onDelete on CharField.

3. Error while setting up writer view, 'Generic detail view Writer must be called with either an object pk or a slug in the URLconf.' - so I added slug.

## Credits and sources

- git rm --cached .env: 

[dev.to](https://dev.to/dailydevtips1/removing-a-env-file-from-git-history-3gao)

- model qualties: 
 [official django documentation](https://docs.djangoproject.com/en/5.0/ref/models/options/)

 - learning more about slug urls:
 [Learn django]( https://learndjango.com/tutorials/django-slug-tutorial)

 - all stories, about and terms text were written by:
 [chatgpt](https://chat.openai.com/)