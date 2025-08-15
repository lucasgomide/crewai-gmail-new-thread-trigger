#!/usr/bin/env python
import sys
import warnings

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
    # Example Gmail message inputs - replace with actual message ID and recipient email from Gmail trigger
    # The message_id should be the Gmail message ID to retrieve
    inputs = {
        'message_id': "198adefd9068d7bc",  # Example Gmail message ID
        'to_email': 'lucas@crewai.com'
    }

    try:
        GmailNewThreadTrigger().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    # Example Gmail message inputs for training
    inputs = {
        'message_id': "198adefd9068d7bc",  # Example Gmail message ID
        'to_email': 'lucas@crewai.com'
    }
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
    # Example Gmail message inputs for testing
    inputs = {
        'message_id': "198adefd9068d7bc",  # Example Gmail message ID
        'to_email': 'lucas@crewai.com'
    }

    try:
        GmailNewThreadTrigger().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
