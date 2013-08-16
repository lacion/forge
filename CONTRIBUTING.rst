============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given. 

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/lacion/forge/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug"
is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "feature"
is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

forge could always use more documentation, whether as part of the 
official forge docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/lacion/forge/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `forge` for local development.

1. Fork the `forge` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:lacion/forge.git

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature


I strongly encourage the use of gitflow

4. Create a branch for local development::

    $ git flow feature start name-of-your-bugfix-or-feature



Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8 and the
tests::

    $ flake8 --max-line-length=120 forge tests
	$ python setup.py test

To get flake8 , just pip install it into your virtualenv.

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

the only flake8 rule were changing is the line length up to a 120 chars --max-line-length=120

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 2.7 Check
   https://travis-ci.org/lacion/forge/pull_requests

Tips
----

To run a subset of tests::

	$ python -m unittest tests.test_forge
