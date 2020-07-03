# Contributing

> You can contribute at will, you will always be welcome. But here are some rules to follow.

## Add/update features:

Did you look at the application and think about some functionality that should be added to the project ? :open_mouth:

**_So, you have two options:_**

- [Open an issue detailing your idea](#open-issue)
- [You implement the functionality yourself](#clone-the-repository)

## Open issue:

On the [project](https://github.com/Rickecr/PyTwitter) page, you can click on the `Issues` button and a`new issue` button will appear on the page, then just select and follow the following steps:

- Select the type of your issue: `Bug ou Feature`.
- Give your issue a good name
- Detail very well about the purpose of the issue.
- Images if possible.
- Select labels for your issue.
- Finaly, click on `Submit new issue`.

## Clone the repository:

On the home page of the [repository](https://github.com/Rickecr/PyTwitter) there is a `Fork` button. When you click, just wait to complete the fork. And then it will create the repository in your account. And now just clone in your machine, this:

```sh
git clone https://github.com/<name_user>/PyTwitter
```

When finished, you will have the repository on your computer and then just open in your preferred editor and make your changes.

Before you should create your branch for your development:

```sh
git checkout -b <name_branch>
```

For the name of the branch use the number of the issue to facilitate, ex: `issue_17`.

And now can begin the development :smiley: .

When you have finished make your changes, you should commit your changes, but first:

```sh
git add .
```

The above command will prepare all modified files to be committed, going through all the changes that were made by you where you will decide if the change will be added(you must be inside the project folder to use the command).
Now just commit the changes:

```sh
git commit -m "<Your_message>"
```

Remember to use message clear. If what you're solving already has an issue open, reference issue in commit.
Ex: `git commit -m "#17 - Add contributing.md"`

And finally, you will submit the changes to the remote repository:

```sh
git push --set-upstream origin <name_branch>
```

This is only the first time that submit a new branch to the remote repository, next times, just:

```sh
git push
```

But that will only in your fork, the official repository will not have its changes now what ? :confused:

Calm down, now that the `Pull Request` ou `PR`

### Pull Request

On your fork page, a yellow message will appear asking you to make a Pull request to the original repository. Clicking will open a page for you to fill in information about your PR.

- Reference the issue in that you are working on using: `#<number_issue>`

- Describe your changes.

- Wait by evaluation of your PR, and it may happen that we ask for some changes to be made. 
