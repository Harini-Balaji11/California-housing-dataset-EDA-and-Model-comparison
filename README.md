
# Mathematical Foundation Project 3

This project explores **linear regression** using **gradient descent optimization** applied on a real-world dataset (loaded via a built-in library). The objective is to understand the mathematical foundations of regression, error minimization, and optimization, implemented manually in Python.

---

## Project Overview

This notebook demonstrates the full pipeline of:
- Loading and visualizing a real dataset,
- Performing linear regression from scratch (without using built-in ML models),
- Minimizing error using **gradient descent**,
- Visualizing both the learning process and final results.

---

##  Dataset Used

- The dataset is **loaded from a built-in library** such as `sklearn.datasets` or `seaborn`.
- It contains numerical features suitable for simple linear regression.
- A subset of the data (one feature vs one target) is used for 2D visualization and modeling.

---

##  Key Concepts Covered

1. **Exploratory Data Analysis (EDA)**
2. **Feature Selection**
3. **Mean Squared Error (MSE)**
4. **Gradient Descent Optimization**
5. **Manual Linear Regression**
6. **Loss Curve Visualization**

---

##  Steps Followed in the Project

### 1. **Importing Libraries**
   - `numpy`, `pandas`, `matplotlib.pyplot`, and the dataset loader (e.g., `sklearn.datasets` or `seaborn`)
   - Purpose: Data loading, numerical computation, and visualization

---

### 2. **Dataset Loading**
   - A dataset is loaded using a built-in method.
   - One independent variable (feature) and one dependent variable (target) are selected.
   - Data is structured as numpy arrays or DataFrames.

---

### 3. **Data Visualization**
   - A scatter plot is created to observe the relationship between the selected feature and target.
   - This helps verify if a linear relationship exists, justifying the use of linear regression.

---

### 4. **Parameter Initialization**
   - Initial values for slope `m` and intercept `c` are set randomly.
   - Learning rate (`lr`) and number of iterations (`epochs`) are defined.

---

### 5. **Loss Function (MSE) Definition**
   - The error between predicted and actual values is calculated using:
     \
     MSE = (1/n) * Σ(y - y_pred)^2
     \
   - Helps evaluate model accuracy during training.

---

### 6. **Gradient Descent Implementation**
   - Compute gradients of the loss function:
     - ∂MSE/∂m and ∂MSE/∂c
   - Update rules:
     \
     m = m - lr * ∂/∂m,   c = c - lr * ∂/∂c
     \
   - Loop through `epochs` to iteratively update and minimize loss.

---

### 7. **Training Loop**
   - In each iteration:
     - Predict output using current `m`, `c`
     - Compute loss and gradients
     - Update parameters
     - (Optional) Store loss history for visualization

---

### 8. **Result Visualization**
   - Final regression line is plotted on the original data.
   - Optional: plot the loss curve (MSE vs Epochs) to show convergence behavior.

---

### 9. **Model Output**
   - Final optimized values of `m`, `c` are printed.
   - This gives the equation of the best-fit line learned through gradient descent.

---

##  Sample Outputs

- **Best Fit Line Equation:**  
  `y = mx + c` (based on learned `m` and `c` values)

- **Final MSE Value:**  
  A small number indicating low error between predicted and actual values

---

##  Learning Outcomes

- Applying linear regression using real-world data
- Understanding loss function and gradient updates
- Coding gradient descent from scratch
- Visualizing model performance and convergence

---

---

## 📎 License

This project is provided under the MIT License for educational purposes.
