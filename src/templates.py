# # predefined templates

# PREDEFINED_TEMPLATES = {
#     "Referral Request": {
#         "subject": "Referral Request for ${job_title} Position at ${company}",
#         "body": """   
# Hello ${recipient},

# I hope this message finds you well. My name is ${user_name}. I am currently an ${education_level} student majoring in ${major} with a graduation date in ${graduation_date}. I am excited about the ${job_title} position at ${company} and believe that my background and skills make me a strong candidate.

# I have completed several projects that demonstrate my proficiency in ${skills}, and I have practical experience in ${related_experiences}. Additionally, I have worked on projects related to ${additional_relevant_projects}.

# I understand that ${company} values referrals, and I would greatly appreciate it if you could refer me for this role. I have attached my resume for your review. If you need any additional information or would like to discuss further, please let me know.

# Thank you for your assistance!

# Best regards,
# ${user_name}
#         """
#     },
#     "Job Application": {
#         "subject": "Application for ${job_title} Position at ${company}",
#         "body": """   
# Hello ${recipient},

# I hope this email finds you well. My name is ${user_name}, and I am writing to express my interest in the ${job_title} position at ${company}. With my background in ${major}, I am confident in my ability to contribute effectively to your team.

# I have a strong foundation in ${skills}, and I have worked on several projects that demonstrate my abilities. I have attached my resume for your review. I would greatly appreciate the opportunity to discuss how my background, skills, and certifications will be beneficial to your team.

# Thank you for considering my application. I look forward to hearing from you.

# Best regards,
# ${user_name}
#         """
#     },
#     "Product Launch": {
#         "subject": "Discover Our Latest ${product} - Special Offer Just for You!",
#         "body": """   
# Hello ${recipient},

# I hope you're doing well! My name is ${user_name}, and I'm excited to introduce you to our latest product, the ${product}. At ${company}, we believe in providing top-quality products that cater to your needs.

# The ${product} offers ${features}, making it the perfect choice for ${use_case}. As a valued customer, we're offering you an exclusive discount. Use the code ${discount_code} at checkout to enjoy a special price.

# If you have any questions or need more information, feel free to reach out. We're here to help!

# Best regards,
# ${user_name}
# ${company}
#         """
#     },
#     "Event Invite": {
#         "subject": "You're Invited! Join Us for ${event} on ${date}",
#         "body": """   
# Hello ${recipient},

# I hope you're having a great day! My name is ${user_name}, and I'm excited to invite you to our upcoming ${event} on ${date}. It's going to be a fantastic event filled with ${highlights}.

# Your presence would mean a lot to us. Please let us know if you can make it by responding to this email. Feel free to bring along any friends or colleagues who might be interested.

# Looking forward to seeing you there!

# Best,
# ${user_name}
#         """
#     },
# }


PREDEFINED_TEMPLATES = {
    "Referral Request": {
        "subject": "Referral Request for ${job_title} Position at ${company}",
        "body": """   
        <p>Hello ${recipient},</p>
        <p>I hope this message finds you well. My name is ${user_name}. I am currently an ${education_level} student majoring in ${major} with a graduation date in ${graduation_date}. I am excited about the ${job_title} position at ${company} and believe that my background and skills make me a strong candidate.</p>
        <p>I have completed several projects that demonstrate my proficiency in ${skills}, and I have practical experience in ${related_experiences}. Additionally, I have worked on projects related to ${additional_relevant_projects}.</p>
        <p>I understand that ${company} values referrals, and I would greatly appreciate it if you could refer me for this role. I have attached my resume for your review. If you need any additional information or would like to discuss further, please let me know.</p>
        <p>Thank you for your assistance!</p>
        <p>Best regards,<br>${user_name}</p>
        """
    },
    "Job Application": {
        "subject": "Application for ${job_title} Position at ${company}",
        "body": """   
        <p>Hello ${recipient},</p>
        <p>I hope this email finds you well. My name is ${user_name}, and I am writing to express my interest in the ${job_title} position at ${company}. With my background in ${major}, I am confident in my ability to contribute effectively to your team.</p>
        <p>I have a strong foundation in ${skills}, and I have worked on several projects that demonstrate my abilities. I have attached my resume for your review. I would greatly appreciate the opportunity to discuss how my background, skills, and certifications will be beneficial to your team.</p>
        <p>Thank you for considering my application. I look forward to hearing from you.</p>
        <p>Best regards,<br>${user_name}</p>
        """
    },
    "Product Launch": {
        "subject": "Discover Our Latest ${product} - Special Offer Just for You!",
        "body": """   
        <p>Hello ${recipient},</p>
        <p>I hope you're doing well! My name is ${user_name}, and I'm excited to introduce you to our latest product, the ${product}. At ${company}, we believe in providing top-quality products that cater to your needs.</p>
        <p>The ${product} offers ${features}, making it the perfect choice for ${use_case}. As a valued customer, we're offering you an exclusive discount. Use the code ${discount_code} at checkout to enjoy a special price.</p>
        <p>If you have any questions or need more information, feel free to reach out. We're here to help!</p>
        <p>Best regards,<br>${user_name}<br>${company}</p>
        """
    },
    "Event Invite": {
        "subject": "You're Invited! Join Us for ${event} on ${date}",
        "body": """   
        <p>Hello ${recipient},</p>
        <p>I hope you're having a great day! My name is ${user_name}, and I'm excited to invite you to our upcoming ${event} on ${date}. It's going to be a fantastic event filled with ${highlights}.</p>
        <p>Your presence would mean a lot to us. Please let us know if you can make it by responding to this email. Feel free to bring along any friends or colleagues who might be interested.</p>
        <p>Looking forward to seeing you there!</p>
        <p>Best,<br>${user_name}</p>
        """
    },
        "CDS Special": {
        "subject": "NJIT Spring 2025 Career Fair - Last Chance to Register",
        "body": """   
            Hello ${Fname},

            Career Development Services at NJIT invites you to attend our <a href="https://www.njit.edu/careerservices/njit-career-fairs">Spring 2025 Career Fair</a> to be held on <strong>Tuesday, February 18th from 11:30 AM - 4:00 PM.</strong>

            Attend to connect face-to-face with top STEM talent from <a href="https://www.njit.edu/">NJIT</a>, one of the nation's leading public polytechnic universities, designated as an <a href="https://news.njit.edu/njit-reaffirmed-elite-research-university-retains-r1-classification">R1 Research University</a> and <a href="https://news.njit.edu/njit-earns-hispanic-serving-status-us-dept-education">Minority-Serving Institution</a>, and recently named <a href="https://news.njit.edu/wall-street-journalcollege-pulse-ranks-njit-no-2-public-university-us">Number 2 Public University in the US</a> by the Wall Street Journal.

            <strong>We anticipate a sold out event, so act fast!</strong>
            
            <a href="app.joinhandshake.com/career_fairs/ecf839f5-f02b-4e95-ae9f-155c79f9f8db/employer_preview">Register for NJIT Spring 2025 Career Fair</a>
            
            We look forward to sharing the full-time, co-op, and intern opportunities of your organization with the talented and diverse students of NJIT in Engineering, Computing, Architecture, Design, Business, Science, and Math disciplines. Please be in touch if you have any questions about this event or to discuss your Spring 2025 recruiting strategy at NJIT.

            Regards,

            Patrick Young
            Interim Executive Director
            Director, Employer Relations & Outcomes
            Career Development Services
            New Jersey Institute of Technology
        """
    },
}