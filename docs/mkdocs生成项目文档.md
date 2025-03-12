<<<<<<< HEAD
## mkdocs生成项目文档

`Mkdocs`是一个使用Python编写的文档生成工具，用于快速构建项目文档网站。它的重点在于使用简单的Markdown文件构建网站，以便开发人员可以快速开发和维护文档。 `Mkdocs`可以从多个源文件中构建网站，可以从Github、Gitlab、Bitbucket等多个版本控制系统上读取文件，也可以从网络上读取文件。另外，它还提供了一些丰富的主题，以及可以自定义生成网站的功能，这些功能使Mkdocs成为构建项目文档网站的理想工具。

使用Mkdocs生成项目文档的步骤如下：

1. 安装Mkdocs：使用pip安装Mkdocs，命令如下：

```
pip install mkdocs
pip install mkdocs-material
```

2. 创建项目文件夹：使用与项目相关的名称创建一个新的文件夹，该文件夹将用作项目文档的文件夹。

3. 初始化项目：使用Mkdocs init命令初始化项目，命令如下：

```
mkdocs init
```

初始化后，会在文件夹中生成一个mkdocs.yml文件，该文件用于配置文档网站的相关参数。

4. 创建文档：在文件夹中创建Markdown文件，用于存储项目文档。

5. 生成项目文档：使用以下命令生成项目文档：

```
mkdocs build
```

6. 查看文档：使用以下命令在本地服务器上查看文档：

```
mkdocs serve
```

这样，就可以在浏览器中查看文档，查看本地生成的项目文档网站。

#### 下载.git文件并放入mkdocs文件夹

```
git clone git@github.com:xiaopch/xiaopch.github.io.git
```

#### 上传至github的page空间

```
mkdocs gh-deploy
```
=======
## mkdocs生成项目文档

`Mkdocs`是一个使用Python编写的文档生成工具，用于快速构建项目文档网站。它的重点在于使用简单的Markdown文件构建网站，以便开发人员可以快速开发和维护文档。 `Mkdocs`可以从多个源文件中构建网站，可以从Github、Gitlab、Bitbucket等多个版本控制系统上读取文件，也可以从网络上读取文件。另外，它还提供了一些丰富的主题，以及可以自定义生成网站的功能，这些功能使Mkdocs成为构建项目文档网站的理想工具。

使用Mkdocs生成项目文档的步骤如下：

1. 安装Mkdocs：使用pip安装Mkdocs，命令如下：

```
pip install mkdocs
pip install mkdocs-material
```

2. 创建项目文件夹：使用与项目相关的名称创建一个新的文件夹，该文件夹将用作项目文档的文件夹。

3. 初始化项目：使用Mkdocs init命令初始化项目，命令如下：

```
mkdocs init
```

初始化后，会在文件夹中生成一个mkdocs.yml文件，该文件用于配置文档网站的相关参数。

4. 创建文档：在文件夹中创建Markdown文件，用于存储项目文档。

5. 生成项目文档：使用以下命令生成项目文档：

```
mkdocs build
```

6. 查看文档：使用以下命令在本地服务器上查看文档：

```
mkdocs serve
```

这样，就可以在浏览器中查看文档，查看本地生成的项目文档网站。

#### 下载.git文件并放入mkdocs文件夹

```
git clone git@github.com:xiaopch/xiaopch.github.io.git
```

#### 上传至github的page空间

```
mkdocs gh-deploy
```
>>>>>>> ee0de038a932e9888ffa0b60c04e3c6a89d7d464
