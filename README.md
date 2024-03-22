## Flask Application Design for TOEFL Preparation App

### HTML Files

- **home.html**: The main page of the application. It will display a banner or title for the TOEFL preparation app.
- **practice_tests.html**: A page that provides access to practice tests. It will include links to various practice tests.
- **vocabulary_trainer.html**: A page that provides vocabulary training exercises. It will contain input fields for user interaction and display vocabulary words with their definitions.
- **grammar_exercises.html**: A page that provides grammar exercises. It will include interactive elements for users to practice grammar concepts.
- **progress_tracker.html**: A page that allows users to track their progress in preparing for the TOEFL. It will display charts and statistics related to the user's performance in practice tests and exercises.

### Routes

- **"/"**: The main route that renders the home.html page.
- **"/practice_tests"**: The route that renders the practice_tests.html page.
- **"/vocabulary_trainer"**: The route that renders the vocabulary_trainer.html page.
- **"/grammar_exercises"**: The route that renders the grammar_exercises.html page.
- **"/progress_tracker"**: The route that renders the progress_tracker.html page.
- **"/feedback"**: A route for collecting feedback from users. It will render a simple form where users can provide their feedback.
- **"/api/practice_tests"**: An API endpoint that provides access to practice tests in JSON format.
- **"/api/vocabulary"**: An API endpoint that provides a list of vocabulary words with their definitions in JSON format.
- **"/api/grammar"**: An API endpoint that provides a list of grammar exercises in JSON format.
- **"/api/progress"**: An API endpoint that allows users to track their progress and retrieve their performance data in JSON format.