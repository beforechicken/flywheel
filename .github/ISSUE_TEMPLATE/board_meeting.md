name: Board Meeting Agenda & Minutes
description: Prepare agenda and capture resolutions
title: "Board Meeting: YYYY-MM-DD"
labels: ["board"]
body:
  - type: markdown
    attributes:
      value: "## Agenda"
  - type: textarea
    id: agenda
    attributes:
      label: Agenda items
      placeholder: "- Item 1\n- Item 2"
  - type: textarea
    id: resolutions
    attributes:
      label: Proposed Resolutions
      placeholder: "- R1: ...\n- R2: ..."
  - type: textarea
    id: conflicts
    attributes:
      label: Conflicts Declared
      placeholder: "List declared conflicts and management approach"
