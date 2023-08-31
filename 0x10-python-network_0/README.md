# Python - Network #0

## Resources:
`Bash`
`Python`
`Scripting`
`Back-end`
`API`
`Http Verbs`



| Questions | Answers |
| --- | --- |
| What is URL | known for it's name `uniform resource identifier`, it specifies the location of a web resource on a computer |
| What is Http | Hyper text transfer protocol, an application protocol used in the internet for the web |
| How to read a Url | `https://www.isaacajibola.tech` protocol name is `https` subdomain: `www` domain: `isaacajibola.tech` and `https://www.isaacajibola.tech/login/login.html` resource path: `/login/login.html` |
| The scheme for a HTTP URL | This is the part that indicates the protocol being used, usually `http` |
| What a domain name is | This is the part after the www or double slash |
| What a sub-domain is | This is the part before the sub domain usually `www` |
| How to define a port number in a URL | To define a port number in a url you can include it after the domain name or ip address it would look like this `www.isaacajiboola.tech:8080/login` `8080` is the port number |
| What a query string is | this is a string containing the passed data to the web server in the url it looks like this https://`www.isaacajibola.tech/search?query=programming&category=tech` |
| What an HTTP request is | This is a message sent by a client to a web server to request a specific resource. |
| What an HTTP response is | This is the response/message sent by the server to the client in response to a http request |
| What HTTP headers are | Headers are additional information sent along with an http response. |
| What the HTTP message body is | This is the optional data part of an http request or response |
| What an HTTP request method is | These are methods that specifies the action to be performed on a resource |
| What an HTTP response status code is | These are usually 3 digit codes sent by the server to indicate the outcome of the requested operation |
| What an HTTP Cookie is | This is a small piece of data that a web server sends to user's web browser |
| How to make a request with cURL | Command line URL is a command-line tool and library for making https requests. |

# TASKS

## 0-body_size.sh:

Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

The size must be displayed in bytes

You have to use curl

## 1-body.sh:

Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response

Display only body of a 200 status code response

You have to use curl

## 2-delete.sh:

Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response

You have to use curl

## 3-methods.sh:

Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.

You have to use curl

## 4-header.sh:

Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response

A header variable X-School-User-Id must be sent with the value 98

You have to use curl

## 5-post_params.sh:

Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response

A variable email must be sent with the value test@gmail.com
A variable subject must be sent with the value I will always be here for PLD

You have to use curl

## 6-peak.py, 6-peak.txt:

- [X] Technical interview preparation:

- You are not allowed to google anything
- Whiteboard first

- [X] Write a function that finds a peak in a list of unsorted integers.

- Prototype: def find_peak(list_of_integers):
- You are not allowed to import any module
- Your algorithm must have the lowest complexity (hint: you don’t need to go through all numbers to find a peak)
- 6-peak.py must contain the function
- 6-peak.txt must contain the complexity of your algorithm: O(log(n)), O(n), O(nlog(n)) or O(n2)
- Note: there may be more than one peak in the list

# ADVANCED TASKS
