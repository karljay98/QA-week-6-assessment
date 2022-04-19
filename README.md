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

![ERD]: (https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Owner_ERD.drawio#R7Vtbc9o8EP01fmzGF0ySRyDQfFNoMyRtHzuKLWxNjOSRxS2%2F%2FpNsCeMLIBdCUsgMk9hreS3tOXssVsJwetPlVwricER8GBm26S8N586wbatl24b4mP4qs1zftjJDQJEvG%2BWGR%2FQKpdGU1hnyYVJoyAiJGIqLRo9gDD1WsAFKyaLYbEKi4lNjEMCK4dEDUdX6G%2FkszKw3rpnb7yEKQvVky5RXpkA1loYkBD5ZFExwyQYEM9nFB0inAEPM%2BJURoC%2BQGm4%2FZEyMtGPYA%2F6ZiNZXASFBBEGMkiuPTLnZS3iTwQRMUSTCvOGoKx3xxzl9w%2BlRQlh2NF32YCSwUjBkfRpsubqOAxV%2BNW7ofZmvhi8mw%2FcL5xcbjYKH6%2BcvlmTDHEQzGWAZHLZSEYc%2BB0Ce8mchthrDCDBEcD%2B%2F0oXY7wh4eaP%2B%2BBVS8kRGAPPRdxMGKMuvESybDxDvn3NnqSby3OTn1bHJ4SZkRj24Y0COpCSgAWS7Bn4tEfcLdJOh%2BwrJFDK64g0WOcnWVAo3CaaMNA3KvEhTIKkUrB2un%2FFAUMosmZkt5UfmpXVjFl1kQ5d3beJcdtQuOrJNt%2Bgoi03FET%2FYGHhuSmnUgFJVRv1YYEiTCq94%2FsXikIHnlEEpCaTgOIIFXEIYQPxeyRKPRBGIE5Q2zywhivwhWJEZU47UWXeCltAfZ3oj2nL%2BDbmzRFJMZK5itbgMIhRgfuxxyokndilMeF%2BGIGGyxVZSziFlcLmTRQobtwSyEp4NltluHctuze2EKiDYFC5nvwAooPjQGQLRmMs6wEGKWRESEVefkvhJZZ8wxIJokPbnMBPWNPg81XskIgJZnAlC2iwdnNvlHz7cnnnlGi7vQI%2BfW%2Fk5%2F4jmlPUIThgFKIUDcqAWUIDVZSSWz4ngRHWDymCK42fCGNfpbbDupPV%2BrCW2jia0zlsh26og%2B%2FCtCbaEj3USpaodIt%2BHOEtJ8VYHOd41UNbGfx3zMhjlRNTEw9HGYwMAp2H8pbM8Ko29gYhzHwMGu2SG%2FeQtBNetZnDPNjriJn5n%2Bmr4%2FuNJ%2FP05HH5AAijlzdp2kxh4CAfD7M72KRiy3J6x9lEZo%2BXuBJRpX7Lo108wjyP67fcW%2FeuDkD1RxmtGv60d%2FXOX%2BJsKqhNEE%2FYHg6no8K%2FOuHffGf%2FzQn90XpyzsM9%2FWvi1vVrc%2BePo%2B%2FhlFMy%2BkRqiXKSwV6ihq%2FVbhf1WU9jbRxD2WmRv%2Fx1h3xP97cRtLOy7ot1c2MveTpCvqqp6Gcp%2BRGI0VPa%2FJ4qWuxNMAQ7L%2F7NR9uNP2S1XU9pbbzVnrxGBD5jjmvG%2F1Y7%2FHjXeFe7m2l72doKMtawKrHcw8SiKxdrJ2Yn7EZnRUNz%2Fnila7k5BlWoV%2FjEk8HPNxKiumbR010xs880Eu1pav6CXcYMSrKVfg%2F0oqyZWtZx%2BTssma%2Bp%2BFtWsahX80pdMGrDjnEtrO3eMXKboN%2FgG0Fz0333VxDqsbvqxvoGtifop8Va1aiLm1RvVNf73kr6DNeDGxQm86sanwB9d4HVXT95M4O1qLeYDZrlm%2FNdE%2FRR4BeMGrokQeFGG4Ob%2FzmAqf3xSnLOy16%2ByaWT%2Fxv51iWPIpmp%2FOhVdg34hTUs7x2uqXDvTsU7%2BlO3QreRq67iaXtulkGtvJS85csul0eNtJa%2FHrW5zchtMeX518XMi%2FqXZzl%2B9fESGZkWdpwcrwstfneQFltK4JrNLuSpSDXkg6kjzlMtEKh2LEDH4yDNZPHFBQbyFQnvWQ%2FfURbeBc0g%2BH7RFobYsWoSLiJ8C%2FNErs5wrTtfvjlO1xDmoljgPD%2F96WeCdAXD3A9B0crQl%2Fvw0%2F0FXpoL5r%2FCc%2Fv8%3D)


