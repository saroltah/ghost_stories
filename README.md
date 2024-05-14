# Ghost stories

Live website: https://ghost-stories-072f21228a45.herokuapp.com/
![Ghost stories front page](</readme/assets/ghost stories front.png>)
CONTENT:
- [Goal of the website](#goal-of-the-website)
- [Wireframe](#wireframe)
- [User experience](#user-experience)
- [Design](#design)
- [Epics and user stories](#epics-and-user-stories)
- [Existing features](#existing-features)
- [Future features](#future-features)
- [Deployment and forking](#deployment-and-forking)
- [Work progress](#work-progress)
- [Languages](#languages)
- [Libraries and frameworks](#libraries-and-frameworks)
- [Validating](#validating)
- [Manual testing](#manual-testing)
- [Credits and sources](#credits-and-sources)

## Goal of the website

The website creates a community of short story writers specified in horror genres (ghost, vampire, etc.). The website is for amateur writers to show off their works, and for editors, who would like to find new talents. 

### Wireframe

Due to the time limit, I drew my wireframes by hand. I decided to come back to that later using the wireframe program if I had time, but I have prioritized other parts of the development. 

Sign up and sign in: 

![sign up and sign in](</readme/assets/wireframe images/sign up and sign in page.jpg>) 

Stories and one story:

![wireframe image](</readme/assets/wireframe images/stories and one story page.jpg>) 

About and terms: 

![wireframe image](</readme/assets/wireframe images/about and terms page.jpg>) 

Add story and add comment:

![wireframe image](</readme/assets/wireframe images/add story and add comment page.jpg>) 

Desktop and mobile view profile page:

![wireframe image](</readme/assets/wireframe images/desktop and mobile view profile page.jpg>) 

Liked stories page (this I don't have): 

![wireframe image](</readme/assets/wireframe images/liked stories page.jpg>) 

Logged out and logged in home page

![wireframe image](</readme/assets/wireframe images/logged out and logged in home page.jpg>)

# User experience

#### Importnace of the website:
Amateur writers can show their work to a bigger audience, which improves their creativity, encourages them to practice and improve their writing skills
Users can receive feedback, which helps them improve, as well as provide encouragement and support.
The website creates a community between writers( and readers) who share similar interests.
 Editors can find hidden talents, it is a good business. If a writer proves to be talented, they might even receive opportunities in writing-related projects or publishing vents.

#### Design

The page is horror-themed, so I used dark colors, text, and box-shadow. My original idea was to make it black and white as in an old thriller movie and then put red as the color of blood. The font families I chose also mirror the style, they look gothic and mysterious. I used a gradient for the background, so it is still not boring. For that reason, I mixed the font families also.

I designed the page to be easily navigatable, that does not contain any unnecessary design, because it is all about the stories. The menu’s left side contains About and Terms links, while the Right side the profile, stories, and/or authentication. 

The user gets a notification to confirm he sent/deleted or edited something. 
- **Colors:** I wanted to keep it simple, so I used only a light grey, a dark red, and white. I chose the grey from the default profile picture. I Stored everything in CSS variables.

Default profile picture: 

![Default profile photo](</readme/assets/34. getting colors from default image.png>)


- **Fonts:** I used 4 types of font families.
  - For the logo: **Permanent Marker, cursive**
  - The written font for the heading is beautiful: **Julee, cursive**
  - Light Written font mostly for names and titles, because it looks handwritten:**"Allura", cursive**
  - Simple font for long texts - more readable: **Karla, sans-serif **
- I used mobile-first design, then made it responsive.
- I made buttons match for consistency with classes. Back-button, basic-button, and auth buttons are the same. This way I also avoid repetition. 

- Pages related to authentication have borders around, to make it a little different, and the page_not_found also has a border, but unlike in authentication pages, the back button is out of the border, which represents that this page is not found.

## Epics and user stories

I used GitHub projects, to write down all the important features I needed in my website, using user stories. I divided my user stories into different categories (I would make them as epics), so it is easier to see my progress or find a story I need. I also labeled them by the MoSCoW prioritization: must-have, should have, could have, won’t have, and put a question mark for those, I need to do research on how to implement. 
As I started/finished a task, I moved it from the to-do list to the in-progress and then Done list.
I haven’t accomplished everything I planned, but I closed all issues, and the ones that are not finished, I will move to version 2 of this project. All user stories have acceptance criteria also.

![Github projects](</readme/assets/23. using github project.png>)

**Categories:**

Admin: All user stories related to admin activities
Profile: Everything about the user profile
Sign up: Authentication stories
Sign in: Stories about logins, logouts, and passwords.
Stories: Involves stories connected to adding, editing, viewing, etc stories.
Communication: It involves users getting in contact with each other.
Interaction: Users interact through their stories, comments, likes
Menu: Stories related to the menu and navigation


As my project involved, I changed some prioritization, but this is the original version of my plans and user stories:

**Must have**:

1. **Admin: Styling website:** As an admin, I provide eye-catching but easy-to-follow design, so it gives a remarkable user experience.
Menu on the top, toggle in mobile view
Responsive
Matching colors and font style
All the pages are similarly styled

 2. **Interaction:  Date of the posts:** As a user, I want to see when the posts were published, so I can see if it is new.
When I open stories, the published date should is written.
The published date is automatic, and can not be changed.
There is a separate date for the editing.

3. **Interaction: Like a post:** As a user I want to like the posts, so I can express and show to the writers that I like them.
Heart smiley under the stories.
Clicking on it changes the smiley (color or size).

4. **Interaction: Delete comment:** As a user, I want to delete my comment, so I can change my mind about it with no commitment.
There is a delete button next to the comment.
Clicking on it, the comment disappears.
5.** Interaction: Edit comment:** As a user, I want to edit my comment, so I can correct it if I make a mistake.
There is an edit option under the comment.
Clicking it, the user can rewrite their comment.
Then by clicking the Send button again, the edited comment is published.
6. **Interaction: Commenting post:** As a user, I want to comment under posts, so I can express my opinion, advice, or criticism.
Under the posts, there is an option to leave a comment.
The comment field has a limited length.
There is a Send button, to send the comment.

7. **Stories: Title of the post:** As a writer, I want to add a title to my story so it is unique and easily recognized.
When adding a story, there is an option to add a title.
It can be edited when the writer edits the story.
The title field has a limited length.

8. **Stories: Deleted post notification:** As a writer, I want to get confirmation that my post was deleted, so I know it was successful.
After successful deleting, a notification should pop up, that the story is deleted.
If it is not successful, the notification says, something went wrong, please try again.
9. **Stories: Edited post notification:** As a writer, I want to get confirmation that my post was edited, so I know it was successful.
After successful editing, a notification should pop up, that the story is edited.
If it is not successful, the notification says, something went wrong, please try again.
10. **Stories: Published post notification:** As a writer, I want to get confirmation that my post was published, so I know it was successful.
After successful publishing, a notification should pop up, that the story is successfully published.
If it is not successful, the notification says, something went wrong, please try again.
11. **Stories: Delete Story:** As a writer, I want to delete my post, so if I am not satisfied, it doesn't need to stay on the page.
When I open my post, there is a delete button under it.
Clicking on the button deletes my story with the comments and likes under it.
12. **Stories: Edit post:** As a writer, I want to edit my posts, so I can correct mistakes.
When I open my story, there is a button to edit the story.
Clicking on the button, I can edit my story.

13. **Stories: Publish story:** As a writer, I want to be able to write and publish stories.
In the menu, there is the option to create a story.
Clicking on that leads to the board, where I can add different details.

14. **Profile: Delete profile:** As a user, I want to delete my profile, so I can finish using the page.
Delete button/link on the profile site.
As I click on the link, it asks if I want to delete the profile.
Clicking yes leads back to the homepage.
15. **Profile: Edit profile:** As a user, I want to be able to edit my profile, so I can make it personal.
There is an edit button.
There is a save button.
When the edit button is clicked, the fields are rewritable.
When the save button is clicked, the data is saved.

16. **Login: Sign-out notification:** As a user, I want to get a notification about logging out, so I know my log-out was successful.
After clicking the log-out button, and getting into the log-out page, a message appears: You are signed out.
If logging out was not successful, the message says: there was an error, try again.
17. **Login:  Sign-in notification:** As a user, I want to get a notification about signing in, so I know my sign-in was successful.
After clicking the sign-in button, and getting into the sign-in page, a message appears: You are signed in, as username.
If sign-in was not successful, the message says: there was an error, try again.
18. **Login:  Sign out: as a user:** As a user I want to be able to sign out, so I can save my details and personal page, and quit my workspace.
Visible sign-out button in the menu.
When it is clicked, the user is no longer logged in.
It leads back to the main page, or to the signed-out page.


19. **Sign up: Sign-up error:** As a user, I want to get an error message if something is not right with my registration so I can correct the error, or move on.
The message pops up saying something went wrong.
It suggests trying again, or the possible error options.
It pops up only when an error happens.

20. **Sign up:  Sign up confirmation:** As a user, I want to get confirmation about signing up, so I know my registration was successful.
-Message that says you are signed up.
It only shows a message if the registration is successful.
21.**Sign up:  Sign up with password:** As a user, I want to sign up with a password, so I can make it a unique, and safe way to log in.
Find the form on the start page or in the menu
The right fields appear to be filled out
22. **Menu: About information:** As a user, I want to read about the website’s purpose so that I can see if it is for me.
Opened from the menu
Contains info about what the website is used for

23. **Menu: Easy navigation:** As a user, I want to easily access the website’s options, so it is clear how to use the page.
Links on the top.
Readable.
Links to the correct page.
It opens in the same tab.

**Should have**

24. **Admin: Supervising profiles:** As an admin, I want to supervise profiles and decide whether to delete or publish them, so there is no inappropriate content on the website.
Open the admin site, and see the profiles.
Decide to publish or delete (only if inappropriate).

25. **Admin: Supervising comments:** As an admin, I want to supervise comments and decide whether to delete or publish them, so there is no inappropriate content on the website.
Open the admin site, and see the comments.
Decide to publish or delete (only if inappropriate).
26. **Admin: Supervising posts:** As an admin, I want to supervise posts and decide to delete or publish them, so there is no inappropriate content on the website.
Open the admin site, and see the posts.
Decide to publish or delete (only if inappropriate).

27. **Communication: Profile view:** As an editor, I want to see the writers' profiles, so I can contact them by mail.
Click on the name of the writer
That leads to the profile, with the public details. (all but password)

28. **Interaction:  Filtering posts:** As a user, I want to be able to filter the posts, so I can find the ones I am interested in.
Opening the stories from the menu, there is an option to filter.
I choose from more options, how I want to filter by.
Clicking on the option, the page only shows those stories, which went through the filter.
29. **Interaction:  Number of comments:** As a user, I want to see the number of comments, so I can see how many people commented on a story.
Next to the like session, there is another smiley representing the comments.
Next to the smiley, there is a number showing how many users have sent a comment.
Every comment increases the number by 1.
( - If someone deletes a post, the number is reduced by 1. )
30. **Interaction:  Number of likes:** As a user, I want to see the number of likes, so I can see how many people like the story.
Next to the heart smiley, there is a number showing how many users clicked on the button.
Every like increases the number by 1.
If someone dislikes the post, the number is reduced by 1.

31. **Stories: Teaser of the story:** As a writer, I want to add a teaser, so it brings the attention of other users, and they can decide if they are interested in reading my whole story.
When adding a story, there is an option to add a teaser.
It can be edited when the writer edits the story.
The teaser field has a limited length.
32. **Stories: Keywords of the post:** As a writer, I want to add keywords to my stories so that other users can filter and find them more easily.
When adding a story, there is an option to add keywords.
It can be edited when the writer edits the story.
The keywords field has a limited length.

33. **Profile: Stories posted:** As a writer, I want my profile to show all the stories I posted, so it is collected in one place.
There is a link to the user's stories.
Clicking on the link shows all the stories written by that user.
34. **Profile:  About me section:** As a user, I want to add an About me section so that potential employers, colleagues, or friends can read my back story.
There is a default text section.
Clicking in the field lets the user write their text.
There is a maximum length given.
35. **Profile: Profile photo:** As a user, I want to refresh my profile photo, so others can see who I am.
There is a default image.
There is a link to "Change my photo" under the image.
Clicking on the link I can upload an image from my computer.
There is an option to delete the profile photo.

36. **Sign up: Writer or editor account:**  As a user, I want to choose the option to sign up as a writer or as an editor, so I can use the website for my special needs/roles
-Two clickable options after signing up: Writer / Editor
Different details they need to add for registration
 
37. **Menu: Terms and conditions:** As a user, I want to have official terms that protect my rights so that I can safely use the website.
It is accessible from the menu.
It describes the rules of posting and commenting and the consequences of inappropriate behavior.

**Could have**

38. **Admin: Notification of supervising comments:** As an admin, I want to send the notifications, that the comment is under supervision.
When the user publishes a comment, a notification pops up: The content is under supervision.
When the admin accepts the comment, the notification says the content is published.
39: **Admin: Notification of supervising posts:** As an admin, I want to send the notifications, that the post is under supervision.
When the user publishes a post, a notification pops up: The content is under supervision.
When the admin accepts the post, the notification says the content is published.
40. **Interaction: Notification of likes:** As a user, I want to get a notification if someone likes my post, so I know immediately that it happened.
There is a notification button, where the menu is.
The button shows a sign if there is a new notification.
Opening the notifications, the user can read, that they got a new like.
41. **Interaction:  Dislike a post:** As a user, I want to dislike a post, so it is not a problem if I accidentally hit the button, and I can take back my likes.
After clicking on the like button (smiley) clicking it again, changes back, takes back the like.
42. **Interaction:  Notification of comment:** As a user, I want to get a notification, that someone commented on my post.
When I send the comment, a notification pops up, that the comment is sent.
If an error comes up, the notification says, something went wrong, please try again.

43. **Interaction: Notification of comments:** As a user, I want to get a notification if someone comments on my post, so I know immediately that it happened.
There is a notification button, where the menu is.
The button shows a sign if there is a new notification.
Opening the notifications, the user can read, that they got a new comment.

44. **Stories: Number of views:** As a writer, I want to see the number of views, so I can see how many people read my story.
When I open my story, it has an eye emoji and a number next to the like and comment section.
The number shows how many times the story was clicked on.
45. **Stories:  Styling the post:** As a writer, I want to style my post so it is prettier, looks more interesting, and is easier to read.
When adding/editing the story, there is an option for styling.
When adding/editing the story, there is an option for removing styling.
46. **Stories:  Editing history:** As a user, I want to see the previous versions of the edited stories, so I see how the stories improved.
There is a button called, edited.
Clicking on the button shows the changed parts.
47. **Profile: Stories liked:** As an editor, I want to see all the posts I liked, so I can look them back.
There is a link to Liked stories
Clicking on the link shows the stories being liked by the editor.

48. **Profile: Linked in / website:** As a user, I want to add a social media account or website link so that others can get to know me better.
There is a field where links can be given.
When the user edits the profile, they can click on the field
49. **Profile: Hiding profile:** As a user, I want to choose if I hide my profile.
There is a button that says Don't show my profile.
The other users can not open the profile when the button is triggered.
After the button changes to unhide my profile - so it does the opposite.
50. **Log in: Remember me option:** As a user I want the computer to remember me, so the next time I log in it goes quicker.
There is a checkbox on the log-in site.
When the checkbox is clicked, the name and password are saved as default.
For log-ins after, the fields are filled with the default data.

51. **Log in: Password reset:** As a user, I want to reset my password if I don’t remember it, so I can log in again.
There is a link under the password field: Reset password.
There is a field to fill out the email address.
A random new password is sent to the given email, as soon as the link is clicked.
The new password is automatically given to the user's profile.
52. **Log in: Password in the email:** As a user, I want to get an e-mail reminder if I don’t remember my password, so I can see it in my emails.
There is a clickable link or button that Have you forgotten your password? Send it by e-mail.
The email is sent to the given e-mail address immediately, as the button is clicked.
The link is under the password field.
53. **Sign up: Editor validation:** As an editor, I want to validate myself, so the writers know I am official and not catfish.
Get a green arrow if it is proven that the user is who they tell they are.
Upload a photo of the ID.
54. **Sign up: Sign up email:** As a user, I want to get a confirmation email about signing up, so I have proof about signing up if any error comes up.
The email is sent out to the given email address.
The email contains the sign-up details.
The email is sent out automatically and immediately as the registration is done.
55. **Sign up: Sign up with social media:** As a user, I want to sign up with my social media, so it is quicker and easier without typing so much.
Link to sign up with Google account
Link to sign up with a Facebook account
A question from the website if it allows the user's data for the registration
Automatical fill out

56. **Communication: Inside chat:** As a user, I want to be able to write messages to the other users, so we can get in touch, and talk privately.
Message sign next to the user's name
Clicking on it opens a window, where the chat is possible

**won’t have**
 
Originally I didn’t put anything here, just as the project involved. In the end, I put here Inside chat, and notification buttons because I was sure I would not implement them. The rest I left, and will be moved to the next coding version.

### Existing features
**Authentication**:
- Sign up with username (email optional)

- Password repetition
- Log in with the “remember me” option
- Sign out - with confirmation
- Only about and terms can be seen without signing in
- Sign-in - sign-out messages
- Authentication links in the menu

**Profile**

- Own profile link in the menu

- View and edit option (edit only for your own profile)
- Edit: name, image, About me (with text editor), choose goal: writer/editor, email, and phone number.
- Default profile picture
- Change or reset their password
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
- Any user can leave a comment, with the name the status (writer/editor) also written out

_NOTE: The like button will be replaced in the future, now the page will be refreshed._


**Admin functions**

- View, edit, and delete users.
- View, edit, and delete profiles.
- View, edit, and delete Stories.
- View, edit, and delete Comments.

**Error handling**:

- If a user makes a wrong request, or looks for a non-existing page, it redirects to a custom “page not found” template. 

### Future features

#### In progress (I had no time for it)

- I planned to make different models for writers and editors - in the end, I used only one - so it is called writers. I will rename it to users.
- Add writer and editor options to the sign-up form and user table, so the user can not change it on their profile

_Note: The original plan was to have 2 interfaces with different actions. One for writers, one for editors. Difference: Writers can add a story, and read each other’s story, but can not see the personal details of other writers. The editors can not share stories, they are there to discover new talents. They can open the writer's profiles, and see their contact details so that they can call or write and offer a job or mentorship._

- Replace the LIKE button - right now it refreshes the page. Also add transaction handling to it, in case 2 people click on it at the same time.

- Show all stories on the profile of the writer - using the filter method: queryset = Stroy.objects.filter.. and the author’s name should match the writer’s name.
- Log in with a social media account - Allauth gives the option for it
- Create an admin supervision interface, so the user sees that the admin needs to approve stories before they are published.
- Add the number of comments the same way I added the number of likes
- Add a dislike button
- Add delete account option 
- Add edit/delete comment function.

- Reset password: The registration is happening by username, not email. So connection is not found (even if I added email at registration) The registration form needs to be changed, or the reset password form, to be connected with username (and then email).

#### Ideas:

- See the number of views, how many times the post has been opened by other users

- Showing the editing history

 - The writer can choose, to share the story with a username or real name.

 - Program to be unable to add the same titles

- Inside chat for users

- Notification board for seeing likes or comments

## Deployment and forking

-**Create Github project**
1. Create a new repository
2. In the menu click on project > Link a project > Create new project 
3. Click on Board, and give a name > Create
4. Click on the three dots menu, choose workflows
5. Item added to project > Edit
6. Click on issue dropdown, select issue, unselect pull request
7. Status value: status to do > green button: Save and turn on workflow.
8. In your project’s three dots menu (exit workflow) click on Settings
9. In the danger zone section choose visibility. 
10. Add user story template: Go to your repository’s settings > Features > Issues > Set template > Custom template (fill out) > Propose changes > Commit changes
11. Add user stories: In your repository’s menu click on issues > new issue > Get started! > Fill out, add labels, connect with your project > Submit a new issue

<br>

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

1. On the Heroku dashboard create new app with unique name
2. Settings - reveal the config vars - Add key DISABLE_COLLECTSTATIC with value 1 (later with staticfiles we delete it, but we add Cloudinary details: CLOUD_NAME, API_KEY, SECRET_KEY.
3. Update our code: install gunicorn, and refresh requirement.txt
4. Create Procfile in the root directory, and add: web: gunicorn your_project_name.wsgi

5. In settings.py set Debug = False, and add,'.herokuapp.com' to ALLOWED_HOSTS

6. Git add, commit, push to GitHub

7. On Heroku’s page click on the Deploy tab, and connect your app with your GitHub repository.

8. Click on deploy branch - manually or you can set it up automatically.

9. On the resources tab choose your plan (eco dinos). Verify that there is no existing Postgres database add-on, if so, click on Delete Add-on.

10. After having static files, always run the collectstatic command before deployment.

11. If any error occurs, can see the deployment log - on the top right side click on more, and choose view vlogs. Otherwise, view app.


## Work progress

As my first Django project, I was not able to guess the time frame for the different tasks, but with more practice, I will be able to follow categories better.

I followed the agile methods, and MoSCoW labeling - must have, should have, could have, and won't have. I was prioritizing, and did first what was most important, then left the not important things to the end, set up the won't have features as future features.

I was making notes continuously, so I wrote down new ideas, what was working what was not, and where I needed to go back. Where I met with an error I couldn't handle, rather moved on due to the time frame I had, and decided to return later.

I opened dev tools and source code all the time to check, how the data returned, look for different details, or try out different styles. It helped me find ID-s, understand the forms, and validate my html code.

I worked on more user stories simultaneously.

For clarity, I used comment-out lines for separate CSS and HTML sections, also named CSS elements according to their section.
 
### Set up the project:

1. Set up my django, and set up .env file before publishing with my secret code.  

2. Publish the site on Heroku. I used an example page just to see if it was working.

3. Write epics and user stories.

4. Create the URL connections.


_NOTE These URLs I did not make:_
- https://gs/contact
- https://gs/user/username/change_password
- https://gs/user/username/stories
- https://gs/stories/storytitle/edit_comment
- https://gs/stories/storytitle/delete_comment

 _For these comment URL-s I need comment ID - or make it on the page, so no extra URL is needed_

5. Create the model relationship tables.

6. Create the database.

### Create the body of the project:

1. Add models (according to my Excel sheet): profiles, stories, and comments.

2. Import elements to the administration site, log in and check if everything is working.

3. Add methods to classes.

4. Add comments and like classes to the stories. (_Note: later I united like with story class_)

5. Add story and profile views. I used generic views, so they can inherit from it. I added templates and URLs. I set up a test page, to make sure the template, the URLs, the views, and models are connected right.

6. Add stories through the admin panel, so I can see how the page will look.

7. Set up the homepage with a template and view.

8. Create basic HTML pages for index, stories, and profiles, to see, if it is working.  - I deployed it also and checked if everything was working.

9. Set up the authentication, and install all folders and files.

10. Add basic styling - base.html, so I added the rest of the links, buttons, etc to the right place, and can create more templates with visuals.

11.  Add edit and delete story view.

 ### Add details, functions, and optimization:

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

19. adding CSS variables:

  - grey-gradient: linear-gradient(1deg, rgba(0, 0, 0) 20%, rgb(22, 22, 22) 80%);
  - light-grey-color: #9a9997;
  - red-color: #a6071a;
  - written-font: "Julee",
    cursive;
  - thick-written-font: "Permanent Marker",
    cursive;
  - light-written-font: "Allura",
    cursive;
  - basic-font: "Karla",
    sans-serif;
  - white-text-shadow: 10px 12px 34px rgba(255, 255, 255, 0.9);
  - red-text-shadow: 0px 0px 31px rgba(166, 7, 26, 1);
  - white-box-shadow: 2px 12px 50px 1px rgba(255, 255, 255, 0.8);
  - red-box-shadow: 9px 16px 51px 13px rgba(166, 7, 26, 1)



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

_NOTE: I used in-line JS, and did not put any JS code in a separate file, because it was a couple of lines, and I prioritize performance, so it doesn’t need to load an extra file._

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

### Tools, programs, and technologies

- VSCode
- [Shecodes shadow and gradient generators](https://generators.shecodes.io/css-box-shadow-generator)
- GitHub projects
- GitHub Desktop
- ElephantSQL
- Bootstrap
- Heroku
- [Chrome color picker](https://chrome.google.com/webstore/detail/color-picker-for-chrome/clldacgmdnnanihiibdgemajcfkmfhia)

### Validating

- [W3C CSS validator](https://jigsaw.w3.org/css-validator/) - shows no error
- [W3C HTML validator](https://validator.w3.org/) 



I used the source code for validation. - Django’s automatically generated forms, and summernote show error! My code without this automatically generated code shows no error!

- [JS Hint](https://jshint.com/): Shows no error
- [Site 24x7 Js validator](https://www.site24x7.com/tools/javascript-validator.html): Shows one warning
- [Python Validator](https://pep8ci.herokuapp.com/): Shows no error

_Note: [Am I responsive](https://ui.dev/amiresponsive) was not working. I tried with different websites, but it didn’t load anything. I used dev tools to test._

Lighthouse checks for desktop devices:
Desktop:
Mobile:

## Manual testing

**Homepage:**
What is the expectation and how to test it? | Is it working? 
| :--- | :--: 
| I click on the logo, and it loads the home page (logged out, logged in also.) | Yes. 
| I click on About, and it loads the About page (logged out, logged in also.) | Yes. 
| On the About page I click on the Back button, and it brings me back to the previous page. | Yes.
| I click on Terms, and it loads the terms page (logged out, logged in also.) | Yes.
| On the Terms page I click on the Back button, and it brings me back to the previous page. | Yes.
| On the footer there are two links. left side: contact, email, right side. created by, copy right name.. | Yes.
| I click on footer email, and it opens a separate tab with my emailing program, filled out that email address as reciever | Yes.
| I click on my name and it opens my portfolio in separate tab | Yes.

<br>

**Authentication:** 

What is the expectation and how to test it? | Is it working? 
| :--- | :--: 
| I click on Register both in the middle and in the menu, it opens the register form | Yes. 
| I fill out the form and click on Sign up, if everything is fine, it redirects me to the signed-in webpage. | Yes. 
| The email field can be left empty, and I can still register. | Yes. 
| I get a message, that I am registered as my username, and I can close this message by clicking the x | Yes. 
| I write a username to register that already exists, text is written out that the username already exists.  | Yes. 
| I write not valid email, it throws a message, that it should contain @.  | Yes. 
| I write a username to register that already exists, text is written out that the username already exists.  | Yes. 
| I write not valid passwords (1,2,3,4) - it throws a message, that it is too short and too common.  | Yes. 
| I write two different passwords, and it throws a message that it should be the same. | Yes. 
| I click on remember me, next time I open the app, it automatically fills out the details. | Yes. 
| I click on login (all the three links tried, it loads the login form) | Yes. 
| I type the correct username and password, I am redirected to the logged-in homepage and get a successfully logged-in message | Yes. 
| I write wrong username and/or wrong password, it writes out that it is not correct | Yes. 
| I go to my profile, click on edit, and click on change password, it redirects me to the change password site. | Yes.
| I fill out the change password form correctly, and it refreshes the page and sends a message, that the change was successful. | Yes.
| At the change the password I write not valid passwords (1,2,3,4) - it throws a message, that it is too short and too common.  | Yes. 
| At the change password I write two different passwords, and it throws a message that it should be the same. | Yes. 
| Change password field: I click on the back button, and it brings me back to the previous page. | Yes. 
| The change password and back button changes color, when I click/hover them.  | Yes.
| I click on the logout button, and it redirects me to the logout page. | Yes
| It asks, if I want to log out, there are two buttons | Yes
| I click on Yes, log out button, and it redirects me to the homepage. | Yes
| I click on the logout page back button and it redirects me to the previous page. | Yes

<br>

**Profile:** 

What is the expectation and how to test it? | Is it working? 
| :--- | :--: 
| I click on the profile, and I see my profile’s view. on a smaller screen photo first, then details, on a bigger screen left side photo, right side details. I also see the edit link. | Yes.
| I click on the social media icon (Facebook/Instagram/LinkedIn and it opens the page in a new tab | Yes.
| Only those icons can I see, that I fill out in my profile | Yes.
| On the view profile page I click on the back button and it brings me back to the previous page | Yes.
| On the view profile page I click on the edit link, and it redirects me to the edit profile template | Yes.
| I click to leave the fields empty | Yes.
| The goal has two choices: Editor / Writer (I will rename it to status) | Yes.
| The vis dropdown has two choices: Visible and Hidden (I will rename this also) | Yes.
| The default goal is writer, and the default visibility is visible if I don’t change it. | Yes.
| As a writer I can see the add story link when I click on stories | Yes.
| As a writer I can not see the email or phone number when I view a profile(mine or I click on another author’s name)  | Yes.
| As an editor, I can see the email or phone number when I view a profile(mine or I click on another author’s name)  | Yes.
| As an editor, I can not see the add story link when I click on stories | Yes.
| When my profile is visible, I can see it, when I click on profile. When I click on another author’s name, who chose to be visible I can see their profile. | Yes.
| When my profile is hidden, I can not see it, when I click on profile. When I click on another author’s name, who chose to be hidden I can not see their profile. The page says this user has a hidden profile | Yes.
| I only see the edit button on my own profile | Yes.
| On the edit profile page I have a text editor to the about me section | Yes.
| On the edit profile page I I click on | Yes.
| I write a comment as a writer. Then changed my status(goal) to writer. In the comment, it also changes my status from writer to editor. I I click on | Yes.
| The story I write as an writer is still there, even touch i change my status to editor. | Yes. _Note: The future function will not let editors/writers to change their status_
| At the edit profile's image section I click on select file and select image from my computer. Then I click on update profile, it redirects me to the view profile page, and I can see my new image. | Yes.
| I upload big images from my professional camera, and since max size is 10 MB, it writes a message, that the max size is 10MB | Yes
| At the image section I click on the clear checkbox and update profile button, and my image changes back to the default picture.  | Yes.


<br>

**Stories:**

What is the expectation and how to test it? | Is it working? 
| :--- | :--: 
| I click on the Stories link from the homepage or from the menu and it redirects me to the Stories template | Yes.
| On the stories page, I can see the story title, story teaser, author, and date it was published or edited. | Yes.
| On the stories page, If I am the author of a story, I have an edit and delete story option under the author If I am not the author, I don’t see these links. | Yes.
| On the stories page, I click on the edit story link, and redirects me to the edit story page. | Yes.
| On the stories page, I click on the delete story link, and redirects me to the delete story page. | Yes.
| I click on the author’s name, and it redirects me to their profile. | Yes.
| I click on the Read more button and it redirects me to the story’s page, where I can read the whole story. | Yes.
| I click on the back button at the bottom of the stories page, and it redirects me to the previous page. | Yes.
| I click on add story, and it redirects me to the add story page. | Yes.
| To add story I need to fill out all fields. I left empty fields one by one, clicked on publish, and the page jumped to the empty field, and it writes out: This field is required, or Please fill out this page. | Yes.
| I click on Post, and my story is posted, I am redirected to the stories page and get a message: Story posted. | Yes.
| The stories are ordered by creation date, the newest is on the top. - I share stories, and they are on the top, also I can read their dates. | Yes.
| To find a story, I write a keyword to the search field, click on search, and it redirects me to the filter story page | Yes.
| I write upper and lowercase words, for example: Test and test, and the result is the same. | Yes.
| I write special characters and numbers, there is no match | Yes.
| I write just a piece of a word, for example hor (of horror), there is match. | Yes.
| I type more keywords with coma, it shows. | Likely no.*
| When there are more matches, I can see them under each other with title, and author. | Yes.
| I click on the matched link, it goes to the stories page. | Yes.
| On the one-story’s page I see the title, author,  publishing date, the whole story text, a like button with the number of likes, and a comment section. | Yes.
| I click on the author’s name under the title on the one-story page, and it goes to the writer’s profile. | Yes.
| I click on the like button, and the inner text of the button says: liked. Then the counting goes up to 1 number.  | Yes.  _Note: I want to edit/replace this button, so it doesn’t refresh the page._
| I click on the back button, and it goes back to the story list page. | Yes.
| I click on the add comment link, and it redirects to the add comment page. | Yes.
| I fill out the form and click on the send button, it redirects back to that story page, I commented.. | Yes.
| The latest comments are on the top. | Yes.
| If there is no comment yet, it says no comments yet, add one. | Yes.

*_Note: The keywords section counts as one word, space and coma also part of it. When I look for one word, I search for one part of it. If I look for more words (and don’t type the exact same snippet as in the keywords field) then it can not compare two separate parts of it._

<br>

**Last-minute changes**

What is the expectation and how to test it? | Is it working? 
| :--- | :--: 
| I click on the forget password link, and it redirects me to the reset password template. | Yes.
| I click on send email, and it sends the password to my email. | No. I realized since the email field is not obligatory, there is no connection between the user and the email. So for now I deleted this option.

<br>

**Design**

What is the expectation and how to test it? | Is it working? 
| :--- | :--: 
| All the links and all the buttons change color when I hover/click on them | Yes.
| I open the desktop, I should see the left side logo, about and terms, and the right side log in and register. | Yes.
| When I log in on a bigger screen (on my laptop) it shows Stories, Profil, and Log Out on the menu’s left side. | Yes.
| On a smaller screen the dropdown menu puts everything in the middle. | Yes.
| I open the stories page, the add story button is on the left, and the search field is on the right. | Yes.


<br>

**Error handling**

What is the expectation and how to test it? | Is it working? 
| :--- | :--: 
| I am not logged in, I just type in the URLs, and the page says please log in to see the stories or profiles. | Yes.
| I log in, open someone else's story, and change the url to edit-story, / delete-story. The page says only the author can edit/delete the story.| Yes.
| I log in, open someone else's story, and change the url to edit-story, / delete-story. The page says only the author can edit/delete the story.| Yes.
| I type in a not valid URL, and it redirects me to a custom error page, which says this page does not exist..| Yes.
| I log in as a writer and modify the URL to add a story. The page says only writers can share stories.| Yes.

<br>

**Admin:**

What is the expectation and how to test it? | Is it working? 
| :--- | :--: 
| I can see, edit, and delete posts as I log in to my admin site. | Yes. 
| I can see, edit, and delete comments as I log in to my admin site. | Yes. 
| I can see, edit, and delete profiles as I log in to my admin site. | Yes. 
| I can see, edit, and delete users as I log in to my admin site. | Yes. 

<br>

### Bugs and solutions

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

9. The search engine is case-sensitive. Solution: I put both input values in lowercase. In forms the keywords:
'text-transform:lowercase;',
in views.py the search field input: ['searched_keyword'].lower()

 After that altough it showed only lowercase letters, still the value was saved in uppercase. So I added a function with self.cleaned_data.get(), that changes all the data lowercase.

10. Summernote editor is not responsive. Solution: I found the ID in the source code, so I could style it.

11. The back button of auth had a different color.. because it was inside the section. I put it outside, but I wanted the border around it, so I created a div around the section.

12. Deployment error: slugify was not recognized.. - I refreshed requirement.txt.

13.  Exception Value: Must supply cloud_name in a tag or in configuration. Solution: Add CLOUD_NAME, API_KEY, SECRET_KEY in config vars.

But I added these names first, instead of how I saved them in my .env files. It was working for the first refresh, but after it threw a 505 error, “must supply API key”. So I printed out values in my settings.py, for debugging,  I also checked my Cloudinary page, and then when I checked again the config var values compared with .env values,  I realized, the names should be also the same.


14. Validation error: the element a must not appear as a descendant of the button element. - So deleted the buttons, and styled the links as buttons.

15. Image size error: When the Image was too big, it redirected the user to a server error page. I added a validator to the cloudinary image model, so it throws an error message if the image is too instead of redirecting to an error page.


<br>

**Known bugs:**

NONE


## Credits and sources

- git rm --cached .env: [dev.to](https://dev.to/dailydevtips1/removing-a-env-file-from-git-history-3gao)

- onClick="javascript:history.go(-1)" class=" edit": [Stack overflow](https://stackoverflow.com/questions/67360498/how-to-make-a-django-return-button-point-to-the-correct-previous-page)

-  enctype="multipart/form-data”: [Stack Overflow](https://stackoverflow.com/questions/45912825/image-upload-field-works-in-django-admin-but-not-working-in-template)

- from django.contrib import messages: [Stack overflow](https://stackoverflow.com/questions/67366138/django-display-message-after-creating-a-post )

- get context data: [Don’t repeat yourself](https://dontrepeatyourself.org/post/django-blog-tutorial-part-4-posts-and-comments/)
- push menu items to the right side: [System22WebDesign YouTube video](https://www.youtube.com/watch?v=Bb5B40QAkcs&ab_channel=System22WebDesign%7CDiviThemeElementorWP)

- self.cleaned_data.get('keywords'): [chatgpt](https://chat.openai.com/)

- Add validator to Cloudinary image field (validate_image_size(value) function): 
[chatgpt](https://chat.openai.com/)

- tutorial to add autoslug: [Django-autoslug](https://django-autoslug.readthedocs.io/en/latest/)

- signals tutorial: [Medium](https://medium.com/@abdullafajal/automating-user-profile-creation-with-default-data-using-django-signals-50abef9ce529)

- Error handling page tutorial: [Programming knowledge YouTube video](https://www.youtube.com/watch?v=gsW5gYTNi34&ab_channel=ProgrammingKnowledge)

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

- [John Elder, Codemy, Create a simple django blog playlist](https://www.youtube.com/playlist?list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi) : I watched the whole series, learned a lot from these videos!


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

Special thanks to Code Institute and my mentor Ronan McClelland for reviewing, helping, and answering all my questions.




