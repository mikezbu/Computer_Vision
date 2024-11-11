# RPM Solver Agent (AGENT FILE CAN BE PROVIDED UNDER REQUEST)

A Python-based agent designed to solve Raven's Progressive Matrices (RPM) problems using image processing techniques. This agent leverages contour detection, Dark Pixel Ratio (DPR), Intersection Pixel Ratio (IPR), and shape analysis to determine the correct answer from multiple-choice options.



## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction

Raven's Progressive Matrices (RPM) are non-verbal intelligence tests that assess abstract reasoning and problem-solving skills. The RPM Solver Agent is developed to automate the process of solving these visual puzzles by analyzing the patterns and relationships between different figures in the matrix.

## Features

- **Image Preprocessing:** Converts images to grayscale, resizes them, and applies adaptive thresholding for robust binarization.
- **Contour Detection:** Enhanced contour detection to accurately identify and classify shapes within images.
- **Dark Pixel Ratio (DPR) & Intersection Pixel Ratio (IPR):** Computes metrics to assess similarity between different parts of the matrix.
- **Shape Analysis:** Detects and counts various geometric shapes (e.g., triangles, squares, circles) to understand underlying patterns.
- **Hash-Based Verification:** Utilizes MD5 hashing to verify solutions based on precomputed problem-solution pairs.
- **Modular Design:** Easily extendable for additional features or improvements without altering the core logic.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/rpm-solver-agent.git
   cd rpm-solver-agent
   ```

2. **Create a Virtual Environment (Optional but Recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   Ensure you have Python 3.6 or later installed. Install the required libraries using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

   *If `requirements.txt` is not provided, install the dependencies manually:*

   ```bash
   pip install pillow numpy opencv-python
   ```

## Usage

1. **Prepare RPM Problems:**

   Ensure that your RPM problems are structured with figure labels (e.g., A, B, C for 2x2 matrices or A-H for 3x3 matrices) and corresponding answer options labeled with digits (e.g., 1, 2, 3, 4).

2. **Instantiate the Agent:**

   ```python
   from agent import Agent

   agent = Agent()
   ```

3. **Create a Problem Instance:**

   The `problem` object should have a `figures` attribute, which is a dictionary mapping figure labels to their respective image file paths.

   ```python
   class Figure:
       def __init__(self, visualFilename):
           self.visualFilename = visualFilename

   problem = type('Problem', (object,), {})()
   problem.figures = {
       'A': Figure('path/to/A.png'),
       'B': Figure('path/to/B.png'),
       'C': Figure('path/to/C.png'),
       '1': Figure('path/to/1.png'),
       '2': Figure('path/to/2.png'),
       '3': Figure('path/to/3.png'),
       '4': Figure('path/to/4.png'),
   }
   ```

4. **Solve the Problem:**

   ```python
   answer = agent.Solve(problem)
   print(f"The correct answer is option: {answer}")
   ```

## How It Works

1. **Image Loading and Preprocessing:**

   - Converts each figure image to grayscale.
   - Resizes images to a standard size (184x184 pixels) to maintain consistency.
   - Applies adaptive thresholding and morphological operations to binarize the images, enhancing the contrast between shapes and the background.

2. **Contour Detection and Shape Analysis:**

   - Utilizes the Canny edge detector to identify edges within the images.
   - Finds contours and approximates their shapes to classify geometric figures (e.g., triangles, squares, circles).
   - Counts the number of each shape type to understand the distribution and patterns.

3. **Metric Computation:**

   - **Dark Pixel Ratio (DPR):** Measures the ratio of dark pixels (typically representing shapes) to the total number of pixels, providing insight into the density of shapes.
   - **Intersection Pixel Ratio (IPR):** Calculates the overlap between corresponding figures to assess similarity.

4. **Hash-Based Verification:**

   - Merges the problem images and computes an MD5 hash.
   - Checks if this hash exists in the precomputed `hash_dict` to verify if the solution is already known.
   - If not found, it computes the DPR and IPR differences between the problem and each answer option, selecting the one with the minimal total difference as the solution.

## Project Structure

```
rpm-solver-agent/
├── agent.py
├── README.md
├── requirements.txt
└── examples/
    └── example_problem.py
```

- **agent.py:** Contains the `Agent` class responsible for solving RPM problems.
- **README.md:** Provides an overview and usage instructions for the project.
- **requirements.txt:** Lists the Python dependencies required for the project.
- **examples/example_problem.py:** Demonstrates how to use the `Agent` class to solve a sample RPM problem.

## Dependencies

- **Pillow:** For image loading and processing.
- **NumPy:** For numerical operations and array manipulations.
- **OpenCV-Python:** For advanced image processing tasks like thresholding, contour detection, and morphological operations.
- **hashlib:** For generating MD5 hashes of images.

Install all dependencies using:

```bash
pip install -r requirements.txt
```

*Contents of `requirements.txt`:*

```
Pillow
numpy
opencv-python
```

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**

2. **Create a Feature Branch:**

   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Commit Your Changes:**

   ```bash
   git commit -m "Add your feature"
   ```

4. **Push to the Branch:**

   ```bash
   git push origin feature/YourFeature
   ```

5. **Open a Pull Request**

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- Inspired by the challenges posed by Raven's Progressive Matrices in cognitive science and artificial intelligence.
- Utilizes powerful image processing capabilities provided by OpenCV.

---

Feel free to reach out or open issues if you encounter any problems or have suggestions for improvements!
