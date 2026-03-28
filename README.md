# Airflow Agent Skills PoC

This is a small Proof of Concept (PoC) built for the **Airflow Contribution & Verification Agent Skills** GSoC project.

## What this PoC does

The idea here is simple — represent common contributor workflows (like running tests or static checks) as reusable "skills", and execute them differently depending on the environment.

For example:
- On local machine → run normal commands
- Inside Breeze → use Breeze commands

## Why this matters

In Airflow, contributors often switch between local setups and Breeze. This PoC explores how an agent can handle that automatically by choosing the correct command based on context.

## What’s implemented

- Basic skills:
  - Run tests
  - Run static checks
- Context-aware execution:
  - `local`
  - `breeze`
- Simple simulation of how an agent would use these skills

## How it works

- `skills.py` contains the core logic (each skill returns a command)
- `main.py` simulates how an agent would call these skills

## How to run

```bash
python main.py
```
