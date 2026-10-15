import json
from pathlib import Path
from rich.console import Console
from rich.table import Table

console = Console()
file_path = Path(__file__).resolve().parent / "jinn_stories.json"

stories = [
    {
        "story_name": "The Fisherman and the Jinni",
        "culture": "Middle Eastern",
        "description": "A fisherman releases a jinni from a jar.",
        "source": "One Thousand and One Nights",
    },
    {
        "story_name": "Aladdin and the Magic Lamp",
        "culture": "Middle Eastern literary tradition",
        "description": "Aladdin finds a magic lamp with a genie inside.",
        "source": "One Thousand and One Nights",
    },
]


def show_stories(story_list):
    table = Table(title="Supernatural Stories Across Cultures")
    table.add_column("Story Name", style="cyan")
    table.add_column("Culture / Origin", style="magenta")
    table.add_column("Description")
    table.add_column("Source")

    for story in story_list:
        table.add_row(
            story["story_name"],
            story["culture"],
            story["description"],
            story["source"],
        )
    console.print(table)


def ask_field(question):
    answer = input(question).strip()
    while not answer:
        console.print("Please enter something for this field.", style="yellow")
        answer = input(question).strip()
    return answer


console.print("Here are two example supernatural stories:", style="bold cyan")
show_stories(stories)

if file_path.exists():
    with open(file_path, "r", encoding="utf-8") as file:
        stories = json.load(file)
    console.print("\nLoaded your previously saved stories.", style="green")

while True:
    console.print("\n[bold]Add a story[/bold]")

    while True:
        story = {
            "story_name": ask_field("Story name: "),
            "culture": ask_field("Culture / origin: "),
            "description": ask_field("Short description: "),
            "source": ask_field("Source: "),
        }

        console.print("\nPlease check your entry:")
        show_stories([story])
        confirm = input("Is this correct? (yes/no): ").strip().lower()
        if confirm in ("yes", "y"):
            stories.append(story)
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(stories, file, indent=2, ensure_ascii=False)
            console.print(f"Saved to: {file_path}", style="bold green")
            break
        console.print("No problem. Enter the story again.", style="yellow")

    another = input("Would you like to add another story? (yes/no): ").strip().lower()
    if another not in ("yes", "y"):
        break

console.print("\nThanks for adding to the collection!")
