
{ pkgs, ... }:
let
  python-with-packages = pkgs.python313.withPackages (ps: [
    ps.pip
    ps.ipykernel
    ps.colorama
    ps.numba
  ]);
in
{
  channel = "unstable";

  packages = [
    python-with-packages
  ];

  idx.extensions = [
    "ms-python.python"
    "ms-toolsai.jupyter"
  ];

  # Optional: Set the Python interpreter path for VS Code
  # environment.variables = { 
  #   VIRTUAL_ENV = "${python-with-packages}";
  # };
}
