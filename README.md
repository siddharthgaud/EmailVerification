# EmailVerification
This project is a Django-based authentication system that includes user signup, email verification, login, and restricted access to an "About" page for authenticated users. The system ensures that users can only log in after verifying their email via a secure activation link.

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'Email host mail ID'   # Enter Email ID
EMAIL_HOST_PASSWORD = 'Email Host Password'   # Fenerate APP Password


Steps to generate APP Password:-
Under "Signing in to Google," you will see "App passwords." Click on it.
You may need to sign in again.
In the "Select app" dropdown, choose the app you want to generate a password for (e.g., "Mail").
In the "Select device" dropdown, choose the device you are using (or select "Other" and name it).
Click on "Generate."
A 16-character app password will be displayed. Copy this password.
