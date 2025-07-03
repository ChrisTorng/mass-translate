This is another test Markdown file.

This paragraph is for testing purposes.

```md
# This is a sample code snippet.
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": USER_PROMPT_TEMPLATE.format(text=text)}
```

The `role` field in the messages indicates the type of participant in the conversation. It can be either `user` or `system`.
