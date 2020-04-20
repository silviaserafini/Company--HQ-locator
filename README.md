# Company-HQ-locator

<img style="float: left;" src="INPUT/download.jpg">

The goal of the project is to find the  perfect location for the new offices of a young company in the `GAMING industry`. 
The company will has the following scheme:

- 20 Designers
- 5 UI/UX Engineers
- 10 Frontend Developers
- 15 Data Engineers
- 5 Backend Developers
- 20 Account Managers
- 1 Maintenance guy that loves basketball
- 10 Executives
- 1 CEO/President


The first goal is to place the **new company offices** in the best place for the company to grow. And  accomplish the most of the following requirements: 

    - Designers like to go to design talks and share knowledge. There must be some nearby companies that also do design.
    - 30% of the company have at least 1 child.
    - Developers like to be near successful tech startups that have raised at least 1 Million dollars.
    - Executives like Starbucks A LOT. Ensure there's a starbucks not to far.
    - Account managers need to travel a lot.
    - All people in the company have between 25 and 40 years, give them some place to go to party.
    - Nobody in the company likes to have companies with more than 10 years in a radius of 2 KM.
    - The CEO is Vegan

You can see read my approach to the problem and my solution in the file `Geolocalization`

In order to find the location I tried 2 approaches:

    1-target coordinates as the weighted distance from the baricentres of the differnts categories locations of interest
    2-a random location tester

I found a solution and reverse geocoded the coordinates.

In the file `ProjectW4` I run a deep analysis of the crunchbase dataset using MongoDB.

I've used some APIs to fetch informations about the Starbucks, Airports, Recent Companies, Vegan restaurants, 
parties and events in the city I choose and I build some dataframes with the queries results always insluding geospatial coordinates.

Taking advantage of the fact that MongoDB allows me to create Collections with different documents' categories inside, I created a dataset including all the different categories called "geopro". This will help me in my approach 2 solution.

