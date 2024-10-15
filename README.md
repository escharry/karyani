<div align="center">
<pre>
 █████                                                           ███ 
░░███                                                           ░░░  
 ░███ █████  ██████   ████████  █████ ████  ██████   ████████   ████ 
 ░███░░███  ░░░░░███ ░░███░░███░░███ ░███  ░░░░░███ ░░███░░███ ░░███ 
 ░██████░    ███████  ░███ ░░░  ░███ ░███   ███████  ░███ ░███  ░███ 
 ░███░░███  ███░░███  ░███      ░███ ░███  ███░░███  ░███ ░███  ░███ 
 ████ █████░░████████ █████     ░░███████ ░░████████ ████ █████ █████
░░░░ ░░░░░  ░░░░░░░░ ░░░░░       ░░░░░███  ░░░░░░░░ ░░░░ ░░░░░ ░░░░░ 
                                 ███ ░███                            
                                ░░██████                             
                                 ░░░░░░                              
---------------------------------------------------
python cli program to manage tasks
</pre>

[![PyPI](https://img.shields.io/pypi)](https://pypi.org/project/karyani/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

Not enough CLI tools? Here's another one! karyani is a Python program that helps manage your tasks in the terminal.

## Installation

pip install this repo.

```sh
pip3 install karyani
```

(or)

```sh
pip install karyani
```

## Usage example

### To get help with commandline arguments

```sh
karyani --help
```

### Adding a task

```sh
karyani add "Buy groceries" --due "2024-10-15" --priority "high"
```

### List all tasks

```sh
karyani list
```

### Filter tasks by priority

```sh
karyani list --priority "high" // or karyani list -p "high"
```

### Filter task by status (completed, pending)

```sh
karyani list --status "completed" // or karyani list -s "completed"
```

### Mark a task as done by its id

```sh
karyani complete 1
```

### Edit a task

```sh
karyani update "Buy groceries and wash car" --due "2024-10-17" --priority "low"
```

### Clear a task

```sh
karyani clear 1
```

### Clear all completed tasks

```sh
karyani clear
```

### Clear all tasks

```sh
karyani clear -a // or karyani clear --all
```

## Development setup

Clone this repo and install packages listed in requirements.txt

```sh
pip3 install -r requirements.txt
```

---

Esteban Charry – echarry@berkeley.edu

Distributed under the MIT license. See `LICENSE` for more information.

[https://github.com/escharry/](https://github.com/escharry/)

## Contributing

1. Fork it (<https://github.com/escharry/karyani/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
