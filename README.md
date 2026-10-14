# Seva Setu – Pension Portal (Fixing the Legacy)

A production-grade refactor, debugging, and deployment of **Seva Setu**, a citizen-facing state government pension portal inherited under the *Build for Bharat Fellowship*.

---

## 📌 Project Overview

This repository contains the diagnosed, stabilized, and deployed pension management platform. The inherited system originally featured:
- A legacy application stack serving a citizen database of over 100,000 pensioners[cite: 31].
- Asynchronous SMS notification gateway mocks (`smsgw`).
- Background scheduled automation scripts for deemed approvals (`app/scripts/deemed_approval.py`).
- Model Context Protocol integration servers (`mcp_servers/`)[cite: 32].
- Historical server log traces indicating performance bottlenecks, high query latencies, and service outages[cite: 31].

---

## 🏗 System Architecture & Services

The application runs as a containerized multi-service ecosystem managed via Docker Compose[cite: 32]:

| Service | Technology | Role |
| :--- | :--- | :--- |
| **`app`** | Python 3.11, Flask, Gunicorn | Main web application and REST API portal[cite: 32] |
| **`db`** | PostgreSQL | Primary relational database for pension records and citizen data[cite: 32] |
| **`smsgw`** | Python | Mock SMS gateway service handling dispatch notifications[cite: 32] |
| **`cron`** | Linux `cron` | Scheduled cron job executing statutory deemed approvals[cite: 32] |
| **`mcp_servers`** | Python / FastMCP | Citizen and officer MCP helper interfaces[cite: 32] |

---

## 🛠 Key Diagnoses & Applied Fixes

Detailed technical justifications, database profiling, and architectural trade-offs are documented in [`DESIGN_NOTE.md`](./DESIGN_NOTE.md)[cite: 31, 32]. High-level highlights include:

1. **Database Bottlenecks & Missing Indexes:**
   - Identified slow scans across legacy tables in `schema.sql`[cite: 32].
   - Applied composite indexes on pension lookup IDs and citizen status fields to improve query response times.

2. **Concurrency & Worker Optimization:**
   - Refactored Gunicorn worker bindings and timeouts inside the `Dockerfile` to handle peak user loads without thread starvation[cite: 32].

3. **Cron Reliability:**
   - Fixed cron execution environments and path bindings within `app/deploy/crontab` to ensure automated approvals run on schedule[cite: 32].

4. **Security & Input Sanitization:**
   - Patched input handling and session state vulnerabilities across core authentication and verification routes.

---

## 🚀 Local Setup & Installation

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Engine running)[cite: 30]
- [Git](https://git-scm.com/)

### 1. Clone the Repository
```bash
git clone [https://github.com/webreacher/sewasetu-ai-project.git](https://github.com/webreacher/sewasetu-ai-project.git)
cd sewasetu-ai-project
