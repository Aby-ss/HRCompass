from rich import print
from rich import text
from rich.panel import Panel
from rich.table import Table
from rich.layout import Layout
from rich.console import Console

from rich.traceback import install
install(show_locals=True)

from datetime import datetime
import numpy as np
import pandas as pd
import asciichartpy
import math

console = Console()
layout = Layout()

layout.split_column(
        Layout(name = "Header"),
        Layout(name = "Body"),
        Layout(name = "Footer")
        )

layout["Body"].split_row(Layout(name = "Body_Right"), Layout(name = "Body_Left"))
layout["Body_Right"].split_column(
        Layout(name = "BR_1"),
        Layout(name = "BR_2")
        )

layout["Body_Left"].split_column(
        Layout(name = "BL_1"),
        Layout(name = "BL_2")
        )

layout["Header"].size = 3
layout["Footer"].size = 3

class Header:
    def __rich__(self) -> Panel:
        grid = Table.grid(expand = True)
        grid.add_column(justify = "center", ratio = 1)
        grid.add_column(justify = "right")
        grid.add_row("[b]HR[/]Compass", datetime.now().ctime().replace(":", "[blink]:[/]"))

        return Panel(grid, style = "Green on Black")

def Employee_DB():
    csv_path = 'EmployeeDB.csv'
    # Read the CSV file into a Pandas DataFrame
    data = pd.read_csv(csv_path)
    
    # Initialize the table
    EDP_table = Table(show_header=True, header_style="bold magenta")
    
    # Add columns to the table
    for column in data.columns:
        EDP_table.add_column(column)
    
    # Add rows to the table
    for row in data.values.tolist():
        EDP_table.add_row(*row)
    return Panel(EDP_table, title = "Employee Database", title_align = "left", style = "Bold White")

def Firm_Productivity():
    x = [i * 0.1 for i in range(0, 68)]
    y = [math.cos(xi) for xi in x]
    chart = asciichartpy.plot(y, {"height" : 16, "width" : 50})

    return Panel(chart, title = "Firm Productivity", title_align = "left", style = "bold white")

def Attendance():
    x = [i * 0.1 for i in range(0, 63)]
    y_values = [math.sin(xi) for xi in x]
    chart_data = asciichartpy.plot(y_values, {'height': 16, 'width': 50})

    return Panel(chart_data, title="Bar Chart")


layout["Header"].update(Header())
layout["BR_1"].update(Employee_DB())
layout["BL_1"].update(Firm_Productivity())
layout["BR_2"].update(Attendance())

print(layout)
