#!/usr/bin/env python
import sys
import warnings
import base64

from datetime import datetime

from gmail_new_thread_trigger.crew import GmailNewThreadTrigger

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information


def run():
    """
    Run the crew.
    """
    # Example email inputs - replace with actual email data from Gmail trigger
    # The content_base64 should contain the base64 encoded email content
    sample_content = "Hello,\n\nI hope this email finds you well. I wanted to follow up on our meeting yesterday regarding the project timeline. Could you please confirm if we're still on track for the March deadline?\n\nBest regards,\nJohn"
    sample_content_base64 = base64.b64encode(sample_content.encode('utf-8')).decode('utf-8')

    inputs = dict(
        subject='Follow-up on Project Timeline',
        to_email='recipient@example.com',
        from_email='john.doe@example.com',
        content_base64=sample_content_base64
    )

    try:
        GmailNewThreadTrigger().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    # Example email inputs for training
    sample_content = "Hello,\n\nI hope this email finds you well. I wanted to follow up on our meeting yesterday regarding the project timeline. Could you please confirm if we're still on track for the March deadline?\n\nBest regards,\nJohn"
    sample_content_base64 = base64.b64encode(sample_content.encode('utf-8')).decode('utf-8')

    inputs = dict(
        subject='Follow-up on Project Timeline',
        to_email='recipient@example.com',
        from_email='john.doe@example.com',
        content_base64=sample_content_base64
    )
    try:
        GmailNewThreadTrigger().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        GmailNewThreadTrigger().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    # Example email inputs for testing
    sample_content = "Hello,\n\nI hope this email finds you well. I wanted to follow up on our meeting yesterday regarding the project timeline. Could you please confirm if we're still on track for the March deadline?\n\nBest regards,\nJohn"
    sample_content_base64 = base64.b64encode(sample_content.encode('utf-8')).decode('utf-8')

    inputs = dict(
        subject='Follow-up on Project Timeline',
        to_email='recipient@example.com',
        from_email='john.doe@example.com',
        content_base64=sample_content_base64
    )

    try:
        GmailNewThreadTrigger().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
