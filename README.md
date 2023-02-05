# MedBox

## What it does
MedBox is a health and prescription assistance webapp, which allows the user to choose and order a drug based on their symptoms, search and order a specific drug, and pick-up and refill their prescription.  

## How we built it
The backend utilizes Python scripts and the ApiMedic API to take symptoms as input and internally determine the diagnosis. We then use a dictionary that maps each diagnosis to the corresponding treatment. This two-step process enables the user to enter their symptoms and see the recommended drugs to help them. The frontend utilizes HTML, CSS, and JS to construct the whole website, which consists of 9 web pages. 

## Challenges we ran into
In the backend, there was no direct way to map symptoms to treatments via an API. Also, most APIs required approval before we could get the access key. So, we had to break the process into two parts: symptoms to diagnosis, and diagnosis to treatments. Since there was no API that mapped diagnoses to treatments available, we used a dictionary to solve that issue. Also, we developed the entire website from scratch, learning every step of the way. We learned how to operate Git, GitHub, HTML, CSS, and JS from basic tutorials and asking mentors for their help. Also, it was quite difficult to make a button, but once we figured that out, we could reap the benefits as we used buttons in many places. 

## Accomplishments that we're proud of
We are very proud of creating MedBox with many of the features that we originally envisioned. We also think our website aesthetics resemble the medical-based theme. In addition, we are also proud of the backend that executes a complex process from symptoms to diagnosis to treatments.  

## What we learned
We learned how to interface Python with APIs, how to use APIs and process JSON files, how to build the entire website using HTML, CSS, and JS, and how to connect the frontend to the backend via Flask Python server and HTTP requests.  

## What's next for MedBox
