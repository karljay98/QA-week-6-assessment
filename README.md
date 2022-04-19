# QA-week-6-assessment

# My flask shoe collection application

## Requirements

The requirements for this project can be summarised as the following:
"To develop a Flask application which incorporates CRUD fucntionality with utilisation of supporting tools, methodologies and technologies that encapsulate the core modules covered in training."

## Specific requirements

These are the requirements needed along with what is mentioned above:
* A Kanban board (Trello)
* A front end web design (HTML)
* Testing using pytest
* A python functional application that follows best practices and design principles
* A relational database using MySQL that consists of at least two tables
* The use of a version control system (Git)
* Clear documentation of the design phase, application architecture and risk assessment

### My design process

To design an application that adhires to the brief I opted for a simple library-concept application.

* To satisfy the Create statement of CRUD I provided a form to create an owner for the library
 * * *first name*
 * * *last name*
 * * *description*

* To satify the Read functionality of CRUD I updated the home page whenever a new owner was added. The information displayed included:
 * * *id*
 * * *first name*
 * * *last name*
 * * *description*

* To satisfy the Delete functionality of CRUD, a button was provided whereby an owner could delete their library.

## Database Architecture

![owner_erd_2](https://user-images.githubusercontent.com/71146682/164019482-877d3cc2-b864-4e11-ba48-ae56883845e6.jpg)

The ERD above shows the relationship between owners and shoes. With the foreignkey being owner_id which is used to link the tables together. The relationship between the tables is a one-many. One owner can have many shoes in their collection.

## Project Tracking

To track my progress a Trello Kanban board was used. The full board can be found here https://trello.com/invite/b/mD42Vby2/c08649c5bf7b29baba52c0f979b85d3f/owner

The purpose of this board is to track the project from start to end and document all the decisions and requirements as the project progressed. Each card in the Kanban board is associated with a particular element of the project:

*  User stories:
  * These are the requirements but from the user perspective and structured by stating what the action is and who is performing the action.
*  Project brief:
  * This is a list of all the requirements needed to complete the brief specification and produce the minimal viable product.
*  To be completed:
  * This is a list of all the tasks which were not completed and may still be in th eplanning phase.
*  In progress: 
  * This card details what tasks and currently being worked on to produce the MVP.
*  Done:
  * These are all the tasks that have been completed

## Risk Assessment
Risk assessment can be found here
[RISK assessment.docx](https://github.com/karljay98/QA-week-6-assessment/files/8514314/RISK.assessment.docx)

## Testing

For testing pytest was used and a coverage report was produced

![coverage](https://user-images.githubusercontent.com/71146682/164040482-805dfbfe-86e0-430e-a9cf-95976ecfe73b.jpg)




