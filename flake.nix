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

              python3 = prev.python3 // {
                pkgs = prev.python3.pkgs // {
                  python-cs50 = prev.python3.pkgs.buildPythonPackage rec {
                    pname = "cs50";
                    version = "9.3.0";
                    format = "setuptools";
                    src = prev.fetchPypi {
                      inherit pname version;
                      hash = "sha256-pRMECa0S1kpj/UNtMacLV1psxReXp7Ck1kgjVQrnYkg=";
                    };
                    propagatedBuildInputs =
                      with prev.python3.pkgs; [
                        flask
                        packaging
                        sqlalchemy
                        sqlparse
                        termcolor
                        wheel
                      ];
                    doCheck = false;
                  };
                };
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
              languages.python.enable = true;
              packages = with pkgs; [
                valgrind
                clang-tools
                libcs50
                style50
              ] ++
              (with pkgs.python3.pkgs; [
                python-lsp-server
                python-cs50
                termcolor
              ]);
            }
          ];
        };
      });
}
