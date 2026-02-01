{ pkgs }: {
  deps = [
    pkgs.mysql
    pkgs.python311
    pkgs.python311Packages.pip
  ];
}
