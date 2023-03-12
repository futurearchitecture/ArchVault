---
AutoNoteMover: disable
---


# Introduction
This document contains the setting for this Vault.

# Options

## Editor
- Show Frontmatter = Yes 

## Files & Links

### Default Location for new Notes
- Dropdown  = In the folder specified below
	- Folder to create new notes in = 0 - Inbox

### Default Location for New Attachments
- Dropdown  = In the folder specified below
	- Attachment Folder Path = [100 - References/_Attachments] 


### Appearance
- Themes = Things - [GitHub - colineckert/obsidian-things: An Obsidian theme inspired by the beautifully-designed app, Things.](https://github.com/colineckert/obsidian-things)


# Core Plugins
- Daily Notes = off

- Template
	- Template Folder Location = '100 - References/_Templates'


# Community Plugins
These are the Plugins that are installed with this Vault. It is recommend to run an update after opening this Vault in Obsidian.

## Auto Note Mover

Once a specific hash tag is applied a note is automatically moved to the appropriate folders.

https://github.com/farux/obsidian-auto-note-mover

### Settings

The Auto Mover plugin moves files to a specific location when a tag is assigned.

| Tag | Folder | 
|---|---|
| #MoC   |0 - Atlas    |
| #Archived | 1000 - Archives|
| #Reference/Web | 100 - References |
| #Tasks| 900 - Tasks |
|#Standards      | 200 - Standards |

The Auto Mover plugin moves files to a specific location when text in the file name matches.

| File Name | Folder |
| --- | --- |
| Project | 10 - Projects | 


## Dataview

Dataview is a query the vault using a language very similar to SQL. Dataview is used to generate the content of the Map of Contents

https://github.com/blacksmithgu/obsidian-dataview


## Editing Toolbar

Markdown and Obsidian can both have steep learning curves. Having a 'Microsoft Word' style toolbar can help ease these learning curve. 

[GitHub - cumany/obsidian-editing-toolbar: An obsidian toolbar plugin, modified from the Cmenu plugin](https://github.com/cumany/obsidian-editing-toolbar)


## GPT 

https://github.com/jmilldotdev/obsidian-gpt

*Please note you will need to obtain your own OpenAI Key for this plugin to work*


## Natural Language Dates

[argenos/nldates-obsidian: Work with dates in natural language in Obsidian (github.com)](https://github.com/argenos/nldates-obsidian)




## Obsidian Git

This Plugin will save what has changed to a Git Repo.

**Please Note** - that the default settings are in place.

https://github.com/denolehov/obsidian-git


## Tasks

Manage Tasks across the Vault 

https://obsidian-tasks-group.github.io/obsidian-tasks/


## Text Generator

[nhaouari/obsidian-textgenerator-plugin: Text generator is a handy plugin for Obsidian that helps you generate text content using GPT-3 (OpenAI). (github.com)](https://github.com/nhaouari/obsidian-textgenerator-plugin)

*Please note you will need to obtain your own OpenAI Key for this plugin to work*

Model - text-davinci-003
Max Tokens - 1000
Tempature - 0.9
Frequency Penalty - 0.1

