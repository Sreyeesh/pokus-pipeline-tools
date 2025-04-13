

---

# 🎬 Tuulekera Pipeline (Poku Ärkab)

**Codename:** `Tuulekera`  
**Project Title:** *Poku Ärkab*  
**Show Code:** `TLK`  
**Type:** Animation Short Film (30 seconds)  
**Owner:** Sreyeesh Garimella  

This is a fully Dockerized, production-ready animation pipeline built for the short film *Poku Ärkab*. The project is organized using best practices from animation and VFX studios, with an internal codename (`Tuulekera`) to separate production logic from the film’s public-facing identity.

📂 Folder structures, naming conventions, asset registration, and versioning are all driven by config — enabling clean automation and scalable workflows, even for a small team.

---

## 🧭 Notion Dashboard (Production Hub)

🔗 [**Tuulekera – Notion Workspace**](https://stump-principle-4a6.notion.site/Tuulekra-1d4c1e24aece80a19fa8f3e80b0dc4ce)

This dashboard includes:
- 📋 Full production schedule (3-week breakdown)
- ✅ Task tracking
- 🧪 Shot and asset review status
- 🧠 Meeting notes and weekly check-ins
- 📦 References and design archive

---

## 📁 Pipeline Features

- ✅ **Config-driven folder structure** with codename & show code support
- ✅ **Studio-style file naming conventions** with version control
- ✅ **Shot and asset registration** into an SQLite database
- ✅ **Validation tools** for folder structure and file names
- ✅ **Dockerized environment** for consistent dev/prod workflows
- ✅ **Makefile automation** for all operations
- ✅ **Progress tracking & production scheduling**

---

## 🛠️ Usage

### ✅ Basic Workflow

```bash
# Generate env variables from config
make generate-env

# Initialize project structure (dev or prod)
make dev-init         # or make prod-init

# Register assets and shots in the database
make dev-register

# Validate naming conventions and folder structure
make dev-validate

# Launch an interactive shell inside the container
make dev-bash
```

You can swap `dev-` with `prod-` for the production environment.

---

### 🧹 Reset the Project (Danger Zone)

```bash
make prod-reset
```

> Deletes and regenerates the entire project directory and database using the production config. Use with care.

---

## 🗂️ Folder Structure Example

```
TLK/
├── database/
│   └── pipeline.db
├── preproduction/
│   ├── references/
│   ├── storyboards/
│   └── designs/
│       └── characters/
│           └── poku/
│               └── exports/
├── production/
│   ├── assets/
│   │   ├── characters/
│   │   ├── props/
│   │   └── environments/
│   └── shots/
│       ├── sh001/
│       ├── sh002/
│       └── ...
└── renders/
    └── previews/
```

---

## 📦 File Naming Convention

```bash
[SHOW_CODE]_[SEQUENCE]_[SHOT]_[TYPE]_v[VERSION].[EXT]
```

| Component     | Example                 |
|---------------|-------------------------|
| `SHOW_CODE`   | `TLK`                   |
| `SEQUENCE`    | `SQ01`                  |
| `SHOT`        | `SH001`                 |
| `TYPE`        | `anim`, `model`, etc.   |
| `VERSION`     | `v001`                  |
| `EXT`         | `blend`, `kra`, etc.    |

---

## 🧪 Validation & Registration

The pipeline validates:
- Folder naming (e.g., shots, assets, exports)
- File versions and naming compliance
- Missing or invalid paths

It also registers all shots and assets into a SQLite database for tracking.

---

## 📆 Production Schedule

- **Start Date:** April 15, 2025
- **End Date:** May 5, 2025  
_(with optional review buffer until May 9)_

The production schedule is broken into 3 weekly phases:
1. **Pre-Production** – Storyboarding, design
2. **Production** – Modeling, rigging, layout
3. **Post** – Animation, lighting, rendering, compositing

🗓️ Live schedule: [See on Notion](https://stump-principle-4a6.notion.site/Tuulekra-1d4c1e24aece80a19fa8f3e80b0dc4ce)

---

## 🔁 Daily Syncs & Check-Ins

We use a dedicated Discord channel `#tuulekera-dailies` for:
- Daily updates
- Work in progress posts
- Quick reviews and planning

---

## 🔐 Codename Policy

To keep the production clean and modular, the internal pipeline uses:

- `Tuulekera` as the **codename**
- `TLK` as the **show code**
- `Poku Ärkab` as the **project title**

This helps maintain separation between pipeline logic and creative identity.

---

## 📬 Contact


**Pipeline TD / Director**  
Sreyeesh Garimella  
✉️ [GitHub](https://github.com/Sreyeesh)  
🗨️ Join the discussion on Discord: [discord.gg/xFc4akCC](https://discord.gg/xFc4akCC)
