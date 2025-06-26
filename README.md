# 📦 Product Inventory Management System

**Maryam Elhamidi**
Programming Fundementals
Instructor: Sara Shaheen
October 25, 2023

---

## 🎯 Project Overview

This is a **Python-based inventory tracking application** that simulates a year-long sales and stock cycle for a product. It uses object-oriented principles like **inheritance**, **encapsulation**, and **modular design** to manage product attributes, monthly production, stock levels, and profit calculations.

---

## 💡 Key Features

* **User-Driven Input**: Collects data such as product name, code, price, costs, and stock levels
* **Stock & Sales Simulation**: Simulates 12 months of stock, manufacturing, and random sales
* **Profit Calculation**: Computes net profit for the year, rounded to 2 decimal places
* **Validation**: Checks all user inputs for correctness and data type
* **BONUS**:

  * Prevents stock from going negative
  * Tracks and reports unfulfilled sales

---

## 🛠️ Technologies Used

* Python 3.x
* `random` module
* Object-Oriented Programming (OOP)
* Git & GitHub for version control

---

## 🧱 Class Breakdown

### 📘 `Product` (in `Module_A2.py`)

Base class for all products. Contains:

| Attribute                    | Description           | Data Type |
| ---------------------------- | --------------------- | --------- |
| `product_code`               | Product identifier    | `int`     |
| `product_name`               | Name of product       | `str`     |
| `sale_price`                 | Selling price         | `float`   |
| `manufacture_cost`           | Cost to manufacture   | `float`   |
| `stock_level`                | Current stock         | `int`     |
| `monthly_units_manufactured` | Estimated units/month | `int`     |

Includes **getters** for all attributes.

---

### 🖥️ `Application` (in main file)

Inherits from `Product`. Contains:

* `setProductinfo()`: Collects and validates user input, runs simulation
* `process_sale()`: Ensures stock never drops below zero
* `simulate_sales()`: Tracks unsuccessful sales and prints report

---

## 💵 Net Profit Calculation

```
Net Profit = (Total Units Sold * Sale Price) - (Total Units Manufactured * Manufacturing Cost)
```

Rounded to 2 decimal places for clarity.

---

## 🧪 Sample Output (Abbreviated)

```plaintext
♥ Welcome to Maryam's Sample Product Inventory ♥

Enter Product Name: Chips
Enter Product Sale Price: 2.99
...

♥ Maryam's Sample Stock Statement ♥
Product Code: 222
Product Name: Chips
...

Month 1:
Manufactured: 200 units
Sold: 193 units
Stock: 107 units
...

Net Profit: $789.23 CAD
```

---

## 📌 Notes

* `setProductinfo()` handles **all user interaction** (as required by assignment guidelines).
* All core logic and calculations are encapsulated within the `Application` class.
* The `Product` class acts as a **data model** with protected access and getters.
* The design respects **OOP principles** like separation of concerns and reusability.

---

## 🧠 Reflections & Learnings

> “Initially, I placed all my code in the `Product` module, which led to issues when applying interaction rules. I later restructured everything to isolate interaction within `Application`, added getters, and properly inherited from `Product`. Through trial and error, I learned about class structure, data validation, and controlling user flow effectively.” – *Maryam*

---


## ✅ Future Improvements

* Add a **menu system** for more user control (e.g., update product, view summary, simulate only sales)
* Allow saving results to a file
* Add exception handling for string/number mismatch during input

---
