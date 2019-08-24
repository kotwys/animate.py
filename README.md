# animate.py

Utility to create motion graphics with Python scripts.
It uses [Wand](http://wand-py.org) to generate images.

## Usage

```shell
main.py [options] <script> [-o <output>]
```

- `script` is a Python script to use.
- `-o <output>` specifies output directory. It has to be a printf-style
string with single number input for frame. By default it renders to
`./render/%03d.png` relative to working directory.

### Options

- `--props=<value>` JSON encoded properties for graphics. If script
declares a schema input will be validated against it.

## Scripts

Scripts define how animation's state is changing and how it should be
rendered.

*State* may be anything. It is optional and will be `None` unless
`init()` is defined. `init()` takes [props](#options) and creates a new state
which later will be updated in `update()`. Any of the state functions
is optional.

`draw()` function is required. It takes a state and produces a
`wand.image.Image` for it.

By default animation longs 1 frame and accepts any props.
`register` hook allows to adjust it. To define multiframe animation
you need to specify both `duration` (in seconds) and `fps`. Schema
is a [Python Schema](https://github.com/keleshev/schema) which
validates the provided [properties](#options) before execution.

Examples may be found in [examples folder](examples)
