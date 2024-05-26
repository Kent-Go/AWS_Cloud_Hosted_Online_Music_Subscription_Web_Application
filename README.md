<h1>AWS Cloud Hosted Online Music Subscription Web Application</h1>
<h2>EC2, S3, DynamoDB, Lambda, API Gateway</h2>

## Overview
Cloud Computing course’s project built for music lovers to register profile, query and subscribe/unsubscribe music upon login. Tech stacks include Amazon EC2, S3, DynamoDB, Lambda and API Gateway for hosting and running the cloud based online music subscription web application. Individually developed using JavaScript, Python, HTML and CSS. Achieved “High Distinction” grade for the project.

## Tech Stack
**EC2:** Virtual machine to host Apache HTTP Server for running the web application online

**S3:** Scalable object storage and hosting for artist images

**DynamoDB**: NoSQL database service for storing and querying unstructured login, music, and subscribed music data</h3>

**Lambda:**: Event-based severless Python (Boto3) functions for perform CRUD to database

**API Gateway:** Map RESTful API HTTP methods (GET and POST) to Lambda

## Features
1. **Register Page:** allow users to sign up for an account
2. **Login Page:** allow users to sign in to their account
3. **Main Page (For logged in users):**
    <ol type="a">
        <li><strong>Subscribed Music Section</strong></li>
        <ul>
            <li>display all subscribed music's info: title, artist name, published year and artist imagel</li>
            <li>remove music from the list of subscribed music</li>
        </ul>
        <li><strong>Query Music Section</strong></li>
        <ul>
            <li>allow users to search for a particular music based on any/all info (title, published year and artitst)</li>
            <li>display relevant music's info based on the search</li>
            <li>allow users to subscribe to music</li>
        </ul>
        <li><strong>Logout</strong></li>
        <ul>
            <li>allow users to logout and redirect to login page</li>
        </ul>
    </ol>
