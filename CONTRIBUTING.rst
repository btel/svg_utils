If you like the project and you would like to contribute, you can submit pull requests (PRs).

Make sure to included the following with your PR:

* short description of the contribution (in the Github form)
* unit tests for the code that you implemented
* documentation of new functions, classes etc.

You can also fix some the issues in the github tracker. 
If you decide to work on it, make sure to add a comment
saying that you take it. If there was no activity for 
a week on a PR or an issue, please feel free to adopt it.


## Code formatting

This project uses [black](https://github.com/psf/black) for automatically format the Python source code.
You can run the check and formatting hooks using pre-commit:

```
pip3 install pre-commit
pre-commit run --all
```

You can also integrate pre-commit with git, to run it for each commit:

```
pre-commit install
```
