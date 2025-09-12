name: Board Resolution Request
description: Request a formal resolution
title: "Resolution: <<Title>>"
labels: ["resolution"]
body:
  - type: textarea
    id: text
    attributes:
      label: Resolution text
      placeholder: "Resolved that ..."
  - type: input
    id: effective
    attributes:
      label: Effective date
