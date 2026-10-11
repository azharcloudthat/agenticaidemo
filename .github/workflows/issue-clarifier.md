---
on:
  issues:
    types: [opened]
permissions: read-all
engine:
  id: copilot
  model: gpt-5
safe-outputs:
  add-comment:
---

# Issue Clarifier

Analyze the current issue and ask for additional details if the issue is unclear.