#!/usr/bin/env nix-shell
{ pkgs ? import <nixpkgs> {} }:





pkgs.mkShell {
    # nativeBuildInputs is usually what you want -- tools you need to run
    nativeBuildInputs = with pkgs.buildPackages; [ 
      python311Packages.jedi
    ];

    shellHook =
      ''
        source .env/bin/activate
        zsh
        echo "Entered dev-shell"

      '';
}
