<img src="assets/reproducible.svg" width="880"
     alt="The same flake.lock, built in 2026 and in 2031, resolving to the identical /nix/store path">

```nix
{ pkgs, lib, ... }:

{
  victor = {
    name     = "Victor Ferreira";
    handle   = "v1cferr";
    role     = "AI Systems Analyst";
    at       = "FAI·UFSCar";
    location = "São Carlos, SP, Brazil";
  };

  environment.systemPackages = with pkgs; [ python313 typescript nix gleam ];

  stack = {
    backend  = [ "FastAPI" "SQLAlchemy 2.0 (async)" "Alembic" "PostgreSQL" ];
    frontend = [ "Next.js (App Router)" "React" "Tailwind" ];
    ai       = [ "RAG" "Ollama" "MCP" ];
    infra    = [ "NixOS" "Docker Compose" "Caddy" "Playwright" "Azure (Bicep)" ];
  };

  services.automation = {
    enable = true;
    timers = {
      # This desktop sleeps at night. A missed sweep runs late, never not at all.
      grad-radar    = { onCalendar = "08,20:00"; persistent = true; };
      # One authorisation, taken by whoever gets there first: the tap or the deadline.
      acuttis-point = { askBefore = true; };
    };
  };

  programs.llm = {
    enable   = true;
    provider = "ollama";
    local    = true;         # nothing leaves the machine
    trust    = "proposals";  # a model is never the source of a fact
  };

  meta.homepage = "https://v1cferr.dev";
}
```

Everything up there is real, including the timers.

[v1cferr.dev](https://v1cferr.dev) · [LinkedIn](https://www.linkedin.com/in/v1cferr/) · [dev.victorferreira@gmail.com](mailto:dev.victorferreira@gmail.com)

<!--
A language/stats card can go here, e.g.:
https://github-readme-stats.vercel.app/api/top-langs/?username=v1cferr&layout=compact&langs_count=8&hide=html,css,tex&hide_border=true
Left out on purpose: the public instance is frequently rate-limited and renders as a
broken image, which reads worse than no card at all. Self-host it if you want it back.
-->
