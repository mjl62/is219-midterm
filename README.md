# IS 219-002 Midterm
## Matthew LiDonni - Spring 2024

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
