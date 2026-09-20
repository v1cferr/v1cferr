# Victor "v1cferr" Ferreira

**AI Systems Analyst at FAI·UFSCar.** I build automation and AI-integrated systems in Python
and TypeScript, and run them on infrastructure I declare in Nix.

Most of what I ship starts as a problem I actually have: an admission deadline nobody noticed,
a timekeeping punch made twice, a workstation that had to be rebuilt from scratch. The
interesting part is never the script. It is deciding what the machine is allowed to decide on
its own.

[v1cferr.dev](https://v1cferr.dev) · [LinkedIn](https://www.linkedin.com/in/v1cferr/) · [dev.victorferreira@gmail.com](mailto:dev.victorferreira@gmail.com) · São Carlos, SP, Brazil

## Currently

- **Building** [`grad-radar`](https://github.com/v1cferr/grad-radar), which monitors graduate
  admission calls so that a deadline cannot pass unnoticed.
- **Running** a self-hosted NixOS machine that serves my own projects behind a single Caddy
  origin, with systemd timers instead of daemons.
- **Learning** Gleam, local LLM pipelines (Ollama, RAG) and MCP as an integration surface.

## Selected work

| Project | What it does | Stack |
| --- | --- | --- |
| **[grad-radar](https://github.com/v1cferr/grad-radar)** | Sweeps 19 official sources twice a day, detects changes in admission notices (HTML *and* PDF), and derives eligibility verdicts from quoted evidence. One proven failure eliminates; the absence of failures never approves. 23-table domain model, three test layers. | FastAPI · SQLAlchemy 2.0 async · PostgreSQL 17 · Next.js 16 · Playwright |
| **[dotfiles](https://github.com/v1cferr/dotfiles)** | My whole workstation as code: NixOS and home-manager in one flake, one command applies system *and* user. Secure Boot with my own keys, btrfs subvolumes, sops-managed secrets. Docs published at [dotfiles.v1cferr.dev](https://dotfiles.v1cferr.dev). | Nix · home-manager · sops-nix · disko · Hyprland |
| **[acuttis-point](https://github.com/v1cferr/acuttis-point)** | Headless timekeeping RPA that *asks before it acts*: a notification with a button authorises the punch, and a deadline run covers the tap that never comes. Pure domain logic in Gleam, browser work isolated in an adapter. | Gleam · Playwright · NixOS service + timer |
| **[portfolio-weblog](https://github.com/v1cferr/portfolio-weblog)** | My site, [v1cferr.dev](https://v1cferr.dev), with routing and content in English, Portuguese and Chinese. *(work in progress)* | Next.js 16 App Router · TypeScript · Tailwind · Supabase |

More in the same vein: [`credit-radar`](https://github.com/v1cferr/credit-radar) (credit
scores, debts and exposure tracked as one picture),
[`ufscar-housing-radar`](https://github.com/v1cferr/ufscar-housing-radar) (collect, compare and
rank apartments by price, distance and viability),
[`ascension-coa-scraper`](https://github.com/v1cferr/ascension-coa-scraper) (talent trees
normalised into a structured JSON dataset, over plain HTTP with no browser automation) and
[`obsidian-rag`](https://github.com/v1cferr/obsidian-rag) (RAG over a personal Markdown vault).

## Stack

| | |
| --- | --- |
| **Languages** | Python · TypeScript · Nix · Gleam · Bash · Java |
| **Backend** | FastAPI · SQLAlchemy 2.0 (async) · Alembic · PostgreSQL · Supabase |
| **Frontend** | Next.js (App Router) · React · Tailwind · Astro |
| **AI** | LLM integration · RAG · Ollama (local models) · MCP |
| **Infra** | NixOS · Docker Compose · Caddy · systemd timers · Playwright · Azure (Bicep) |
| **Tooling** | `just` · `uv` · `pnpm` · direnv · Git |

## How I work

- **Declarative and reproducible.** If it isn't in a flake or a compose file, it doesn't exist.
- **Official sources first**, with the original document preserved and the moment it was read recorded.
- **Manual first, automate after** the domain is understood, never before.
- **A model is never the source of a fact.** LLMs propose; verified extraction and human reading decide.
- **English-first codebases and documentation**, because the repositories are public.

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

**Analista de Sistemas de IA na FAI·UFSCar.** Construo sistemas de automação e integração com
IA em Python e TypeScript, e os executo sobre uma infraestrutura que declaro em Nix.

Quase tudo que eu entrego começa como um problema que eu realmente tenho: um prazo de edital
que ninguém viu, um ponto batido duas vezes, uma estação de trabalho que precisou ser remontada
do zero. A parte interessante nunca é o script. É decidir o que a máquina tem permissão de
decidir sozinha.

[v1cferr.dev](https://v1cferr.dev) · [LinkedIn](https://www.linkedin.com/in/v1cferr/) · [dev.victorferreira@gmail.com](mailto:dev.victorferreira@gmail.com) · São Carlos, SP, Brasil

## No momento

- **Construindo** o [`grad-radar`](https://github.com/v1cferr/grad-radar), que monitora editais
  de pós-graduação para que nenhum prazo passe despercebido.
- **Mantendo** uma máquina NixOS self-hosted que serve meus próprios projetos atrás de uma única
  origem Caddy, com timers do systemd em vez de daemons.
- **Estudando** Gleam, pipelines de LLM local (Ollama, RAG) e MCP como superfície de integração.

## Trabalhos selecionados

| Projeto | O que faz | Stack |
| --- | --- | --- |
| **[grad-radar](https://github.com/v1cferr/grad-radar)** | Varre 19 fontes oficiais duas vezes ao dia, detecta mudanças em editais (HTML *e* PDF) e deriva vereditos de elegibilidade a partir de evidência citada. Uma falha comprovada elimina; a ausência de falhas nunca aprova. Modelo de domínio com 23 tabelas, três camadas de teste. | FastAPI · SQLAlchemy 2.0 async · PostgreSQL 17 · Next.js 16 · Playwright |
| **[dotfiles](https://github.com/v1cferr/dotfiles)** | Minha estação de trabalho inteira como código: NixOS e home-manager em um único flake, um comando aplica sistema *e* usuário. Secure Boot com chaves próprias, subvolumes btrfs, segredos com sops. Documentação publicada em [dotfiles.v1cferr.dev](https://dotfiles.v1cferr.dev). | Nix · home-manager · sops-nix · disko · Hyprland |
| **[acuttis-point](https://github.com/v1cferr/acuttis-point)** | RPA headless de registro de ponto que *pergunta antes de agir*: uma notificação com botão autoriza a batida, e uma execução no limite do prazo cobre o toque que nunca vem. Lógica de domínio pura em Gleam, navegador isolado em um adaptador. | Gleam · Playwright · serviço + timer NixOS |
| **[portfolio-weblog](https://github.com/v1cferr/portfolio-weblog)** | Meu site, [v1cferr.dev](https://v1cferr.dev), com rotas e conteúdo em inglês, português e chinês. *(em desenvolvimento)* | Next.js 16 App Router · TypeScript · Tailwind · Supabase |

Mais na mesma linha: [`credit-radar`](https://github.com/v1cferr/credit-radar) (score, dívidas
e exposição de crédito acompanhados como um retrato único),
[`ufscar-housing-radar`](https://github.com/v1cferr/ufscar-housing-radar) (coletar, comparar e
ranquear apartamentos por preço, distância e viabilidade),
[`ascension-coa-scraper`](https://github.com/v1cferr/ascension-coa-scraper) (árvores de talento
normalizadas em um dataset JSON estruturado, em HTTP puro e sem automação de navegador) e
[`obsidian-rag`](https://github.com/v1cferr/obsidian-rag) (RAG sobre um cofre pessoal em Markdown).

## Stack

| | |
| --- | --- |
| **Linguagens** | Python · TypeScript · Nix · Gleam · Bash · Java |
| **Back-end** | FastAPI · SQLAlchemy 2.0 (async) · Alembic · PostgreSQL · Supabase |
| **Front-end** | Next.js (App Router) · React · Tailwind · Astro |
| **IA** | Integração com LLM · RAG · Ollama (modelos locais) · MCP |
| **Infra** | NixOS · Docker Compose · Caddy · timers do systemd · Playwright · Azure (Bicep) |
| **Ferramentas** | `just` · `uv` · `pnpm` · direnv · Git |

## Como eu trabalho

- **Declarativo e reprodutível.** Se não está em um flake ou em um compose, não existe.
- **Fontes oficiais primeiro**, preservando o documento original e registrando quando foi lido.
- **Manual primeiro, automatizar depois** de entender o domínio, nunca antes.
- **Um modelo nunca é a fonte de um fato.** LLMs propõem; extração verificada e leitura humana decidem.
- **Código e documentação em inglês**, porque os repositórios são públicos.

</details>

<details>
<summary><strong>中文</strong></summary>

<br>

# Victor "v1cferr" Ferreira

**FAI·UFSCar 人工智能系统分析师。** 我用 Python 和 TypeScript 构建自动化与 AI 集成系统，
并将它们运行在我用 Nix 声明式定义的基础设施上。

我做的大部分项目都源于我自己真实遇到的问题：一个没人注意到的招生截止日期、一次重复打卡、
一台需要从零重建的工作站。有意思的部分从来不是脚本本身，而是决定机器可以自己决定什么。

[v1cferr.dev](https://v1cferr.dev) · [LinkedIn](https://www.linkedin.com/in/v1cferr/) · [dev.victorferreira@gmail.com](mailto:dev.victorferreira@gmail.com) · 巴西圣卡洛斯

## 目前

- **正在构建** [`grad-radar`](https://github.com/v1cferr/grad-radar)，用于监控研究生招生公告，
  确保任何截止日期都不会被漏掉。
- **正在维护** 一台自托管的 NixOS 主机，通过单一 Caddy 入口提供我自己的项目服务，
  用 systemd 定时器而非常驻守护进程。
- **正在学习** Gleam、本地 LLM 流水线（Ollama、RAG）以及作为集成接口的 MCP。

## 精选项目

| 项目 | 简介 | 技术栈 |
| --- | --- | --- |
| **[grad-radar](https://github.com/v1cferr/grad-radar)** | 每天两次扫描 19 个官方来源，检测招生公告（HTML *和* PDF）的变化，并基于引用证据推导资格结论：一项已证实的不符合即淘汰，而没有不符合并不等于通过。23 张表的领域模型，三层测试。 | FastAPI · SQLAlchemy 2.0 async · PostgreSQL 17 · Next.js 16 · Playwright |
| **[dotfiles](https://github.com/v1cferr/dotfiles)** | 把整台工作站写成代码：NixOS 与 home-manager 合在一个 flake 中，一条命令同时应用系统*和*用户配置。自签密钥的安全启动、btrfs 子卷、用 sops 管理的密钥。文档发布在 [dotfiles.v1cferr.dev](https://dotfiles.v1cferr.dev)。 | Nix · home-manager · sops-nix · disko · Hyprland |
| **[acuttis-point](https://github.com/v1cferr/acuttis-point)** | 无头考勤打卡 RPA，*先询问再行动*：带按钮的通知用于授权打卡，若无人点击，临近截止的那次运行会兜底。领域逻辑用 Gleam 保持纯粹，浏览器操作隔离在适配器中。 | Gleam · Playwright · NixOS 服务与定时器 |
| **[portfolio-weblog](https://github.com/v1cferr/portfolio-weblog)** | 我的个人网站 [v1cferr.dev](https://v1cferr.dev)，路由与内容支持英文、葡萄牙文和中文。*（开发中）* | Next.js 16 App Router · TypeScript · Tailwind · Supabase |

同类的其他项目：[`credit-radar`](https://github.com/v1cferr/credit-radar)（把信用分、债务与
信用敞口作为一张整图来追踪）、
[`ufscar-housing-radar`](https://github.com/v1cferr/ufscar-housing-radar)（按价格、距离与
可行性采集、比较并排序公寓）、
[`ascension-coa-scraper`](https://github.com/v1cferr/ascension-coa-scraper)（把天赋树归一化为
结构化 JSON 数据集，纯 HTTP，不用浏览器自动化），以及
[`obsidian-rag`](https://github.com/v1cferr/obsidian-rag)（在个人 Markdown 知识库上做 RAG）。

## 技术栈

| | |
| --- | --- |
| **语言** | Python · TypeScript · Nix · Gleam · Bash · Java |
| **后端** | FastAPI · SQLAlchemy 2.0（异步）· Alembic · PostgreSQL · Supabase |
| **前端** | Next.js（App Router）· React · Tailwind · Astro |
| **人工智能** | LLM 集成 · RAG · Ollama（本地模型）· MCP |
| **基础设施** | NixOS · Docker Compose · Caddy · systemd 定时器 · Playwright · Azure（Bicep） |
| **工具** | `just` · `uv` · `pnpm` · direnv · Git |

## 我的工作方式

- **声明式且可复现。** 不在 flake 或 compose 文件里的东西，就等于不存在。
- **官方来源优先**，保留原始文档，并记录读取的时刻。
- **先手工，后自动化：** 在理解领域之后，而不是之前。
- **模型永远不是事实的来源。** LLM 只负责提议；经过验证的抽取和人工阅读才做决定。
- **代码与文档以英文为先**，因为这些仓库是公开的。

</details>
