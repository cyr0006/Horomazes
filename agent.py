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
load_dotenv()
client = anthropic.Anthropic()

#database module imports
from career import db_career
from academia import db_academia
from fitness import db_fitness
from finance import db_finance

#CLI imports
from career.career_cli import career_cli
from academia.academia_cli import academia_cli
from fitness.fitness_cli import fitness_cli
from finance.finance_cli import finance_cli



def get_db_module(agent):
    if agent == "career":
        from career.db_career import db_career as db_module
    elif agent == "fitness":
        from fitness.db_fitness import db_fitness as db_module
    elif agent == "finance":
        from finance.db_finance import db_fitness as db_module
    elif agent == "academia":
        from academia.db_academia import db_academia as db_module
    else:
        raise ValueError(f"Unknown agent: {agent}")
    
    return db_module

#Load AI instructions
def load_system_prompt(agent):
    with open(f"prompts/system-{agent}.md", "r") as f:
        return f.read()
    
#Load context from file for who I am, what I do, and what I want
def load_personal_context(agent):
    try:
        with open(f"prompts/context-{agent}.md", "r") as f:
            return f.read()
    except FileNotFoundError:
        return ""

#Main function to ask the agent a question and get a response
def ask(user_message, agent):
    init(agent)
    db_module = get_db_module(agent)
    system = load_system_prompt(agent)
    db_context = db_module.get_context_block(agent)
    personal_context = load_personal_context(agent)
   
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
@click.option("--agent", default="career", help="Which agent to use (career/academia/fitness/finance etc.)")
def init(agent):
    """Initialise the database."""
    db_module = get_db_module(agent)
    db_module.init_db(agent)
    click.echo("Database initialised for agent: " + agent)

# No chat history or context query - just a one-off question to the agent, useful for quick queries without needing to start a full conversation
@cli.command()
@click.argument("message")
@click.option("--agent", default="career", help="Which agent to use (career/academia/fitness/finance etc.)")
def query(message, agent):
    """Ask the agent anything."""
    click.echo("\nThinking...\n")
    response = ask(message, agent)
    click.echo(response)

# Chat with message histroy as context
@cli.command()
@click.option("--agent", default="career", help="Which agent to use (career/academia/fitness/finance etc.)")
def chat(agent):
    """Start an interactive conversation with the agent."""
    init(agent)
    db_module = get_db_module(agent)
    system = load_system_prompt(agent)
    db_context = db_module.get_context_block(agent)
    personal_context = load_personal_context(agent)
    
    base_context = f"{personal_context}\n\n{db_context}"
    conversation_history = []
    
    click.echo(f"\n{agent.capitalize()} Agent ready. Type 'exit' to quit.\n")
    
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

#CLI command groups for different agents
cli.add_command(career_cli, name="career")
cli.add_command(fitness_cli, name="fitness")
cli.add_command(finance_cli, name="finance")
cli.add_command(academia_cli, name="academia")


if __name__ == "__main__":
    cli()
