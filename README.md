# ParetoViz - Pareto Chart Visualization in Python

![Pareto Chart Example](images/pareto_example.png)

## Overview

**ParetoViz** is a beginner-friendly Python tool to create Pareto Charts using `matplotlib` and `pandas`.  
A Pareto Chart merges a bar chart and a line graph, highlighting the most significant factors in any dataset based on the Pareto Principle (80/20 rule).

Use ParetoViz to visualize categorical data and analyze cumulative category impacts easily.

---

## Features

- Reads data from a CSV file (`data/sample_data.csv`)
- Sorts data by value in descending order
- Plots a bar chart for individual category values
- Overlays a cumulative percentage line chart
- Saves the chart as an image (`images/pareto_example.png`)
- Easy to customize and extend

---

## Project Structure

```
ParetoViz/
│
├── data/
│   └── sample_data.csv         # Sample input data
│
├── images/
│   └── pareto_example.png      # Output Pareto chart image
│
├── utils/
│   └── helpers.py              # Utility functions (e.g., cumulative % calculation)
│
├── pareto_chart.py             # Main plotting script
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Kirankumarvel/ParetoViz.git
   cd ParetoViz
   ```

2. **(Optional) Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Linux/macOS:
   source venv/bin/activate
   # On Windows PowerShell:
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Generate and display the Pareto chart by running:
```bash
python pareto_chart.py
```
The chart image will be saved as `images/pareto_example.png`.

---

## How It Works

- Loads category and value data from `data/sample_data.csv`
- Sorts data in descending order by value
- Plots a bar chart for category values
- Overlays a cumulative percentage line to illustrate the Pareto Principle
- Uses the utility function `calculate_cumulative_percent` for cumulative percentage calculations

---

## Customization

- Replace `sample_data.csv` with your own categories and values
- Edit `pareto_chart.py` to change chart styles, colors, or add more features

---

## Dependencies

- `matplotlib` for plotting charts
- `pandas` for data handling

See `requirements.txt` for specific versions.

---

## License

This project is licensed under the MIT License.

---

## Author & Contact

Created by [Kirankumarvel](https://github.com/Kirankumarvel)  
GitHub Repo: [ParetoViz](https://github.com/Kirankumarvel/ParetoViz)

---

## References

- [Pareto Principle - Wikipedia](https://en.wikipedia.org/wiki/Pareto_principle)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
```
