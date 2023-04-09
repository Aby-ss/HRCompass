import random
from rich.panel import Panel
from rich.console import Console
from PIL import Image

# define person's specifications
person = {
    "name": "John Doe",
    "age": 30,
    "occupation": "Software Engineer",
    "nationality": "United States of America",
    "hours_worked": 120,
    "Department": "IT Support"
}

# generate random pixels for person's face
pixels = []
for i in range(100):
    row = []
    for j in range(100):
        row.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    pixels.append(row)

# create image from pixels
img = Image.new('RGB', (100, 100))
img.putdata([pixel for row in pixels for pixel in row])

# create panel with person's specifications and image
panel = Panel.fit(
        f"[b]{person['name']}[/b]\n\n[b]AGE[/b]: {person['age']}\n[b]OCCUPATION[/b]: {person['occupation']}\n[b]NATIONALITY[/]: {person['nationality']}\n[b]HOURS WORKED THIS WEEK[/]: {person['hours_worked']}\n[b]DEPARTMENT[/]: {person['Department']}\n[b]ID[/b]",
    title="ID Card",
    border_style="green",
    padding=(1, 2),
    width=50
)

# print panel to console
console = Console()
console.print(panel)

