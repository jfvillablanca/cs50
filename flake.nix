{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
    devenv.url = "github:cachix/devenv";
  };

  outputs = { self, nixpkgs, devenv, flake-utils, ... } @ inputs:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
          overlays = [
            (final: prev: {
              style50 = prev.python3.pkgs.buildPythonApplication
                rec {
                  pname = "style50";
                  version = "2.9.0";
                  format = "setuptools";
                  src = prev.fetchPypi {
                    inherit pname version;
                    hash = "sha256-TIaBLa5cUTRAFHR7+uTL2legBHax2Bdugj6rYJsHsRw=";
                  };
                  doCheck = false;
                  propagatedBuildInputs =
                    with prev; [
                      icdiff
                    ] ++
                    (with prev.python3.pkgs; [
                      setuptools
                      black
                      jsbeautifier
                      pycodestyle
                      magic
                      termcolor
                      jinja2
                    ]);
                };
            })
          ];
        };
      in
      {
        devShells.default = devenv.lib.mkShell {
          inherit inputs pkgs;
          modules = [
            {
              languages.c.enable = true;
              languages.rust.enable = true;
              packages = with pkgs; [
                clang-tools
                libcs50
                style50
              ];
            }
          ];
        };
      });
}
