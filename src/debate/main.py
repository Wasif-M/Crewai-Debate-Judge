#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from debate.crew import Debate

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'School uniforms should not be mandatory in high schools.',
        'motion': 'Homework should be banned in schools.',
    }
    
    print("Inputs before kickoff:", inputs)
    try:
        results=Debate().crew().kickoff(inputs=inputs)
        print(results.raw)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        Debate().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")