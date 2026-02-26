import click
from openai import OpenAI
from rich.console import Console
from rich.markdown import Markdown

# Initialize OpenAI client
client = OpenAI()
console = Console()

@click.command()
@click.argument('spec')
def api_mock(spec):
    """AI-powered API mock response generator."""
    console.print(f"[bold blue]Generating mock response for: {spec}...[/bold blue]")

    prompt = f"""
    Generate a realistic JSON mock API response based on the following API specification or example.
    Specification/Example: {spec}
    Format your response in Markdown.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {{"role": "system", "content": "You are an expert API developer."}},
                {{"role": "user", "content": prompt}}
            ]
        )
        mock_text = response.choices[0].message.content
        console.print(Markdown(mock_text))
    except Exception as e:
        console.print(f"[bold red]Error during mock generation:[/bold red] {e}")

if __name__ == '__main__':
    api_mock()
