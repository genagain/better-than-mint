I use this as a repository as a base repository for my Python projects. Because of this, I decided to add my own instructions to my forked version of the `sampleproject` repository for my own reference.

The commands below clone my forked version of `sampleproject` into a repository called `repo-name`.

```
git clone git@github.com:genagain/sampleproject.git repo-name
cd repo-name
rm -rf .git
git init
```

Create a repository in Github called `repo-name` in a web browser.
Don't initialize the repository with a README.md, gitignore or a license.

Run the following commands to push the contents of your local copy of `repo-name` to the version on Github.

```
git add -A
git commit "initial commit"
git remote add origin git@github.com:genagain/repo-name.git
git push -u origin master
```

# A sample Python project

A sample project that exists as an aid to the [Python Packaging User
Guide][packaging guide]'s [Tutorial on Packaging and Distributing
Projects][distribution tutorial].

This project does not aim to cover best practices for Python project
development as a whole. For example, it does not provide guidance or tool
recommendations for version control, documentation, or testing.

[The source for this project is available here][src].

Most of the configuration for a Python project is done in the `setup.py` file,
an example of which is included in this project. You should edit this file
accordingly to adapt this sample project to your needs.

----

This is the README file for the project.

The file should use UTF-8 encoding and can be written using
[reStructuredText][rst] or [markdown][md use] with the appropriate [key set][md
use]. It will be used to generate the project webpage on PyPI and will be
displayed as the project homepage on common code-hosting services, and should be
written for that purpose.

Typical contents for this file would include an overview of the project, basic
usage examples, etc. Generally, including the project changelog in here is not a
good idea, although a simple “What's New” section for the most recent version
may be appropriate.

[packaging guide]: https://packaging.python.org
[distribution tutorial]: https://packaging.python.org/en/latest/distributing.html
[src]: https://github.com/pypa/sampleproject
[rst]: http://docutils.sourceforge.net/rst.html
[md]: https://tools.ietf.org/html/rfc7764#section-3.5 "CommonMark variant"
[md use]: https://packaging.python.org/specifications/core-metadata/#description-content-type-optional
