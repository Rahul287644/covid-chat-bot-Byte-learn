# covid chat bot using Rasa
Covid -19 chatbot that has ability to provide information about covid -19

### What all questions can this chat bot answer?

- Information about covid
- Precautions or safety measures
- Vaccines
- Covid spread
- Covid symptoms
- What time is it
- Cases and deaths in india 
- Cases and deaths in india on a specific date
- Cases and deaths in a state
- Cases and deaths in a state on a specific date


### How to run the project
I used duckling to extract time entity from the query. Run below code first in the terminal.
``` 
docker run -p 8000:8000 rasa/rasa_duckling
```  


### Known Bugs
- State specific queries work properly with states telangana and delhi due to improper training data




