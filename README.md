GearGuard – Odoo Maintenance & Sales Customization

> A **Dockerized Odoo project** that delivers a complete **Maintenance Management System** along with **custom Sales Order enhancements** — built for scalability, collaboration, and real‑world operations.

---

📌 Project Overview

GearGuard is a custom Odoo implementation designed to:

* Track equipment and maintenance activities efficiently
* Manage maintenance teams and requests
* Extend Odoo’s Sales module with custom UI enhancements
* Provide a clean, Docker‑based development and deployment workflow

The project consists of **two core Odoo modules**:

* **GearGuard (Maintenance Tracker)**
* **Sales Custom (Sales Enhancements)**

---

🧩 Modules Breakdown

### ⚙️ GearGuard – Maintenance Tracker

| Attribute        | Details      |
| ---------------- | ------------ |
| **Version**      | 1.0          |
| **Category**     | Maintenance  |
| **Dependencies** | `base`, `hr` |

#### 🔑 Key Features

* 🏭 Equipment tracking & lifecycle management
* 🧾 Maintenance request creation & monitoring
* 👥 Maintenance team & staff assignment
* 📊 Structured maintenance workflow
* 🧪 Demo data included for quick testing

---

### 🛒 Sales Custom – Sales Order Enhancements

| Attribute        | Details        |
| ---------------- | -------------- |
| **Version**      | 1.0            |
| **Dependencies** | `base`, `sale` |

#### 🔑 Key Features

* ✨ Customized Sales Order views
* 🎨 Enhanced UI components
* 🧩 Frontend assets using **JavaScript & CSS**
* 🔧 Seamless integration with Odoo Sales module

---

## 🏗️ System Architecture (High Level)

```
┌──────────────┐
│   Browser    │
│ (User UI)    │
└──────┬───────┘
       │  http://localhost:8069
┌──────▼───────┐
│     Odoo     │
│ Application  │
│  (Docker)    │
└──────┬───────┘
       │
┌──────▼───────┐
│ PostgreSQL   │
│  Database    │
│  (Docker)    │
└──────────────┘
```

---

## ✅ Prerequisites

Before you begin, ensure you have:

* 🐳 **Docker** installed
* 🐙 **Docker Compose** installed
* 🌱 **Git** for version control

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone <repository-url>
cd gear_guard
```

---

### 2️⃣ Start the Application

```bash
docker compose up
```

This will automatically start:

* 🗄️ **PostgreSQL Database** → Port `5432`
* 🌐 **Odoo Server** → Port `8069`

---

### 3️⃣ Access Odoo

Open your browser and visit:

👉 **[http://localhost:8069](http://localhost:8069)**

---

## ⚙️ Configuration Details

* 📄 **Odoo config file**: `odoo.conf`
* 📦 **Custom addons path**: `addons/`
* 💾 **Database persistence**: Docker volume
* 🧩 Modules are auto‑loaded via mounted volumes

---

## 🧑‍💻 Usage Guide

1. Log in to Odoo using **admin credentials**
2. Navigate to:

   * **Apps → Update Apps List**
3. Search and install:

   * 🔧 **GearGuard**
   * 🛒 **Sales Custom**
4. Configure:

   * Users & roles
   * Maintenance teams
   * Permissions & workflows
5. Start managing:

   * Equipment & maintenance requests
   * Customized sales orders

---

## 🧪 Development Guidelines

* 📁 Add new modules inside the `addons/` directory
* 🧱 Follow official **Odoo development best practices**
* 🐳 Always use Docker for a consistent dev environment
* 🔄 Restart services after module changes

---

## 🤝 Contributing

We welcome contributions! 🚀

**Steps:**

1. Fork the repository
2. Create a new feature branch
3. Implement your changes
4. Test thoroughly
5. Submit a pull request

---

📜 License

This project is licensed under the **MIT License**.

📄 See the `LICENSE` file for more details.

---

🆘 Support

If you face any issues or have questions:

* 🐛 Open an issue in the GitHub repository
* 💬 Provide logs and clear steps to reproduce the issue

---

✨ *Built with Odoo, Docker, and a focus on scalable maintenance management.*
