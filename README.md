# IS 219-002 Midterm
## Matthew LiDonni - Spring 2024

**Setup**
1. Clone or download the repository.
2. In the terminal go into the cloned repository and create the virtual environment.<br>`python -m venv venv`
3. Enable the virtual environment.<br>`source venv/bin/activate`
4. Download the requirements with PIP. <br> `pip3 install -r requirements.txt`
5. Start the program with `python3 main.py`

**Commands**
- `add <value> <value>` - Adds two or more values numeric values
- `subtract <value> <value>` - Subtracts two or more values numeric values
- `multiply<value> <value>` - Multiplies two or more values numeric values
- `divide <value> <value>` - Divides two or more values numeric values
- `menu` - Gets a list of all the currently available commands
- `exit` - Exits the program
- `history <show|last|clear|save|load>`
	- `show` - Show the currently stored history
	- `last` - Get the last performed operation
	- `clear` - Clears the currently stored history
	- `save` - Saves the currently stored history to history.csv in the path defined in .env for HISTORY_DIR.
	- `load` - Loads saved history into the current history from history.csv in the path defined in .env for HISTORY_DIR.

**Documentation**

App: 	
- Functions
	- **\_\_init__:** Loads environment variables, creates cli (app.cli - CLI), sets up logger, and loads all plugins for the program.
	- **logging_setup**: Configure logger to write to defined path at LOG_DIR in .env
	- **load_plugins**: Loads all plugins from a destination defined at PLUGIN_DIR in .env
	- **start**: Begins CLI runtime loop
- Properties:
	-  **app.cli**: The applications CLI instance

**Environment Variable Configuration:**
- CURSOR: Customizes the CLI cursor, leave out for default ">>> "
  	- Example `CURSOR="app$ "`
- LOG_DIR: Required, path to store log files, will attempt to create the directory if it does not exist. Default is "logs"
	- Example: `LOG_DIR = "logs"`
- HISTORY_DIR: Required, path to save and load calculation history data from. Default value is "app/data".
	- Example: `HISTORY_DIR = "app/data"`
- PLUGIN_DIR: Required, path to the plugins directory. Default value is "app/plugins" but can be changed if necessary.
	- Example: `PLUGIN_DIR="app/plugins"`
- CURSOR: Optional, defines a different cursor for prompting the user on the CLI. Leaving blank will default to ">>> "
	- Example: `CURSOR="app>"`

**Implementation**

Abstract Factory:
- https://github.com/mjl62/is219-midterm/blob/df33e94414d2f633649be2aa5614e5eb45d7ea5d/app/cli/__init__.py#L7-L18
	- Using an abstract class with abstract methods we are able to have plugins with the same methods but different results. Since they all have a .run() function and they're all Command classes, we can call these methods even if we arent sure what the classes will be because they must have these methods defined.

Builder:
- https://github.com/mjl62/is219-midterm/blob/df33e94414d2f633649be2aa5614e5eb45d7ea5d/app/calculator/__init__.py#L143-L153
	- Multiple methods here I believe qualify for this, but they all take arguments, pass them through a set of instructions to create a new object, then return a new one created from the original arguments.

How Environment Variables were used:
- https://github.com/mjl62/is219-midterm/blob/df33e94414d2f633649be2aa5614e5eb45d7ea5d/app/__init__.py#L30-L49
- https://github.com/mjl62/is219-midterm/blob/df33e94414d2f633649be2aa5614e5eb45d7ea5d/app/cli/__init__.py#L40-L49
- https://github.com/mjl62/is219-midterm/blob/df33e94414d2f633649be2aa5614e5eb45d7ea5d/app/calculator/__init__.py#L147-L149
- I mostly used environment variables for allowing the user to change file locations such as logging locations, history.csv locations, and plugin locations, however I also added the ability to change the CLI cursor if required. The .env is preconfigured to work with the program as is, but I think allowing this kind of flexibility is worth having.


Try/Catch/Except:
- https://github.com/mjl62/is219-midterm/blob/5c28195af73579d6453bac31279ecca9e279349a/app/cli/__init__.py#L43-L49
	- In this instance I used a try/catch to get a value from the environment variables, but catch the error if it doesn't exist and move forward with the default setting.
 - https://github.com/mjl62/is219-midterm/blob/5c28195af73579d6453bac31279ecca9e279349a/app/plugins/basic_operations/__init__.py#L83-L97
 	- In this one I used a mix of both LBYL and EAFP to handle multiple possible scenarios. It looks at the args to determine if there's any values, then if not it returns instantly, not going through with the process. However, if it gets an invalid value but does still get values then it catches the errors and handles those accordingly.


--------------------------------------------------------------------

### TODO FOR SUBMISSION: 
- [ ] Documentation, configuration examples, commit history
- [ ] Project description
- [ ] Link implementations of design patterns
- [ ] Description of environment variables and link to code to illustrate.
- [ ] Explain and link to how logging is being used
- [ ] Link and explain try/catch / exception handling for LBYL and EAFP implementation.
- [ ] 3-5 minute video demonstration of key features and functionality, link video in README file
- [ ] Make repo public before submission.
- [ ] Submit link to repo on Canvas
- [x] Create repo from scratch

### Feature progress:
- [ ] CLI
    - [ ] Read-Eval-Print-Loop (REPL) interface
	- [x] Add, Subtract, Multiply, Divide commands
	- [ ] Manage Calculation History
	- [x] Access extended functionality through dynamically loaded plugins
- [ ] Plugin System
	- [x] Dynamically load plugins to integrate new commands without altering code of program
	- [x] Include a "Menu" command to list all available plugin commands
- [ ] Calculation History Management with Pandas
	- [ ] Reading and writing to CSV
	- [ ] Load, save, delete and clear history records through REPL interface
- [ ] Professional Logging Practices
	- [ ] Detailed application operations, data manipulations, errors, and info messages.
	- [ ] Differentiate by severity for effective monitoring.
	- [ ] Dynamic logging configuration through environment variables for levels and output destinations.
- [ ] Design Patterns for Scalable Architecture
	- [ ] Facade Pattern: Offer simplified interface for complex pandas data manipulations
	- [x] Command Pattern: Structure commands within REPL for effective calculation and history management.
	- [ ] Factory Method, Singleton and Strategy Patterns: Further enhance applications code structure, flexibility and scalability
### Development, testing and documentation
- [ ] Testing/Quality
	- [ ] Minimum 90% coverage with Pytest
	- [ ] Ensure quality and adherence to PEP 8, verified by Pylint.
- [ ] Version control
	- [ ] Commits are logical, group feature development and corresponding tests.
- [ ] Comprehensive documentation
	- [ ] Detailed README with documentation covering
		- [ ] Setup instructions
		- [ ] Usage examples
		- [ ] In depth analysis of architectural decisions, emphasizing the implementation and impact of chosen design patterns and the logging strategy.
