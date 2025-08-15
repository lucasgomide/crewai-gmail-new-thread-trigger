# Gmail Email Summarization Crew

Welcome to the Gmail Email Summarization Crew project, powered by [crewAI](https://crewai.com). This AI crew automatically analyzes and summarizes received emails from Gmail, providing clear, actionable insights from email content including sender information, key points, and action items.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/gmail_new_thread_trigger/config/agents.yaml` to define your agents
- Modify `src/gmail_new_thread_trigger/config/tasks.yaml` to define your tasks
- Modify `src/gmail_new_thread_trigger/crew.py` to add your own logic, tools and specific args
- Modify `src/gmail_new_thread_trigger/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the gmail-new-thread-trigger Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will create an `email_summary.md` file with a comprehensive summary of the analyzed email.

## Email Input Format

The crew expects the following inputs:
- `subject`: Email subject line
- `to_email`: Recipient email address
- `from_email`: Sender email address (included prominently in the summary)
- `content_base64`: Base64 encoded email content

## Understanding Your Crew

The Gmail Email Summarization Crew is composed of two specialized AI agents:

1. **Email Analyzer**: Analyzes email content to extract key information, action items, and assess tone/urgency
2. **Email Summarizer**: Creates clear, structured summaries including sender information, key points, and action items

These agents collaborate sequentially to provide comprehensive email analysis and summarization.

## Support

For support, questions, or feedback regarding the GmailNewThreadTrigger Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
