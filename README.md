# cis457-project2

Jack Wolak
Matteo Ciavaglia
Andrew Slayton

Project 2 Prospectus

Project Area Description - (Handling Ad Fraud and artificial traffic)

Ad fraud and artificial traffic pose significant challenges to the digital advertising ecosystem. As
online advertising continues to grow, so does the sophistication and prevalence of fraudulent
activities designed to deceive advertisers and inflate ad metrics. Effectively addressing ad fraud
and artificial traffic is crucial for maintaining trust and transparency in the digital advertising
industry.


Description of Click Hijacking - (Specific Problem)

Click Hijacking/Clickjacking: When a user clicks on one ad they see and it redirects them to a
different website not related to the one they clicked. In short, the website they actually go to
steals the click and the ad networks pay them instead of the seen ad.

Current Solutions
Some existing solutions to this problem include:
Click Redirection Validation, implementing click redirection validation mechanisms to ensure that
when a user clicks on an ad, they are directed to the intended destination URL associated with
the ad. This involves verifying the redirect URL against a whitelist of approved destinations
before processing the click.
URL Monitoring and Blacklisting, regularly monitoring click redirection URLs and maintaining a
blacklist of known fraudulent or unauthorized destinations. Ad networks can proactively block
clicks that are redirected to blacklisted URLs, preventing users from being diverted to malicious
or unrelated websites.
Referrer Verification, verifying the referrer information provided with the click request to ensure
that it matches the expected source of the click. Discrepancies in referrer data may indicate click
hijacking attempts and can trigger additional validation checks or block the click altogether.


Proposal for Enhanced Solution
We chose Click Redirection Validation to improve upon, one weakness that some ad companies
use dynamic URLs. Your whitelist on the website will have a hard time checking against these
URLs as they are randomly generated each click.
Our proposed solution is being able to check the dynamic URLs by converting the URL into a
string and checking the part of the URL that doesn't change. Hopefully being able to increase
the effectiveness of the whitelist.


Timeline and Expectations
Breakdown of tasks and responsibilities: ***Each group member will participate in each task.
Research - Research more in depth solutions for checking dynamic URLs and possible coding
techniques to get this done.
Development - Implementing the dynamic URL solutions to improve clickjacking on a given
website
Testing - Test the solution and find any bugs in the current implementation.
Debugging - Fix the bug found in the testing phase to polish up the project.
Documentation - Readable code to help future developers to improve or redesign our solution.
Timeline for each phase of implementation: *** Assuming it is due the week before exams. In 5
weeks.


Week 1 - Research
Week 2 - Development/Documentation
Week 3 - Development/Documentation
Week 4 - Development and Testing/Debugging
Week 5 - Testing/Debugging
