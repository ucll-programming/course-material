# Overview

When running a script in debug mode, a number of buttons will appear at the top.

:::center
![Debugging toolbar](./toolbar.png)
:::

We discuss them from left to right:

* The Continue button resumes execution at full speed until another breakpoint is reached or your scripts ends.
* The Step Over button performs the highlighted line in one step.
  Use it when you're not interested in a step-by-step execution of the code on that line.
  For example, if the line contains a function call, you will not see what happens inside that function.
* The Step Into button allows you to see what happens inside functions.
* Say the debugger is currently inside some function `foo`.
  Step Out will resume execution at full speed until execution leaves the function `foo`.
  You will jump back to the location where `foo` was called.
* The Restart button... well, restarts.
* The Stop button aborts the execution of your script and ends the debugging session.

The debugger offers many other features, which we suggest you experiment with when you can:

* Conditional breakpoints: you can ask the debugger to only interrupt execution if some expression is true.
  Similarly, you can have a breakpoint activate only after execution got past it a certain number of times.
* You can use *watch expression* to view the value of certain expressions as execution proceeds.
  For example, adding `len(groups[0])` will show you the length of the first group; it will also be automatically updated as you step through the code.
* The current line can be part from some function `foo`, that was called by some other function `bar`, which in turn was called by still another function `qux`.
  This information will be visible in the Call Stack pane.

::::IMPORTANT
Note that this is nothing Visual Studio code or Python specific: these same debugger features are available for many languages and many editors/IDEs.
::::

While you're using the debugger to go through your code step by step in search of a bug, we strongly suggest you predict the outcome at every step.
If you don't, it's all too easy to let yourself passively accept that what you're shown is correct, causing you to overlook the error.

A debugger isn't a magic wand, it only shows what's happening.
Determining why it's happening is still your job.
