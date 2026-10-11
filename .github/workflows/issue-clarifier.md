---
on:
  issues:
    types: [opened]
permissions:
  copilot-requests: write
  issues: read
engine:
  id: copilot
  model: gpt-5
safe-outputs:
  add-comment:
---

# Issue Clarifier

Analyze the current issue and ask for additional details if the issue is unclear.

permissions:
  copilot-requests: write
  issues: write