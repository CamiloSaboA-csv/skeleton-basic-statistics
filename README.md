# Python Tech Challenge
* The challenge is to create a program that computes some
basic statistics on a collection of small positive integers. You
can assume all values will be less than 1,000.
* Implement this challenge in whatever programming language
best highlights your skills. Also, please supply a README with
details on how to setup and run your application.


# Requirements
The DataCapture object accepts numbers and returns an object for querying
statistics about the inputs. Specifically, the returned object supports
querying how many numbers in the collection are less than a value, greater
than a value, or within a range.
Here’s the program skeleton in Python to explain the structure:

```
capture = DataCapture()
capture.add(3)
capture.add(9)
capture.add(3)
capture.add(4)
capture.add(6)
stats = capture.build_stats()
stats.less(4)
stats.between(3, 6)
stats.greater(4)
than 4)
```
## Expected output
```
2
4
2
```
## Explanation
* `stats.less(4)` Should return 2 (only two values 3, 3 are less than 4)
* `stats.between(3, 6)` Should return 4 (3, 3, 4 and 6 are between 3 and 6)
* `stats.greater(4)` Should return 2 (6 and 9 are the only two values greater than 4)

# Conditions
Challenge conditions:
* You cannot import a library that solves it instantly
* The methods add(), less(), greater(), and between() should have
constant time O(1)
* The method build_stats() can be at most linear O(n)
* Apply the best practices you know
* Share a public repo with your project

#  How to setup and run

* Clone the repository
* We have two ways to run the flow.
    * First way: Run the app in a  Docker container with the next command lines in the terminal (only if you have Docker daemon):
        * `docker build -t skeleton_app .` 
We take as a template the docker file that is in the directory where we are, with this command the flow will be executed
        * `docker run --rm skeleton_app` the container will be deleted after the application ends.
    * Second way: run manually the app
        * Install `requirements.txt` in your env with `pip install --no-cache-dir --upgrade -r requirements.txt`
        * run `main.py`

