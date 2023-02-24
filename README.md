# be-green
Tree Hacks 2023 Submission

## What is Eat Fresh?
Eat Fresh is a web-app that helps users determine the carbon footprint of their food! Users upload a picture via a url on our website, and our machine learning algorithm classifies the image based on the different foods pictorially available. Then, based on those results we determine the carbon footprint of the highest emitting food and return the result to the user. This way, users can gain some intuition on their carbon footprint over time as they eat different foods. The goal of Eat Fresh is to help users become more ethical consumers. It is important, now more than ever, to lead our lives with an awareness of how our actions affect our environment. Users can also donate money to different clean agriculture organizations. All images are uploaded to our central database as well so we can improve our classifier model and analyze the food-trends of our users.

## Tools/ Strategies 
Our application was built using Flask, a micro web framework. We used Python for the back-end and our auxiliary data analysis, and HTML/CSS/JS tech-stack for our front-end. Our machine learning classifier was built off of Clarafai's public food classifier. We used the checkbook REST API to perform all our payments and the Estuary API (a a decentralized data storage built on blockchain-based cooperative digital storage) to store all our user's images to a central data source. We used vercel to host our website.


