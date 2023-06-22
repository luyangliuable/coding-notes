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
