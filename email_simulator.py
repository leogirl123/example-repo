# --- Email Simulator using OOP in Python --- #

# --- Email Class --- #
class Email:
    def __init__(self, email_address, subject_line, email_content):
        """
        Create a new Email object with sender address, subject, and content.
        Email starts as unread (has_been_read = False).
        """
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    def mark_as_read(self):
        """Mark the email as read."""
        self.has_been_read = True


# --- Inbox List --- #
inbox = []  # Global list to store Email objects


# --- Functions --- #

def populate_inbox():
    """
    Create and add 3 sample Email objects to the inbox at startup.
    """
    email1 = Email("chloe@example.com", "Welcome to HyperionDev!", "Glad to have you on board.")
    email2 = Email("sky@example.com", "Great work on the bootcamp!", "You're doing a fantastic job.")
    email3 = Email("jack@example.com", "Your excellent marks!", "You've scored the highest this term.")
    inbox.extend([email1, email2, email3])


def list_emails():
    """
    Display all emails with their index number and subject line.
    """
    if not inbox:
        print("\nInbox is empty.")
    else:
        print("\n--- All Emails ---")
        for index, email in enumerate(inbox):
            print(f"{index}: {email.subject_line}")


def read_email(index):
    """
    Display full details of a selected email and mark it as read.
    Shows:
    - From (email_address)
    - Subject (subject_line)
    - Content (email_content)
    """
    if 0 <= index < len(inbox):
        email = inbox[index]
        print("\n--- Email Details ---")
        print(f"From: {email.email_address}")
        print(f"Subject: {email.subject_line}")
        print(f"Content: {email.email_content}")
        email.mark_as_read()
        print(f"\n✅ Email from {email.email_address} marked as read.\n")
    else:
        print("\nInvalid email number. Please try again.\n")


# --- Main Program --- #

# Preload inbox with emails at startup
populate_inbox()

# Menu loop
while True:
    print(
        """\nWould you like to:
1. Read an email
2. View unread emails
3. Quit application"""
    )
    user_choice = input("Please enter selection (1/2/3): ").strip()

    if user_choice == "1":
        # Option to read an email
        list_emails()
        if inbox:
            index_input = input("Please enter the number of the email you want to read: ").strip()
            if index_input.isdigit():
                read_email(int(index_input))
            else:
                print("\nInvalid input. Please enter a number.")
        else:
            print("Inbox is empty. Nothing to read.")

    elif user_choice == "2":
        # Option to view unread emails
        print("\n--- Unread Emails ---")
        if not inbox:
            print("Inbox is empty. No emails available.")
        else:
            unread_emails = [
                (index, email) for index, email in enumerate(inbox) if not email.has_been_read
            ]
            if unread_emails:
                for index, email in unread_emails:
                    print(f"{index}: {email.subject_line}")
            else:
                print("✅ All emails have been read!")

    elif user_choice == "3":
        # Exit the application
        print("Goodbye! Thank you for using the email simulator.")
        break

    else:
        print("Incorrect input. Please enter 1, 2, or 3.")