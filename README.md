# YAST
Yet Another Scripting Tetorial tex build. Uses Tex Live and Pygment.

## Installation
The following assumes you are using linux or WSL.

### Update apt.

```bash
sudo apt update
```

### Ensure that you have Python installed.

```bash
sudo apt install python3
```

For convenience you may want:

```bash
sudo apt install python-is-python3
```

### Install Tex Live (~8 GB for everything).
You could be more selective if you want.

```bash
sudo apt install texlive-full
```

### Install pygments plugin.
```bash
python -m venv venv/
venv/vin/pip install .
```

If you update the plugin, you need to reinstall it.

### Configure your environment

I recommend using VS Code with LaTeX Workshop plugin. This will let you auto-compile the output file on save.

In your VS Code `settings.json`, add the following configurations to the root object. The `-shell-escape` option is very important.

```json
"latex-workshop.latex.tools": [
    {
        "name": "latexmk (shell escape)",
        "command": "latexmk",
        "args": [
            "-synctex=1",
            "-shell-escape",
            "-interaction=nonstopmode",
            "-file-line-error",
            "-pdf",
            "-outdir=%OUTDIR%",
            "%DOC%"
        ],
        "env": {
            "PYGMENTIZE": "path/to/project/venv/bin/pygmentize"
        }
    }
],
"latex-workshop.latex.recipes": [
    {
        "name": "latexmk (shell escape)",
        "tools": [
            "latexmk (shell escape)"
        ]
    }
],
"latex-workshop.latex.recipe.default": "latexmk (shell escape)",
"latex-workshop.latex.autoBuild.run": "onFileChange",
```

The `PYGMENTIZE` environment variable is supposed to tell latexmk where to find the pygmentize executable, but latexmk can call pdflatex and it won't pass this environment variable with it. I'm not exactly sure what is the best way to address this.

The bottom line is latexmk and pdflatex need to be able to access the pygmentize executable located in `venv/bin` and select it over other versions of pygmentize that may be in your path variable. An easy, bad solution is to add `.../venv/bin` to your path.
