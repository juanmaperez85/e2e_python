# Packlink QA Automation Code Challenge

Instructions
------------
1. Fork and Clone this repo
2. Work on the requirements
3. Create a file `instructions.md` for the instructions needed to run the project
4. Do a PR with your code and any other needed information
5. Send an email notifying us

Introduction
------------
Prepare a working, suitable for automation test suite including instructions on how to run it, with the following Gherkin style scenarios as base.
Extending the use cases is a plus.

Feature: Register
-----------------

| Scenario | Register a user |
|----------|----------|
| GIVEN    | an internet user |
| WHEN     | going to https://pro.packlink.es/registro |
| THEN     | it will see the registration form with required fields |


| Scenario | Log in for a registered user |
|----------|----------|
| GIVEN    | an internet user |
| WHEN     | registered in https://pro.packlink.es WITH credentials qacandidate+{yourname}@packlink.es and random password |
| THEN     | it will land into the platform dashboard |

Feature: Search
---------------

| Scenario | Search services |
|----------|----------|
| GIVEN    | a registered client |
| WHEN     | performing a search with the following information: Madrid -> Madrid. One parcel, 1 kg, 10 cm x 10 cm x 10 cm. |
| THEN     | it will select the first service of the list |

Feature: Draft Shipments
------------------------
| Scenario | Save a shipment draft |
|----------|----------|
| GIVEN    | a registered client |
| WHEN     | a service has been selected |
| THEN     | it will save the shipment as a draft |
| AND      | it will appear in the shipment list |

Remarks
-------

* {yourname} is a placeholder for your name and surname, ASCII chars, no spaces. You can extend this to allow multiple runs.
* The description of the exercise is deliberately loose in order to evaluate your analytical skills.
* Clarity, readability and structure of the code are also part of the evaluation criteria.
