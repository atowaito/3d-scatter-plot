3D Scatter Plot Program
---
# Project Overview
This program is a simple application that visualizes a list of friends in a 3D graph. Each data point is represented by a name and coordinates (x, y, z) and is displayed as a sphere in 3D space. The color of each sphere is vividly colored based on the x, y, z coordinates.

# Project Structure

```
3d-scatter-plot/
│
├── scatter3d.py              # Main program file
├── requirements.txt        # Required Python libraries
└── data/
            └── data001.txt   # Data file

```

##3. Prerequisites

To run this program, you need the following software:

- Windows 10 or 11
- Python 3.x
- Required Python libraries (pandas, plotly)

# 4. Instructions
## 4-1. Clone the Repository
First, clone the project repository from GitHub.

```
git clone https://github.com/atowaito/3d-scatter-plot.git
cd 3d-scatter-plot
```

## 4-2. Create and Activate a Virtual Environment

Create a Python virtual environment and activate it.

``` bash
# Create a virtual environment
python -m venv env

# Activate the virtual environment (Linux/Mac)
source env/bin/activate

# Activate the virtual environment (Windows)
env\Scripts\activate

```

## 4-3. Install Required Libraries

With the virtual environment activated, install the libraries listed in requirements.txt.

``` bash
pip install -r requirements.txt
```

## 4-4. Edit the Data File

Open data/data001.txt in a text editor and edit it. The file should be formatted as follows:

```
Name1(x1,y1,z1)
Name2(x2,y2,z2)
...
```

Example:

```
Alice(5,3,1)
Bob(8,6,2)
Charlie(3,7,9)
```

## 4-5. Run the Program
Run the program using the edited data file.
```
python scatter3d.py
```
This will generate a 3D graph based on the data, displayed in a browser. You can rotate the graph with the mouse to observe the data from various angles.

# 5. How to Change Axis Names

To change the axis names, modify the following section in scatter3d.py:

``` python
fig.update_layout(
    scene=dict(
        xaxis_title='X Axis Name',  # Name for X-axis
        yaxis_title='Y Axis Name',  # Name for Y-axis
        zaxis_title='Z Axis Name'   # Name for Z-axis
    ),
    title='3D Scatter Plot with Labels'
)

```

For example, to change the axis names to "Horizontal", "Vertical", and "Height", you would write:

```Python
fig.update_layout(
    scene=dict(
        xaxis_title='Horizontal',
        yaxis_title='Vertical',
        zaxis_title='Height'
    ),
    title='3D Scatter Plot with Labels'
)

```

Re-run the program to see the graph with the updated axis names.