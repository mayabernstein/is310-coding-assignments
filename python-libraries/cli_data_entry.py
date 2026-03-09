import rich
from rich.table import Table
from rich.console import Console
import os

console = Console()
console.print("Here is some initial data:", style="blue")

table = Table(title="Olympic Swimming Records")
table.add_column("Olympian", style="cyan", no_wrap=True)
table.add_column("Country", style="cyan")
table.add_column("Event", style="cyan")
table.add_column("Time", style="cyan")
table.add_column("Olympic", style="cyan")
table.add_row("Pan Zhanle", "China", "100m Freestyle", "46.40s", "Paris 2024")
table.add_row("Michael Phelps", "USA", "200m Freestyle", "1:42.96s", "Beijing 2008")
table.add_row("Sun Yang", "China", "400m Freestyle", "3:40.14s", "London 2012")
table.add_row("Adam Peaty", "Great Britain", "100m Breaststroke", "57.13s", "Rio 2016")

console.print(table)
file_name = "swim_records.txt"
file_path = os.path.abspath(file_name)

while True: 
    console.print("\n[purple]Enter some Olympic swimming record data:[/purple]")

    while True:
        olympian = console.input("Olympian: ")
        country = console.input("Country: ")
        event = console.input("Event: ")
        time = console.input("Time: ")
        olympic = console.input("Olympic: ")

        console.print(f"\nYou entered: [bold]{olympian}[/bold] from [bold]{country}[/bold] set a record in [bold]{event}[/bold] with a time of [bold]{time}[/bold] at [bold]{olympic}[/bold].")

        confirmation = console.input("Is this correct? (y/n)")

        if (confirmation.lower() == 'y'):
            console.print("Data entry confirmed!", style="green")
            break
        else:
            console.print("Please re-enter the data.\n", style="red")
    # add to table
    table.add_row(olympian, country, event, time, olympic)

    # save to file (append)
    with open(file_name, "a") as file:
        file.write(f"{olympian}, {country}, {event}, {time}, {olympic}\n")

    console.print(f"Data saved to {file_path}", style="green")

    # ask if user wants another entry
    again = console.input("Do you want to enter another record? (y/n)")

    if (again.lower() != 'y'):
        break
console.print("\nFinal Table of Olympic Swimming Records:", style="blue")
console.print(table)          