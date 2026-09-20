# Victor "v1cferr" Ferreira

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

## What I build

**[grad-radar](https://github.com/v1cferr/grad-radar)** watches 19 official sources twice a day
and notices when an admission call changes, PDFs included. It never approves anything on its
own: one proven failure eliminates a programme, while nothing missing counts in its favour.
Twenty-three tables, three layers of tests, and every verdict carries the sentence it came from.

**[dotfiles](https://github.com/v1cferr/dotfiles)** is the machine all of this runs on. NixOS
and home-manager in a single flake, Secure Boot signed with my own keys, btrfs subvolumes,
secrets through sops. I wrote down why each module exists, and that became
[dotfiles.v1cferr.dev](https://dotfiles.v1cferr.dev).

**[acuttis-point](https://github.com/v1cferr/acuttis-point)** punches my timecard, but only
after I say yes. It sends a notification with a button on it; if nobody taps, a run near the
end of the window punches anyway. That shape came from the two days it did not have it, when a
manual punch landed minutes after the automatic one and the system read it as a lunch break
that began nine minutes after arriving.

**[portfolio-weblog](https://github.com/v1cferr/portfolio-weblog)** is
[v1cferr.dev](https://v1cferr.dev), with routing and content in English, Portuguese and Chinese.

Smaller ones, same habit: [`credit-radar`](https://github.com/v1cferr/credit-radar) keeps
scores, debts and exposure in one picture.
[`ufscar-housing-radar`](https://github.com/v1cferr/ufscar-housing-radar) ranks apartments by
price, distance and whether they are actually viable.
[`ascension-coa-scraper`](https://github.com/v1cferr/ascension-coa-scraper) turns talent trees
into a JSON dataset over plain HTTP, with no browser anywhere near it. And
[`obsidian-rag`](https://github.com/v1cferr/obsidian-rag) answers questions about my own notes
without any of them leaving the room.

<!--
A language/stats card can go here, e.g.:
https://github-readme-stats.vercel.app/api/top-langs/?username=v1cferr&layout=compact&langs_count=8&hide=html,css,tex&hide_border=true
Left out on purpose: the public instance is frequently rate-limited and renders as a
broken image, which reads worse than no card at all. Self-host it if you want it back.
-->

---

<details>
<summary><strong>Português</strong></summary>

<br>

# Victor "v1cferr" Ferreira

O bloco Nix acima vale nos três idiomas, então não o repito aqui.

Tudo o que está nele é real, inclusive os timers.

[v1cferr.dev](https://v1cferr.dev) · [LinkedIn](https://www.linkedin.com/in/v1cferr/) · [dev.victorferreira@gmail.com](mailto:dev.victorferreira@gmail.com)

## O que eu construo

**[grad-radar](https://github.com/v1cferr/grad-radar)** observa 19 fontes oficiais duas vezes
ao dia e percebe quando um edital muda, PDFs inclusive. Ele nunca aprova nada sozinho: uma
falha comprovada elimina um programa, enquanto o que está faltando não conta a favor. São 23
tabelas, três camadas de teste, e todo veredito carrega a frase de onde veio.

**[dotfiles](https://github.com/v1cferr/dotfiles)** é a máquina onde tudo isso roda. NixOS e
home-manager num único flake, Secure Boot assinado com chaves minhas, subvolumes btrfs,
segredos via sops. Escrevi por que cada módulo existe, e aquilo virou
[dotfiles.v1cferr.dev](https://dotfiles.v1cferr.dev).

**[acuttis-point](https://github.com/v1cferr/acuttis-point)** bate meu ponto, mas só depois que
eu digo sim. Ele manda uma notificação com um botão; se ninguém toca, uma execução perto do fim
da janela bate assim mesmo. Esse formato nasceu dos dois dias em que ele não o tinha, quando uma
batida manual caiu minutos depois da automática e o sistema leu aquilo como um almoço que
começou nove minutos depois da chegada.

**[portfolio-weblog](https://github.com/v1cferr/portfolio-weblog)** é o
[v1cferr.dev](https://v1cferr.dev), com rotas e conteúdo em inglês, português e chinês.

Os menores, mesmo hábito: [`credit-radar`](https://github.com/v1cferr/credit-radar) mantém
score, dívidas e exposição num retrato só.
[`ufscar-housing-radar`](https://github.com/v1cferr/ufscar-housing-radar) ranqueia apartamentos
por preço, distância e se são de fato viáveis.
[`ascension-coa-scraper`](https://github.com/v1cferr/ascension-coa-scraper) transforma árvores
de talento em um dataset JSON sobre HTTP puro, sem nenhum navegador por perto. E o
[`obsidian-rag`](https://github.com/v1cferr/obsidian-rag) responde perguntas sobre as minhas
próprias notas sem que nenhuma delas saia da sala.

</details>

<details>
<summary><strong>中文</strong></summary>

<br>

# Victor "v1cferr" Ferreira

上面的 Nix 代码块三种语言通用，这里不再重复。

里面写的都是真的，包括那些定时器。

[v1cferr.dev](https://v1cferr.dev) · [LinkedIn](https://www.linkedin.com/in/v1cferr/) · [dev.victorferreira@gmail.com](mailto:dev.victorferreira@gmail.com)

## 我在做什么

**[grad-radar](https://github.com/v1cferr/grad-radar)** 每天两次盯着 19 个官方来源，
在招生公告发生变化时察觉到，PDF 也算在内。它从不自己下达通过的结论：一项已证实的不符合
就淘汰一个项目，而缺失的信息不会算作有利条件。23 张表、三层测试，每个结论都带着它所依据的那句原文。

**[dotfiles](https://github.com/v1cferr/dotfiles)** 就是这一切运行的那台机器。NixOS 与
home-manager 合在一个 flake 里，用自己的密钥签名的安全启动、btrfs 子卷、经由 sops 管理的密钥。
我把每个模块存在的理由都写了下来，那些文字变成了
[dotfiles.v1cferr.dev](https://dotfiles.v1cferr.dev)。

**[acuttis-point](https://github.com/v1cferr/acuttis-point)** 替我打考勤卡，但要等我点头之后。
它会发一条带按钮的通知；如果没人点，接近时间窗口末尾的那次运行仍然会打卡。这个设计来自它还没有
这层保护的那两天：一次手动打卡落在自动打卡之后几分钟，系统把它读成了一段在到岗九分钟后就开始的午休。

**[portfolio-weblog](https://github.com/v1cferr/portfolio-weblog)** 就是
[v1cferr.dev](https://v1cferr.dev)，路由与内容支持英文、葡萄牙文和中文。

一些更小的，习惯相同：[`credit-radar`](https://github.com/v1cferr/credit-radar) 把信用分、
债务与信用敞口放进同一张图里。
[`ufscar-housing-radar`](https://github.com/v1cferr/ufscar-housing-radar) 按价格、距离以及
是否真的可行来排序公寓。
[`ascension-coa-scraper`](https://github.com/v1cferr/ascension-coa-scraper) 用纯 HTTP
把天赋树变成 JSON 数据集，全程不让浏览器靠近。
[`obsidian-rag`](https://github.com/v1cferr/obsidian-rag) 回答关于我自己笔记的问题，
而这些笔记一条都不会离开房间。

</details>
