# JINJA STATIC SITE GENERATOR

Simple CLI static site generator to convert a directory of Jinja template files
into an output directory as html files.


## USAGE

Basic usage is:

```shell
staticyah INPATH OUTPATH
```

Assume you have this structure:

```
- site/
  - tpl/
    - foo.html.jinja
    - bar/
      - abc.html.jinja
      - _somepartial.html.jinja
  - staticyah_out/
```

`INPATH` will be `./site/tpl` and `OUTPATH` will be `./site/staticyah_out`.

You can convert all files with:

```shell
staticyah ./site/tpl ./site/staticyah_out
```

This will create this driectory structure for `OUTPATH`:

```
- site/
  - staticyah_out/
    - foo.html
    - bar/
      - abc.html
```


## WARNINGS

When you run `staticyah` command, the following files/directories under
the `OUTPATH` directory will be removed:

- Any files ending with `.html`, but not beginning with `.`
- Any empty directories


## RULES

- The directory at `OUTPATH` must be named `staticyah_out`
- Any files under `INPATH` which begin with `_` are considered partials,
  and are only meant to be included in templates.  They are not converted
  as standalone files.
- Only files under `INPATH` with the following extensions will be converted:
  - `.html.jinja`
  - `.html.j2`
  - `.html.j2`
- `INPATH` and `OUTPATH` cannot be symbolic links
- `INPATH` and `OUTPATH` cannot be subdirectories of each other
- The `staticyah` cannot be run from a subdirectory of `OUTPATH`
- User running the `staticyah` command must have write access to `OUTPATH`.
- User running the `staticyah` command must have read access to `INPATH`.
