# Walmart Advanced Software Engineering Experience 🛒

This repository contains my solutions for the **Walmart Advanced Software Engineering Job Simulation** on Forage. The project involves solving complex data structure problems, designing system architectures, and implementing data processing pipelines similar to those used in Walmart's supply chain and e-commerce systems.

## 🚀 Project Overview

The simulation focused on backend engineering tasks, specifically optimizing data handling and designing scalable architectures.

### Key Tasks Completed

#### 1. Advanced Data Structures: Power of Two Max Heap
-   **File**: `PowerOfTwoMaxHeap.java`
-   **Challenge**: Implement a highly optimized max heap where every parent node has $2^x$ children (configurable branching factor) instead of the standard binary heap (2 children).
-   **Solution**:
    -   Built a generic heap class that accepts a `branchingPower` parameter constructor (e.g., `1` for binary, `2` for 4-ary, `3` for 8-ary).
    -   Implemented `insert`, `popMax`, `siftUp`, and `siftDown` logic to respect the custom child count requirements.
    -   This structure optimizes cache locality and reduces the height of the tree for massive datasets.

#### 2. Data Processing & ETL Pipeline
-   **File**: `populate_database.py`
-   **Challenge**: Efficiently process fragmented shipping data from multiple CSV sources and populate a relational database.
-   **Solution**:
    -   Designed `ShipmentDatabaseHandler` to connect to an SQLite database.
    -   Merged data from `shipping_data_0.csv` (direct mapping) and `shipping_data_1.csv`/`shipping_data_2.csv` (linked shipment identifiers).
    -   Implemented automated foreign key resolution for `product` and `shipment` tables to ensure data integrity.

#### 3. System Architecture Design
-   **Files**: `DataProcessor_UML.pdf`, `PetDepartment_ERD.pdf`
-   **Challenge**: Design the backend architecture for a new department integration.
-   **Solution**:
    -   Created UML Class Diagrams to model the relationships between data processors and storage units.
    -   Designed an Entity Relationship Diagram (ERD) for the Pet Department database schema.

## 🛠️ Technology Stack

-   **Languages**: Java, Python 3
-   **Database**: SQLite
-   **Tools**: UML Modeling, JDBC/Python DB-API

## 💻 Usage

### Running the Heap Implementation
```bash
javac PowerOfTwoMaxHeap.java
java PowerOfTwoMaxHeap
```
*Output will demonstrate the insertion sort order and max extraction.*

### Running the Data Pipeline
```bash
python populate_database.py
```
*This will read from the `data/` directory and create/update `shipment_database.db`.*

## 🤝 Acknowledgments

-   **Walmart Global Tech**: For the realistic problem statements.
-   **Forage**: For hosting the job simulation experience.

## 👤 Author

**Kanishk Khan**
-   GitHub: [@Kanishkhan](https://github.com/Kanishkhan)
