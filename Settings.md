---
AutoNoteMover: disable
---
# Vault Settings Overview

## Introduction
This guide details the settings applied to the current Vault.

## Structural Evolution
Obsidian's Graph feature stands out, making it superior to the traditional folder system. To simplify and optimise organisation, many folders have been removed or renamed, with a greater emphasis on Tags. For detailed changes, see the [[Release Notes]].

# General Settings

## Editor
- Display Frontmatter: Enabled

## File & Link Preferences
- **New Notes**: Default location - "Data"
- **New Attachments**: Default location - "Annex/Attachments"

## Visual Preferences
- **Theme**: "Things". Check it out [here](https://github.com/colineckert/obsidian-things).

# Plugins in Use

## Core Plugins
- **Daily Notes**: Disabled
- **Template**: Files stored in "Annex/Templates"

## Community Plugins

**1. Auto Note Mover**:
Automatically moves notes to relevant folders based on specific tags or file names. 
- [Plugin Info & Download](https://github.com/farux/obsidian-auto-note-mover)
- **Settings**:
   - Tag-based Moves:
     - `#MoC` to "Atlas"
     - `#Archived` to "Archives"
     - `#Reference/Web` to "References"
     - And more...
   - File Name-based Moves:
     - "Project" files to "Data"

**2. Dataview**: 
Allows vault queries similar to SQL and generates a Map of Contents.
- [Plugin Info & Download](https://github.com/blacksmithgu/obsidian-dataview)

**3. Editing Toolbar**: 
Facilitates a smoother transition for users from platforms like 'Microsoft Word'.
- [Plugin Info & Download](https://github.com/cumany/obsidian-editing-toolbar)

**4. GPT Plugin**:
- [Plugin Info & Download](https://github.com/jmilldotdev/obsidian-gpt)
- **Important**: An OpenAI Key is required.

**5. Natural Language Dates**:
Handles dates in a more intuitive way.
- [Plugin Info & Download](https://github.com/argenos/nldates-obsidian)

**6. Obsidian Git**: 
Automatically backs up changes to a Git Repository. Note: Default settings are active.
- [Plugin Info & Download](https://github.com/denolehov/obsidian-git)

**7. Tasks**: 
Efficiently manage tasks throughout the Vault.
- [Plugin Info & Download](https://obsidian-tasks-group.github.io/obsidian-tasks/)

**8. Text Generator**: 
Generates content using GPT-4.
- [Plugin Info & Download](https://github.com/nhaouari/obsidian-textgenerator-plugin)
- **Note**: You'll need your OpenAI Key. 
- **Settings**: Model - GPT4, Max Tokens - 1000, Temperature - 0.9, Frequency Penalty - 0.1

