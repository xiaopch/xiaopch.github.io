# Create your site - Zensical Documentation

[Zensical Documentation](https://zensical.org) > Create your site

---

[Introducing **Zensical Studio** – Refactor documentation like code.](https://zensical.org/studio)

## Create your site

After you've [installed](../get-started/) Zensical, you can bootstrap your project documentation using the `zensical` executable. Go to the directory where you want your project to be located and enter:

```
zensical new .
```

This creates the following structure:

```
.
├─ .github/workflows
│  └─ docs.yml
├─ docs/
│  ├─ index.md
│  └─ markdown.md
└─ zensical.toml
```

To learn more about the specific files and directories that are generated for you, please consult the usage guide for the [`new` command](../usage/new/#usage).

## Configuration

Zensical comes with many [configuration options](../setup/basics/) that have sensible defaults, which allows to build a documentation site with almost no configuration. [`site_name`](../setup/basics/#site_name) is the only required setting[^1]:

```toml
[project]
site_name = "My site"
```

Unless you're building documentation for [offline usage](../setup/offline/), it's strongly recommended to specify the [`site_url`](../setup/basics/#site_url) setting as well, since it's a prerequisite for the following features:

- [Instant navigation](../setup/navigation/#instant-navigation)
- [Instant previews](../setup/navigation/#instant-previews)
- [Custom error pages](../customization/#custom-error-pages)

## Preview as you write

### Zensical Studio

[Zensical Studio](https://zensical.org/studio) brings workspace intelligence to **Zensical** and **MkDocs projects** and integrates with Visual Studio Code and similar editors[^2]. It gives you a synchronized side-by-side view of your Markdown source and rendered documentation, with the preview updating as you write:

### Zensical

Zensical includes a web server, so you can preview your documentation site as you write. The server will automatically rebuild the site when you make changes to source files. Start it with:

```
zensical serve
```

Point your browser to [localhost:8000](http://localhost:8000) and you should see:

## Build your site

When you're finished editing, you can build a static site from your Markdown files with:

```
zensical build
```

The contents of this directory make up your project documentation. There's no need for operating a database or server, as it is completely self-contained. The site can be hosted on [GitHub Pages](../publish-your-site/#github-pages), a CDN of your choice or your private web space.

If you intend to distribute your documentation as a set of files to be read from a local filesystem rather than a web server (such as in a `.zip` file), please consult the [offline usage](../setup/offline/) guide.

---

[^1]: [`site_name`](../setup/basics/#site_name) is currently required because MkDocs, the static site generator Zensical replaces, requires it. We plan to make this setting optional in a future release.
[^2]: Zensical Studio will be supported in more editors in the future, including JetBrains IDEs and Neovim.

---

- **Previous:** [Get started](../get-started/)
- **Next:** [Publish your site](../publish-your-site/)

© 2025 - 2026 Zensical LLC | Made with [Zensical](https://zensical.org/)
