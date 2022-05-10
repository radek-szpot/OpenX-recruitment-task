# Recruitment task
Performed by: Radosław Szpot

OpenX internship tasks. Reposiotry includes task1.py and task2.py files which are my solution to given problem.

## Task 1
Module task1.py contains function named length_longest_substring(s) created according to given instruction. 

After constructing function I designed PyTests in /test/test_task1.py, tests includes instruction examples, one character string as an input, string with numbers as an input and wrong type input which raises TypeError.

To run tests one should run pytest in command window in test path.

## Task 2
Module task2.py contains functions auth(), get(url), post(url), put(url), delete(url).
* auth() - returns a new auth token to use for access to the PUT and DELETE /booking
* get(url) - returns json_response which contains convereted response text, response which contains all data from request.get().
* post(url) - returns response which contains all data from requests.post().
* put(url) - returns response which contains all data from requests.put(). 
* delete(url) - returns response which contains all data from requests.delete(). 

After constructing functions I designed PyTests in /test/test_task2.py, tests contain cases for token creation, get booking ids, post booking, put/(update) booking, delete booking.
I also designed test case which checks if all data in id=1 is the same as in [example](https://restful-booker.herokuapp.com/apidoc/index.html#api-Booking-GetBooking) but base is being modified continually and in the time there was no entry with id=1.

To run tests one should run pytest in command window in test path.
