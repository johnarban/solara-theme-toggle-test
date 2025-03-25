# ThemeToggle Component Initial State Matrix

| enforce_default | default_to_server | enable_auto | default_theme | server_setting | Result              |
|-----------------|-------------------|-------------|---------------|----------------|---------------------|
| True            | True              | True/False  | *             | light          | Light mode          |
| True            | True              | True/False  | *             | dark           | Dark mode           |
| True            | False             | True/False  | "dark"        | light/dark     | Dark mode           |
| True            | False             | True/False  | "light"       | light/dark     | Light mode          |
| True            | False             | True/False  | "auto"/None   | light/dark     | System preference   |
| False           | True              | True        | *             | light          | System preference   |
| False           | True              | True        | *             | dark           | System preference   |
| False           | True              | False       | "dark"        | light          | Light mode          |
| False           | True              | False       | "dark"        | dark           | Dark mode           |
| False           | True              | False       | "light"       | light          | Light mode          |
| False           | True              | False       | "light"       | dark           | Dark mode           |
| False           | True              | False       | "auto"/None   | light          | Light mode          |
| False           | True              | False       | "auto"/None   | dark           | Dark mode           |
| False           | False             | True        | *             | light/dark     | System preference   |
| False           | False             | False       | "dark"        | light/dark     | Dark mode           |
| False           | False             | False       | "light"       | light/dark     | Light mode          |
| False           | False             | False       | "auto"/None   | light/dark     | System preference   |

## UI Behavior:
- When enable_auto = True: Toggle cycles through Dark → Light → Auto
- When enable_auto = False: Toggle cycles through Dark → Light only

```mermaid
graph TD
    A[Start] --> B{enforce_default?}
    
    B -->|Yes| C{default_to_server?}
    B -->|No| D{enable_auto?}
    
    C -->|Yes| C1[Use server setting]
    C -->|No| C2{default_theme?}
    
    C2 -->|"dark"| C3[Dark mode]
    C2 -->|"light"| C4[Light mode]
    C2 -->|"auto"/None| C5[System preference]
    
    D -->|Yes| D1[System preference]
    D -->|No| D2{default_to_server?}
    
    D2 -->|Yes| D3{server_setting?}
    D2 -->|No| D4{default_theme?}
    
    D3 -->|light| D5[Light mode]
    D3 -->|dark| D6[Dark mode]
    
    D4 -->|"dark"| D7[Dark mode]
    D4 -->|"light"| D8[Light mode]
    D4 -->|"auto"/None| D9[System preference]
```
