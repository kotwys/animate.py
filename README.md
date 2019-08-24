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
rendered. It's represented with a class inherited from `Graphics`.

`Graphics` subclasses can contain their data as any other class.
Properties are stored in `props` attribute by default.
State should be initialized in a constructor for the first frame.
Class may define a `update(delta)` method which is then called every
frame with the delta time that equals to 1 / FPS.

`draw()` function is required. It creates an image for the current
frame after `init()` or `update()` is called.

Class must be passed as a first positional paramater of `register()`.

By default sequence longs 1 frame and accepts any props.
`register()` parameters allows to adjust it. To define an animation
you need to specify both `duration` (in seconds) and `fps`. Schema
is a [Python Schema](https://github.com/keleshev/schema) which
validates the provided [properties](#options) before execution.

Examples may be found in [examples folder](examples)
