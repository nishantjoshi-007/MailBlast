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
        """,
    },
    "Job Application": {
        "subject": "Application for ${job_title} Position at ${company}",
        "body": """   
        <p>Hello ${recipient},</p>
        <p>I hope this email finds you well. My name is ${user_name}, and I am writing to express my interest in the ${job_title} position at ${company}. With my background in ${major}, I am confident in my ability to contribute effectively to your team.</p>
        <p>I have a strong foundation in ${skills}, and I have worked on several projects that demonstrate my abilities. I have attached my resume for your review. I would greatly appreciate the opportunity to discuss how my background, skills, and certifications will be beneficial to your team.</p>
        <p>Thank you for considering my application. I look forward to hearing from you.</p>
        <p>Best regards,<br>${user_name}</p>
        """,
    },
    "Product Launch": {
        "subject": "Discover Our Latest ${product} - Special Offer Just for You!",
        "body": """   
        <p>Hello ${recipient},</p>
        <p>I hope you're doing well! My name is ${user_name}, and I'm excited to introduce you to our latest product, the ${product}. At ${company}, we believe in providing top-quality products that cater to your needs.</p>
        <p>The ${product} offers ${features}, making it the perfect choice for ${use_case}. As a valued customer, we're offering you an exclusive discount. Use the code ${discount_code} at checkout to enjoy a special price.</p>
        <p>If you have any questions or need more information, feel free to reach out. We're here to help!</p>
        <p>Best regards,<br>${user_name}<br>${company}</p>
        """,
    },
    "Event Invite": {
        "subject": "You're Invited! Join Us for ${event} on ${date}",
        "body": """   
        <p>Hello ${recipient},</p>
        <p>I hope you're having a great day! My name is ${user_name}, and I'm excited to invite you to our upcoming ${event} on ${date}. It's going to be a fantastic event filled with ${highlights}.</p>
        <p>Your presence would mean a lot to us. Please let us know if you can make it by responding to this email. Feel free to bring along any friends or colleagues who might be interested.</p>
        <p>Looking forward to seeing you there!</p>
        <p>Best,<br>${user_name}</p>
        """,
    },
    "NJIT CDS Special Use Only (HTML)": {
        "subject": "NJIT 2025 Recruitment Partner Awards Event - Congratulations",
        "body": """   
        <p>Dear ${Fname},</p><br />

        <p>I am excited to share that ${company_name} will be recognized as ${award_name} at our 2025 Recruitment Partner Awards Event.</p><br />

        <p>We hope that you will join us on-campus on <strong>Friday, May 2nd from 10am – 12pm</strong> to receive this recognition.</p><br />
                        
        <p>Best Regards,</p><br />

        <p>Patrick Young</p>
        <p>Interim Executive Director</p>
        <p>Director, Employer Relations & Outcomes</p>
        <p>Career Development Services</p>
        <p>New Jersey Institute of Technology</p>
        """,
    },
    "NJIT CDS Special Use Only (HTML)": {
        "subject": "NJIT 2025 Recruitment Partner Awards Event - Congratulations",
        "body": """   
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>NJIT 2025 Recruitment Partner Awards Event</title>
        </head>
        <body style="font-family: Arial, sans-serif; background-color: #f4f4f4; margin: 0; padding: 0;">

            <!-- Email container -->
            <table width="100%" border="0" cellspacing="0" cellpadding="0" style="background-color: #f4f4f4; padding: 20px 0;">
                <tr>
                    <td align="center">
                        <!-- Main email body -->
                        <table width="600" border="0" cellspacing="0" cellpadding="20" style="background-color: #ffffff; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">

                            <!-- Header -->
                            <tr>
                                <td style="background-color: #ffffff; text-align: center; padding: 0; border-top-left-radius: 8px; border-top-right-radius: 8px;">
                                    <img src="https://res.cloudinary.com/dhzkwhytv/image/upload/v1743095120/Awards_Banner_Email_dhsa8a.png" alt="NJIT Career Fair" style="width: 100%; max-width: 600px; height: auto; border-top-left-radius: 8px; border-top-right-radius: 8px;">
                                </td>
                            </tr>

                            <!-- Body content -->
                            <tr>
                                <td style="color: #333333; font-size: 16px; line-height: 1.6;">
                                    <p>Dear ${Fname},</p>
                                    
                                    <p>Each year, NJIT Career Development Services hosts an awards ceremony to honor our outstanding partners and contributors. These awards recognize the pivotal role these organizations play in providing career opportunities and high-impact experiential learning for students.</p>
                                    
                                    <p>I am excited to share that ${winner} will be recognized as ${award_name} at our 2025 Recruitment Partner Awards Event!</p>

                                    <p>We hope that you will join us on-campus on <strong>Friday, May 2nd from 10am – 12pm</strong> to receive this recognition.</p>

                                    <p><i><strong>Please fill out our RSVP form here:</strong></i><br />
                                        <p style="text-align: center;">
                                            <a href="https://www.njit.edu/careerservices/njit-recruitment-partner-awards-2025" style="display: inline-block; padding: 12px 20px; color: #ffffff; background-color: #0f4c81; text-decoration: none; border-radius: 4px; font-weight: bold; text-align: center;">NJIT 2025 Recruitment Partner Awards Event Invitation</a>
                                        </p><br />
                                    </p>
                            
                                    <p>Regards,<br />
                                    <strong>Patrick Young</strong><br /></p>
                                </td>
                            </tr>

                            <!-- Footer -->
                            <tr>
                                <td style="background-color: #d22630; color: #ffffff; padding: 20px; border-bottom-left-radius: 8px; border-bottom-right-radius: 8px;">
                                    <table width="100%" border="0" cellspacing="0" cellpadding="10">
                                        <tr>
                                            <!-- Left section -->
                                            <td width="50%" style="text-align: left; font-size: 14px;">
                                                <a href="https://www.njit.edu/careerservices" style="color: #ffffff; text-decoration: underline; font-weight: bold;">Visit Our Website</a>
                                            </td>

                                            <!-- Right section -->
                                            <td width="50%" style="text-align: right;">
                                                <a href="https://www.linkedin.com/company/njitcds" style="color: #ffffff; text-decoration: none; margin: 0 10px;">
                                                    <img src="https://raw.githubusercontent.com/nishantjoshi-007/MailBlast/main/static/linkedin.png" alt="LinkedIn" style="width: 24px; height: 24px; vertical-align: middle;">
                                                </a>
                                                <a href="https://www.instagram.com/njitcds/" style="color: #ffffff; text-decoration: none; margin: 0 10px;">
                                                    <img src="https://raw.githubusercontent.com/nishantjoshi-007/MailBlast/main/static/insta.png" alt="Instagram" style="width: 24px; height: 24px; vertical-align: middle;">
                                                </a>
                                                <a href="https://www.facebook.com/NJITCDS/" style="color: #ffffff; text-decoration: none; margin: 0 10px;">
                                                    <img src="https://raw.githubusercontent.com/nishantjoshi-007/MailBlast/main/static/fb.png" alt="Facebook" style="width: 24px; height: 24px; vertical-align: middle;">
                                                </a>
                                            </td>
                                        </tr>
                                    </table>

                                    <p style="margin: 0; text-align: center; font-size: 12px;">Career Development Services, Fenster Hall, Room 400</p>
                                    <p style="margin: 10px 0; text-align: center; font-size: 12px;">323 Dr. Martin Luther King Jr Blvd, Newark, NJ 07102</p>
                                    <p style="margin: 0; text-align: center; font-size: 12px;">&copy; 2025 New Jersey Institute of Technology</p>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
        </body>
        </html>
        """,
    },
}
