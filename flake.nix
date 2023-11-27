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

              presenterm = prev.rustPlatform.buildRustPackage
                rec {
                  pname = "presenterm";
                  version = "0.2.1";

                  src = prev.fetchFromGitHub {
                    owner = "mfontanini";
                    repo = "presenterm";
                    rev = "v${version}";
                    hash = "sha256-sXVMVU34gxZKGNye6hoyv07a7N7f6UbivA6thbSOeZA=";
                  };

                  buildFeatures = [ "sixel" ];

                  nativeBuildInputs = with prev; [ makeWrapper ];

                  doCheck = false;

                  postInstall = ''
                    wrapProgram $out/bin/presenterm \
                      --prefix LD_LIBRARY_PATH : "${prev.lib.makeLibraryPath [ prev.libsixel ]}"
                  '';

                  cargoHash = "sha256-PsDaXMws/8hEvAZwClQ4okGuryg1iKg0IBr7Xp2QYBE=";
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
                presenterm
                valgrind
                clang-tools
                libcs50
                style50
                sqlite
                nodePackages_latest.sql-formatter
              ] ++
              (with pkgs.python3.pkgs; [
                python-lsp-server
                python-cs50
                termcolor
                pylint
                black
                isort
                pytest

                # HACK? 
                # propagatedBuildInputs of the python-cs50 libs are not part
                # of the runtime path if these are not included
                flask
                packaging
                sqlalchemy
                sqlparse
                termcolor
                wheel
                typing-extensions

                # requirements for pset9/finance
                flask-session
                requests
                pytz
                urllib3
                charset-normalizer
                idna
                certifi
                cachelib
                werkzeug
              ]);
            }
          ];
        };
      });
}
