# State Machines

A state machine is like a flowchart that shows how something changes from one situation (called a *state*) to another.

Example: think about a traffic light.

- It has three states: **green**, **yellow**, and **red**.
- It only changes in certain ways:

  - Green → Yellow
  - Yellow → Red
  - Red → Green

The machine “remembers” which state it’s in and changes only when something tells it to — like a timer or a button.

You can think of it as a set of *rules* that say:

- “If I’m in this state, and this happens, move to that state.”

Computers use state machines to keep track of what they’re doing — for example, whether a game character is *walking*, *jumping*, or *falling*.

## Example Code

Below is a simple example of a state machine implemented in Python:

```{literalinclude} ./python_files/state_machine.py
:linenos:
```
