# aria2 Readme

aria2 is a **lightweight** multi-protocol & multi-source command-line
**download utility**. It supports **HTTP/HTTPS**, **FTP**, **SFTP**,
**BitTorrent** and **Metalink**. aria2 can be manipulated via built-in
**JSON-RPC** and **XML-RPC** interfaces.

## Download

Download [version 1.37.0](https://github.com/aria2/aria2/releases/tag/release-1.37.0).
There you can download source distribution and binaries for OS X, Windows and Android.

The legacy releases earlier than 1.19.1 are available
[here](https://github.com/aria2/aria2/releases).

## Features

- **Multi-Connection Download**.
  aria2 can download a file
  from multiple sources/protocols and tries to utilize your
  maximum download bandwidth. Really speeds up your download
  experience.

- **Lightweight**.
  aria2 doesn't require much memory and CPU time. When disk cache is
  off, the physical memory usage is typically 4MiB (normal
  HTTP/FTP downloads) to 9MiB (BitTorrent downloads). CPU usage in
  BitTorrent with download speed of 2.8MiB/sec is around 6%.

- **Fully Featured BitTorrent Client**.
  All features you want in BitTorrent client are available: DHT,
  PEX, Encryption, Magnet URI, Web-Seeding, Selective Downloads,
  Local Peer Discovery and UDP tracker.

- **Metalink Enabled**.
  aria2 supports The Metalink Download Description Format
  (aka [Metalink v4](http://tools.ietf.org/html/rfc5854)),
  [Metalink version 3](http://www.metalinker.org/) and
  [Metalink/HTTP](http://tools.ietf.org/html/rfc6249).
  Metalink offers the file verification, HTTP/FTP/SFTP/BitTorrent integration
  and the various configurations for language, location, OS, etc.

- **Remote Control**.
  aria2 supports RPC interface to control the aria2 process.
  The supported interfaces are JSON-RPC (over HTTP and WebSocket)
  and XML-RPC.

## Usage Examples

Command-line scares you off? No, aria2 is really easy to use!!

**Download from WEB:**

```bash
$ aria2c http://example.org/mylinux.iso
```

**Download from 2 sources:**

```bash
$ aria2c http://a/f.iso ftp://b/f.iso
```

**Download using 2 connections per host:**

```bash
$ aria2c -x2 http://a/f.iso
```

**BitTorrent:**

```bash
$ aria2c http://example.org/mylinux.torrent
```

**BitTorrent Magnet URI:**

```bash
$ aria2c 'magnet:?xt=urn:btih:248D0A1CD08284299DE78D5C1ED359BB46717D8C'
```

**Metalink:**

```bash
$ aria2c http://example.org/mylinux.metalink
```

**Download URIs found in text file:**

```bash
$ aria2c -i uris.txt
```

## Related Projects

- **apt-metalink**: Faster package downloads for Debian/Ubuntu
- **powerpill**: Pacman wrapper for parallel and segmented downloads.
- **python3-aria2jsonrpc**: A wrapper class around Aria2's JSON RPC interface.
- **[aria2.js](https://github.com/aria2/aria2.js)**: JavaScript (browsers and Node.js) library and cli for aria2 RPC

## UI Frontends

- **[webui-aria2](https://github.com/ziahamza/webui-aria2)**: Web browser interface for aria2 (2012 GSOC project)
- **[uGet](http://ugetdm.com/)**: the Linux Download Manager

## License

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or (at
your option) any later version.
