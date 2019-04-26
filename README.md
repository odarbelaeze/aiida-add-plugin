# aiida-add-plugin

This is a plugin for the AiiDA add program.

## Usage

For a quick and easy run:

```bash
./bin/bootstrap.sh
verdi run examples/launch.py
```

## Manual usage

### Installing the plugin python package

You can install the present plugin by:

```bash
# Modify this to activate your preferred virtual environment
git clone https://github.com/odarbelaeze/aiida-add-plugin.git
cd aiida-add-plugin
pip install -e .
```

### Installation of the code

You need to setup the `add` code, this repo provides a static binary file that
works on any linux machine the path for the code is `bin/add`.

The `bin/bootstrap.sh` file sets up the code in your aiida installation, but you
can do it with the following command:

```bash
verdi code setup \
    --non-interactive \
    --label add \
    --on-computer \
    --computer localhost \
    --remote-abs-path $PWD/bin/add \
    --input-plugin add.calculation
```

### Running a simple calculation

This is, to the best of my knowledge, the minimal code you need to write to run
a calculation using this plugin.

```python
code = load_code(label="add@localhost")
calculation = CalculationFactory("add.calculation")

builder = calculation.get_builder()
builder.code = code
builder.x = Float(3.0)
builder.y = Float(3.5)

builder.metadata.options = {"resources": {"num_machines": 1}}

results, node = run.get_node(builder)
print(results, node, sep="\n")
```

## Links of interest

- Lattest aiida develop: [aiida develop]
- `add` program source code: [add repo]


[aiida develop]: https://github.com/aiidateam/aiida_core
[add repo]: https://github.com/odarbelaeze/add-rs
