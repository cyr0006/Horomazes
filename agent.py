"""
AI Carreer Agent
A command-line tool to help you manage and advance your career using AI.

By Aryan Cyrus

Commands:
- `init`: Initialise the database.
- `query <message>`: Ask the agent anything.
- `log-event <description> [--type <type>] [--impact <impact>]
- `log-skill <name> [--level <level>] [--notes <notes>]`
- `log-goal <goal> [--by <target_date>]`
- `log-job <company> <role>`
- `chat`: Start an interactive conversation with the agent.
- Exit the chat with 'exit'
"""
#Imports
import anthropic
import click
from dotenv import load_dotenv
import db
load_dotenv()
client = anthropic.Anthropic()

#Load AI instructions
def load_system_prompt():
    with open("prompts/system.md", "r") as f:
        return f.read()
    
#Load context from file for who I am, what I do, and what I want
def load_personal_context():
    try:
        with open("prompts/context.md", "r") as f:
            return f.read()
    except FileNotFoundError:
        return ""

#Main function to ask the agent a question and get a response
def ask(user_message):
    system = load_system_prompt()
    db_context = db.get_context_block()
    personal_context = load_personal_context()
   
    #Context window consists of personal context + database context + user message, separated by --- to help the model understand the structure
    full_message = f"{personal_context}\n\n{db_context}\n\n---\n\n{user_message}"
    
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1000,
        system=system,
        messages=[
            {"role": "user", "content": full_message}
        ]
    )

    return response.content[0].text

# command line interface
@click.group()
def cli():
    """Your personal career agent."""
    pass

# bot initialisation and commands
@cli.command()
def init():
    """Initialise the database."""
    db.init_db()
    click.echo("Database initialised.")

# No chat history or context query - just a one-off question to the agent, useful for quick queries without needing to start a full conversation
@cli.command()
@click.argument("message")
def query(message):
    """Ask the agent anything."""
    click.echo("\nThinking...\n")
    response = ask(message)
    click.echo(response)

# Log an event
@cli.command()
@click.argument("description")
@click.option("--type", default="other", help="achievement/feedback/project/promotion/other")
@click.option("--impact", default=None)
def log_event(description, type, impact):
    """Log a career event."""
    db.log_event(description, type, impact)
    click.echo(f"Event logged: {description}")

# Log a skill
@cli.command()
@click.argument("name")
@click.option("--level", default="intermediate", help="beginner/intermediate/advanced/expert")
@click.option("--notes", default=None)
def log_skill(name, level, notes):
    """Log or update a skill."""
    db.log_skill(name, level, notes=notes)
    click.echo(f"Skill logged: {name} ({level})")

# Log a goal
@cli.command()
@click.argument("goal")
@click.option("--by", default=None, help="Target date e.g. 2025-12-31")
def log_goal(goal, by):
    """Log a career goal."""
    db.log_goal(goal, target_date=by)
    click.echo(f"Goal logged: {goal}")

# Log a job application
@cli.command()
@click.argument("company")
@click.argument("role")
def log_job(company, role):
    """Log a job application."""
    db.log_job(company, role)
    click.echo(f"Application logged: {role} at {company}")

# Chat with message histroy as context
@cli.command()
def chat():
    """Start an interactive conversation with the agent."""
    system = load_system_prompt()
    db_context = db.get_context_block()
    personal_context = load_personal_context()
    
    base_context = f"{personal_context}\n\n{db_context}"
    conversation_history = []
    
    click.echo("\nCareer Agent ready. Type 'exit' to quit.\n")
    
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("exit", "quit"):
            break
        if not user_input:
            continue
        
        # First message includes full context, subsequent ones don't need to repeat it
        if not conversation_history:
            content = f"{base_context}\n\n---\n\n{user_input}"
        else:
            content = user_input
            
        conversation_history.append({"role": "user", "content": content})
        
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1000,
            system=system,
            messages=conversation_history
        )
        
        reply = response.content[0].text
        conversation_history.append({"role": "assistant", "content": reply})
        
        click.echo(f"\nAgent: {reply}\n")

if __name__ == "__main__":
    cli()
