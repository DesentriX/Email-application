# Email-application
A web application that sends personalised emails to recipients when a csv file is uploaded. Using python, Html, CSS, Javascript and AWS Cloud services.


# Programming Languages and technlogies used
- HTML
- CSS
- Javascript
- Python
- Backend: Amazon Web services: Lambda, S3, SES, DynamoDB


# Features
- Users can upload csv files
- Sends out mass personalised emails based on the content in the csv file

# Process
 Setting up the AWS services (Lambda, SES, DynamoDB, S3) was straightforward but configuring them to work with my frontend application was challenging, I had to revise my lambda functions python logic several times. Ensure the S3 bucket had the correct policies as well as configure the Cross Origin resource sharing(CORS) setting, check that the DynamoDB databse had the correct keys and values. Then finally ensure the Simple Email Service(SES) had to right identities configured in order for the emails to be sent. Then creating the frontend web application using HTML, CSS, AND JAVASCRIPT. Implementing the frontend and backend communication posed some bugs which I troubleshooted and resolved. Using external tools such as Postman to test my API PUT request call to make sure that the uploaded file could be sent to the s3 bucket.    Through debugging and several test runs these challenges were overcome, leading to a functional application. 

# What I learned:
- Gained familiarity with AWS services like DynamoDB and SES

  

# Improvements:
- Implemented better error handling and logging in both frontend and backend.
- Made user interface simple to use.
- Improved knowledge on amazon S3 and Lambda 
- improved CORS error handling.
- Improved debugging skills for frontend-backend communication.
- improved front end and backend communication skills.
- Improved research skills
- Improved cloud familiarity


  # Running the Project:
- To run the project, clone the repository and ensure you have AWS credentials set up.
- Install any required dependencies and deploy the Lambda function.
- Update the frontend js code with the name of your bucket.
- Open the HTML file in a web browser to access the application.



# Demo Video
- To showcase the program
- https://streamable.com/w8pnmq
- your csv file template should look like this:  https://imgur.com/DJ2VKB1

  
  
