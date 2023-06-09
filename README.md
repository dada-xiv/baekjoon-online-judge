# Baekjoon Online Judge

This is a personal repository that solves [Baekjoon Online Judge](https://www.acmicpc.net) problems and records the source codes.

## Python (configuration)

To configure *launch.json* in VS Code for running a Python script with input from a file named "input.txt" and output to the console, we may use the following setup:

```json
{
    "name": "Python: Debug with input.txt",
    "type": "python",
    "request": "launch",
    "program": "${file}",
    "console": "integratedTerminal",
    "args": ["<", "input.txt"],
    "justMyCode": true
}
```
