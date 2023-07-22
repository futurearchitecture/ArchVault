Tags: #Reference 

Reference: https://python.langchain.com/en/latest/modules/indexes/document_loaders/examples/obsidian.html

`Obsidian` files also sometimes contain [metadata](https://help.obsidian.md/Editing+and+formatting/Metadata) which is a YAML block at the top of the file. These values will be added to the document’s metadata. (`ObsidianLoader` can also be passed a `collect_metadata=False` argument to disable this behaviour.)


```
from langchain.document_loaders import ObsidianLoader

loader = ObsidianLoader("<path-to-obsidian>")

docs = loader.load()
```

