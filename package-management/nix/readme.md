# Nix Package Management

## Syntax

* create an dev environment with python3 and has OPENAI_API_KEY env variable and echoes upon running.

```
{ pkgs ? import <nixpkgs> {}
}:

pkgs.mkShell {
  name = "dev-environment";
  buildInputs = [
    pkgs.python3
  ];
  shellHook = ''
    echo "Starting dev environment..."
    export OPENAI_API_KEY="asjdhaskdjbnaskjdbnasjkdhn"
  '';
}
```

## Powerful Things You Could do With nIX
Nix is a powerful package manager for Linux and other Unix systems, which aims to ensure that all installations are reliable, reproducible, and isolated. Here are some cool tricks you can do with Nix:

* Install packages without root access: This is great for using software packages on shared systems where you don't have administrative rights. Just use the nix-env command to install packages in your home directory.

```
nix-env -iA nixpkgs.htop
```

* Per-Project Dependencies with nix-shell: Nix allows you to specify a shell that contains all the dependencies that your project needs. Here's an example shell.nix file:

```
{ pkgs ? import <nixpkgs> { } }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python3
    pkgs.python3Packages.requests
  ];
}
```

This specifies a shell where Python 3 and the requests library are available. You can enter the shell by running nix-shell.

Multi-user package management: Nix can maintain different sets of installed packages for different users of the system. This allows users to install and upgrade software without interfering with each other.

Rollback changes: Nix keeps track of all changes you've made and allows you to easily roll back to previous versions of installed packages.

```
nix-env --rollback
```

* Using Docker with Nix: Nix can be used with Docker to generate lean, reproducible Docker images. You can create a default.nix file to specify the Docker image, like so:

```
{ pkgs ? import <nixpkgs> {} }:
pkgs.dockerTools.buildLayeredImage {
  name = "my-docker-image";
  config.Cmd = [ "${pkgs.python3}/bin/python3" ];
}
```

* Then, build the Docker image with the nix-build command, and load it into Docker:

```
nix-build
docker load -i result
```

* Garbage collection: Nix allows you to clean up unused packages with its garbage collector. You can run it like so:

```
nix-collect-garbage -d
```

* NixOS configuration: If you're using NixOS, the whole system is configured through Nix. This allows you to have version-controlled, reproducible system configurations. Your whole system configuration is stored in /etc/nixos/configuration.nix.

* Binary Caching: Nix supports binary caching which means you can share binaries of your packages within your organization without having to compile them from scratch on every system.

## Cheatsheet
* To install a package:

```
nix-env -iA nixpkgs.packageName
```

* To remove a package:

```
nix-env -e packageName
```

* To search for a package:

```
nix-env -qaP packageName
```

* To update the list of packages:

```
nix-channel --update
```

* To upgrade all installed packages:

```
nix-env -u
```

* To rollback to the previous generation:

```
nix-env --rollback
```

* To list all installed packages:

```
nix-env -q
```

* To list all package generations:

```
nix-env --list-generations
```

* To switch to a specific generation:

```
nix-env --switch-generation <number>
```

* To remove unused packages:

```
nix-collect-garbage -d
```

* To start a new Nix shell with specific packages:

```
nix-shell -p packageName
```

* To build a Nix expression:

```
nix-build default.nix
```

Remember, Nix has a steep learning curve. Don't hesitate to consult the official Nix documentation or the man pages (man nix-env, man nix-build, etc.) when you're not sure about something.


## Running Nix Via the Package Manager

```sh
docker run -it nixos/nix
```

* Start nix package manager by exposing current working directory
```sh
mkdir workdir
docker run -it -v $(pwd)/workdir:/workdir nixos/nix
```

* Start nix by cloning

```sh
git clone --depth=1 https://github.com/NixOS/nixpkgs.git
docker run -it -v $(pwd)/nixpkgs:/nixpkgs nixos/nix
docker> nix-build -I nixpkgs=/nixpkgs -A hello
docker> find ./result # this symlink points to the build package
```


## Version and Rollback Management in NIX

In Nix, every time you make a change to your environment, such as installing or uninstalling a package with nix-env -i or nix-env -e, Nix creates a new generation of your user environment. Each generation is a snapshot of your environment at a certain point in time, including the list of installed packages.

The nix-env --rollback command allows you to revert your user environment to the previous generation. In other words, it undoes the most recent change you made with nix-env -i or nix-env -e.

For instance, if you installed a package with nix-env -i and it broke something or didn't behave as expected, you could quickly revert to the state before the package was installed with nix-env --rollback.

This command can be extremely handy as it allows you to experiment with different packages without worrying about causing irreversible damage to your environment. If something goes wrong, you can simply rollback.

If you want to see all available generations, you can use nix-env --list-generations, and if you want to switch to a specific generation, you can use nix-env --switch-generation <number>.

Remember, though, that nix-env --rollback only affects the user environment. It does not rollback changes to the system configuration in NixOS, which is handled by sudo nixos-rebuild switch --rollback.
