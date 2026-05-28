# Python Practice Codebase

Welcome to the **Python Practice Codebase**! This repository is a curated collection of Python scripts, exercises, and examples covering fundamental to advanced programming concepts. It serves as an interactive learning guide and reference for Python scope, Object-Oriented Programming (OOP), Data Structures, and popular Data Science libraries like **NumPy** and **Pandas**.

---

## 📂 Repository Structure

The codebase is organized into modular directories, each focusing on a specific Python domain:

```text
python-practise-code/
│
├── 📁 PythonLibraries/         # Scope & Access Specifiers (Core Demos)
│   ├── GlobalKeyword.py        # Modifying global variables inside functions
│   ├── GlobalVariable.py       # Global scope usage
│   ├── PrivateAttribute.py     # Name-mangling demonstrations for private attributes
│   ├── PrivateAttribute1.py    # Class methods accessing private attributes
│   └── ProtectedAttribute.py   # Protected variables syntax and conventions
│
├── 📁 PythonOOPS/              # Object-Oriented Programming Fundamentals
│   ├── 📁 AccessingParent/     # Superclass & parent reference methods
│   ├── class.py                # Class & instance creations
│   ├── Methods.py              # Instance, class, and static methods
│   ├── SingleInheritance.py    # Standard parent-child inheritance
│   ├── MultipleInheritance.py  # Inheriting from multiple parent classes
│   ├── MultilevelInheritance.py# Multi-tiered inheritance hierarchy
│   ├── HierarchicalInheritance.py# Single parent, multiple child classes
│   ├── isinstance.py           # Runtime type-checking with isinstance()
│   └── issubclass.py           # Verification of class hierarchies
│
├── 📁 accessspecifiers/        # Detailed Access Controls
│   ├── PublicAccess.py         # Unrestricted class variables
│   ├── ProtectedAccess.py      # Standard single-underscore access rules
│   ├── PrivateAccess.py        # Strict double-underscore constraints
│   ├── finalize.py             # Class cleanup demonstrations
│   ├── override.py             # Method overriding mechanics
│   └── new.py                  # Custom object creation methods
│
├── 📁 numpy/                   # Numerical Python & Array Computing
│   ├── 📁 Dimensional/         # 1D, 2D, 3D, and nD array setups
│   ├── 📁 NumpyOpreations/     # Reshaping, Mean, Sum, and Max Operations
│   ├── 📁 FileSystem/          # File reading, loading, and sorting
│   ├── append.py               # Dynamic array expansion
│   ├── reverseArray.py         # Efficient array reversal
│   └── shape.py                # Inspecting array structures and shapes
│
├── 📁 Pandas/                  # Data Manipulation & Analysis
│   ├── ObjectSeries.py         # Working with 1D labeled Pandas Series
│   ├── DataFrame.py            # Creating and indexing DataFrames
│   ├── NewColumn.py            # Adding dynamic data columns
│   ├── ExistingColumns.py      # Selecting and processing active columns
│   ├── MissingValues.py        # Detecting, dropping, and filling NaN values
│   ├── CommonValue.py          # Intersection operations on DataFrames
│   ├── UnCommonValue.py        # Difference operations on DataFrames
│   ├── concatHorizontal.py     # Horizontal axis merging
│   ├── concatVertical.py       # Vertical axis stack concatenation
│   └── reindexing.py           # Aligning indexes dynamically
│
└── 📁 Root level files         # Fundamental core structures (e.g., self.py, docstring.py)
```

---

## 🧠 Core Topics & Concepts Covered

### 1. Scope and Access Specifiers

Python handles variable scope and access restrictions through unique naming conventions and keywords:

*   **Global vs Local Scope**: The `global` keyword tells a function to bind to a variable in the global module scope rather than creating a local shadow copy.
*   **Protected Attributes (`_var`)**: Declared with a single underscore prefix. This is a convention warning other developers that the variable is protected and shouldn't be accessed outside the class, though Python does not strictly enforce it.
*   **Private Attributes (`__var`)**: Declared with a double underscore prefix. Python strictly enforces encapsulation via **Name Mangling**, internally renaming `self.__salary` to `_ClassName__salary` to avoid direct access.

#### 💡 Private Attribute Handling Example
```python
class Student:
    def __init__(self):
        self.__salary = 50000  # Private variable

obj = Student()

# This raises an AttributeError:
# print(obj.__salary) 

# The correct way via Name Mangling:
print(obj._Student__salary)  # Outputs: 50000
```

---

### 2. Object-Oriented Programming (OOP)

OOP principles form the backbone of clean, reusable python code:

*   **Inheritance Patterns**:
    *   **Single Inheritance**: One child class inherits from one parent class.
    *   **Multiple Inheritance**: A class inherits attributes/methods from more than one parent.
    *   **Multilevel Inheritance**: A child class inherits from a parent which itself is a child of another class.
    *   **Hierarchical Inheritance**: Multiple child classes inherit from a single parent class.
*   **Introspection**:
    *   `isinstance(obj, ClassName)` checks if an object is an instance of a class or subclass.
    *   `issubclass(Child, Parent)` verifies class inheritance relationships at runtime.

---

### 3. NumPy (Numerical Python)

NumPy provides powerful N-dimensional array objects (`ndarray`) and vectorized mathematical operations:

*   **Dimensionality**: Deep dives into 1D, 2D, 3D, and n-Dimensional arrays.
*   **Mathematical Operations**: Vectorized aggregations such as `sum()`, `mean()`, and finding the `max()` value across specified axes.
*   **Array Manipulation**: Inspecting structures using `.shape`, reshaping arrays, and reversing dimensions.

---

### 4. Pandas (Data Analysis)

Pandas facilitates fast and efficient data structures for relational or labeled data:

*   **Series & DataFrames**: Core data structures representing 1D arrays and 2D tabular formats.
*   **Data Cleaning**: Locating, replacing, or removing missing/empty cells (`NaN` values).
*   **Merging & Concatenation**: Combining multiple datasets horizontally or vertically.
*   **Set Comparison**: Identifying common and unique values between separate datasets.

---

## 🚀 How to Run the Scripts

### Prerequisites
Make sure you have **Python 3.x** and the required libraries installed.

```bash
# Clone this repository (or open your local copy)
cd Python

# Create and activate a virtual environment (optional but recommended)
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# Install required dependencies
pip install numpy pandas
```

### Execution Example
You can run any script from the terminal by passing its path to Python:

```bash
python PythonLibraries/PrivateAttribute.py
```

---

## 🛠️ Key Learnings Reference

| Category | Key Concept / Tool | Primary Python Feature Demonstrated |
| :--- | :--- | :--- |
| **OOP** | Encapsulation | Name-mangled private variables (`_ClassName__var`) |
| **OOP** | Hierarchical Hierarchy | Multilevel and Multiple Inheritance |
| **OOP** | Introspection | `isinstance()` and `issubclass()` |
| **Data Sci** | Vectorization | Fast mathematical operations using NumPy |
| **Data Sci** | Tabular Alignment | `pd.DataFrame`, dynamic columns, and `reindexing` |
| **Scope** | Global Modification | `global` keyword inside functions |

---

*This practice guide is structured to help quickly lookup real-world code snippets and syntax templates! Happy coding!*
