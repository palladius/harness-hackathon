---
marp: true
theme: default
paginate: true
size: 16:9
footer: 'HSLU CAS Cloud Architecture M3  |  27 Nov 2026, Rotkreuz'
style: |
  section {
    background: #fafafa;
    color: #0f172a;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Inter, sans-serif;
    padding: 44px 54px 42px 54px;
    font-size: 21px;
    line-height: 1.35;
  }
  section::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 6px;
    background: linear-gradient(90deg, #4285f4 0% 25%, #ea4335 25% 50%, #fbbc04 50% 75%, #34a853 75% 100%);
  }
  footer {
    color: #94a3b8;
    font-size: 12px;
    font-weight: 400;
    left: 54px;
    bottom: 16px;
  }
  section::after {
    color: #94a3b8;
    font-size: 12px;
    font-weight: 400;
    right: 54px;
    bottom: 16px;
  }
  h1 {
    font-size: 35px;
    font-weight: 800;
    color: #0f172a;
    margin: 0 0 8px 0;
    line-height: 1.15;
    letter-spacing: -0.02em;
  }
  .sub {
    font-size: 17.5px;
    color: #475569;
    margin: 0 0 18px 0;
  }
  .cover-wrap {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 585px;
  }
  .cover-title {
    font-size: 54px;
    font-weight: 900;
    line-height: 1.08;
    letter-spacing: -0.03em;
    color: #0f172a;
    margin: 14px 0 12px 0;
  }
  .cover-sub {
    font-size: 22px;
    color: #334155;
    max-width: 980px;
    margin: 0 0 18px 0;
  }
  .pill-row {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    margin-bottom: 14px;
  }
  .pill {
    display: inline-block;
    padding: 5px 13px;
    border-radius: 999px;
    font-size: 13.5px;
    font-weight: 700;
    background: #ffffff;
    border: 1.5px solid #cbd5e1;
    color: #1e293b;
  }
  .pill.blue { background: #eff6ff; border-color: #93c5fd; color: #1d4ed8; }
  .pill.red { background: #fef2f2; border-color: #fca5a5; color: #b91c1c; }
  .pill.green { background: #f0fdf4; border-color: #86efac; color: #15803d; }
  .pill.amber { background: #fffbeb; border-color: #fcd34d; color: #b45309; }
  .flow-strip {
    display: grid;
    grid-template-columns: 1fr 28px 1fr 28px 1fr;
    align-items: center;
    gap: 8px;
    margin: 8px 0 12px 0;
  }
  .flow-box {
    background: #ffffff;
    border: 1.5px solid #e2e8f0;
    border-radius: 12px;
    padding: 14px 16px;
    box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);
  }
  .flow-box.red { border-top: 4px solid #dc2626; }
  .flow-box.blue { border-top: 4px solid #2563eb; }
  .flow-box.green { border-top: 4px solid #16a34a; }
  .flow-arrow {
    text-align: center;
    font-size: 24px;
    font-weight: 800;
    color: #94a3b8;
  }
  .speaker-bar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: #ffffff;
    border: 1.5px solid #e2e8f0;
    border-left: 6px solid #4285f4;
    border-radius: 12px;
    padding: 14px 20px;
  }
  .speaker-name {
    font-size: 19px;
    font-weight: 800;
    color: #0f172a;
  }
  .speaker-role {
    font-size: 15px;
    color: #475569;
  }
  .grid2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
  }
  .grid2-wide {
    display: grid;
    grid-template-columns: 1.25fr 0.75fr;
    gap: 24px;
    align-items: center;
  }
  .grid3 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 14px;
  }
  .card {
    background: #ffffff;
    border: 1.5px solid #e2e8f0;
    border-radius: 12px;
    padding: 15px 17px;
    box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);
  }
  .card.blue { border-top: 4px solid #2563eb; }
  .card.red { border-top: 4px solid #dc2626; }
  .card.green { border-top: 4px solid #16a34a; }
  .card.amber { border-top: 4px solid #d97706; }
  .card-title {
    font-size: 17px;
    font-weight: 800;
    color: #0f172a;
    margin: 0 0 6px 0;
  }
  .card-body {
    font-size: 14.5px;
    color: #334155;
    line-height: 1.4;
    margin: 0;
  }
  .prompt-box {
    background: #0f172a;
    color: #f8fafc;
    border-radius: 12px;
    padding: 15px 19px;
    font-family: "Roboto Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
    font-size: 13.8px;
    line-height: 1.5;
    margin-bottom: 16px;
    border-left: 5px solid #2563eb;
  }
  .prompt-box.red { border-left-color: #dc2626; }
  .prompt-box.green { border-left-color: #16a34a; }
  .mono-pill {
    font-family: "Roboto Mono", ui-monospace, monospace;
    background: #f1f5f9;
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    padding: 1px 6px;
    font-size: 0.85em;
    color: #0f172a;
    white-space: nowrap;
  }
  .bullet-sm {
    margin: 8px 0 0 0;
    padding-left: 17px;
    font-size: 13.8px;
    color: #334155;
    line-height: 1.42;
  }
  .bullet-sm li { margin-bottom: 5px; }
  .qr-card {
    background: #ffffff;
    border: 2px solid #e2e8f0;
    border-radius: 16px;
    padding: 18px;
    text-align: center;
    box-shadow: 0 6px 20px rgba(15, 23, 42, 0.06);
  }
  .qr-card img {
    width: 310px;
    height: 310px;
    display: block;
    margin: 0 auto 10px auto;
  }
  .qr-caption {
    font-size: 14px;
    font-weight: 700;
    color: #1e293b;
  }
  .link-list {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  .link-list li {
    background: #ffffff;
    border: 1.5px solid #e2e8f0;
    border-radius: 10px;
    padding: 11px 16px;
    margin-bottom: 10px;
    font-size: 15px;
  }
  .link-url {
    display: block;
    font-family: "Roboto Mono", ui-monospace, monospace;
    font-size: 12.8px;
    color: #2563eb;
    text-decoration: none;
    margin-top: 2px;
  }
---

<div class="cover-wrap">
  <div>
    <div class="pill-row">
      <span class="pill blue">HSLU CAS Cloud Architecture M3</span>
      <span class="pill green">Track 0: Swiss RAG</span>
      <span class="pill amber">Track 1: Cloud Arch Draw</span>
      <span class="pill red">Track 2: Guggu-Gstaeltli</span>
    </div>
    <div class="cover-title">HSLU Harness Hackathon</div>
    <div class="cover-sub">
      Pick 1 of 3 difficulty tracks and build it <strong>twice</strong> with your favorite AI harness — <strong>Pre-Riccardo (Blind Exam)</strong> vs. <strong>Post-Riccardo (Superpowers + Evals)</strong> — and prove the score jump!
    </div>
    <div class="pill-row">
      <span class="pill">Antigravity CLI (agy)</span>
      <span class="pill">Gemini CLI</span>
      <span class="pill">Claude Code</span>
      <span class="pill">OpenAI Codex</span>
      <span class="pill blue">BYOD / Optional Take-Home</span>
    </div>
  </div>
  <div class="flow-strip">
    <div class="flow-box red">
      <div class="card-title">Round 1: Pre-Riccardo</div>
      <div class="card-body">Build normally without peeking at evals; take the blind <span class="mono-pill">grader.py</span> exam.</div>
    </div>
    <div class="flow-arrow">&rarr;</div>
    <div class="flow-box green">
      <div class="card-title">Round 2: Post-Riccardo</div>
      <div class="card-body">Stack-agnostic <span class="mono-pill">SPEC.md</span>, 3+ tricks &amp; <span class="mono-pill">/goal</span> eval loop to <span class="mono-pill">reward = 1.0</span>.</div>
    </div>
    <div class="flow-arrow">&rarr;</div>
    <div class="flow-box blue">
      <div class="card-title">Ship &amp; Ping @palladius</div>
      <div class="card-body">Push GitHub repo + open an Issue tagging <span class="mono-pill">@palladius</span> with your PRE vs. POST delta!</div>
    </div>
  </div>
  <div class="speaker-bar">
    <div>
      <div class="speaker-name">Riccardo Carlesso</div>
      <div class="speaker-role">Developer Advocate, Google Cloud Zurich · ricc.rocks · github.com/palladius</div>
    </div>
    <div class="pill green">Pre-Established Evals · Objective 0..100 Grader</div>
  </div>
</div>

<!-- Speaker notes:
Every student -- whether PM, Cloud Architect, or Staff Engineer -- picks ONE of 3 difficulty tracks and runs the EXACT same scientific Pre-Riccardo vs Post-Riccardo A/B experiment!
-->

---

# Pick ONE Track: 3 Levels, Stack-Agnostic PRD

<div class="sub">Every track separates WHAT (<span class="mono-pill">SPEC.md</span>) from HOW (your favorite tech stack) and runs BOTH Pre-Riccardo &amp; Post-Riccardo!</div>

<div class="grid3">
  <div class="card green">
    <div class="pill-row" style="margin-bottom:8px;"><span class="pill green">Track 0 · Starter (45-60m)</span></div>
    <div class="card-title">Swiss Stories Manual RAG</div>
    <ul class="bullet-sm">
      <li>Transparent manual RAG over <strong>10 Public-Domain Swiss PDFs</strong> (<em>Heidi, William Tell, Ruetli 1291, Pilatus, Matterhorn</em>).</li>
      <li>Chunking + TF-IDF/Embeddings + mandatory filename citations.</li>
      <li><strong>Eval (<span class="mono-pill">--track rag</span>):</strong> 10 factual Qs + <strong>3 refusal traps</strong> (<em>"Heidi's IBAN?"</em>).</li>
      <li><strong>Stack:</strong> Offline Python/TS/Go/Ruby or live Ollama/Gemini.</li>
    </ul>
  </div>
  <div class="card amber">
    <div class="pill-row" style="margin-bottom:8px;"><span class="pill amber">Track 1 · Medium (1.5-2.5h)</span></div>
    <div class="card-title">Swiss Cloud Arch Draw</div>
    <ul class="bullet-sm">
      <li><strong>Option 1A (CLI)</strong> or <strong>Option 1B (Drag-and-Drop Canvas)</strong> for GCP, AWS, or Azure across 5 Swiss scenarios.</li>
      <li>Swiss regions (<span class="mono-pill">europe-west6</span>, <span class="mono-pill">eu-central-2</span>, <span class="mono-pill">CH North</span>) + Red Bottleneck X-Ray.</li>
      <li><strong>Eval (<span class="mono-pill">--track arch</span>):</strong> real <span class="mono-pill">dot -Tsvg</span> + revDSG/OBO/FinOps checks.</li>
      <li><strong>Stack:</strong> Python/Go/Rust/TS, React <span class="mono-pill">@xyflow</span>, or HTML5 SVG.</li>
    </ul>
  </div>
  <div class="card red">
    <div class="pill-row" style="margin-bottom:8px;"><span class="pill red">Track 2 · Boss Mode (3-5h)</span></div>
    <div class="card-title">Guggu-Gstaeltli UI Harness</div>
    <ul class="bullet-sm">
      <li>Build your own Swiss-branded (<span class="mono-pill">#D52B1E</span>) multi-thread UI Harness speaking <strong>Schwiizerduetsch</strong>.</li>
      <li>Synthesized <strong>"Guggu!"</strong> chime (<span class="mono-pill">E5-&gt;C#5</span> Web Audio) + animated cuckoo bird whenever a thread waits for your turn (+ Mute!).</li>
      <li><strong>Eval (<span class="mono-pill">--track guggu</span>):</strong> dialect, audio synth, state machine &amp; offline mock.</li>
      <li><strong>Stack:</strong> Electron, Tauri, Flutter, PyWebView, or Web.</li>
    </ul>
  </div>
</div>

<!-- Speaker notes:
Three difficulty ramps so nobody is bored and nobody is lost! Starter (Track 0) uses 10 real Public-Domain Swiss literature PDFs + 3 anti-hallucination trap questions; Medium (Track 1) is Cloud Architect heaven (CLI or Drag-and-Drop); Boss Mode (Track 2) is our hilarious Guggu-Gstaeltli / Gugger-Gschirr Swiss-German Cuckoo Harness!
-->

---

# Round 1 — Pre-Riccardo (Blind Exam Baseline)

<div class="sub">20-30 min in <span class="mono-pill">./round1-pre-riccardo/</span> — do NOT read <span class="mono-pill">grader.py</span> first; run it only at the end as a surprise exam!</div>

<div class="prompt-box red">
git clone https://github.com/palladius/harness-hackathon.git &amp;&amp; cd harness-hackathon<br/>
agy -i "Read exercises/ex1-yolo.md. I pick Track &lt;0 (rag) | 1 (arch) | 2 (guggu)&gt;.<br/>
Complete Round 1 (Pre-Riccardo) in ./round1-pre-riccardo, then run grader.py --track &lt;rag|arch|guggu&gt;."
</div>

<div class="grid3">
  <div class="card red">
    <div class="card-title">Why Pre-Riccardo Fails (Track 0)</div>
    <div class="card-body">Answers from parametric memory, drops PDF citations, and happily hallucinates Heidi's Swiss bank IBAN!</div>
  </div>
  <div class="card red">
    <div class="card-title">Why Pre-Riccardo Fails (Track 1)</div>
    <div class="card-body">Emits 3-box toy graphs, breaks <span class="mono-pill">dot -Tsvg</span> quotes, and forgets OBO ACLs &amp; Zurich residency.</div>
  </div>
  <div class="card red">
    <div class="card-title">Why Pre-Riccardo Fails (Track 2)</div>
    <div class="card-body">Writes High German instead of Schwiizerduetsch, links a missing <span class="mono-pill">cuckoo.mp3</span>, and crashes offline!</div>
  </div>
</div>

<!-- Speaker notes:
The Blind Exam rule is what makes this an honest A/B experiment! Without /grill-me, TDD, or pre-established Evals, models routinely take shortcuts and score 25 to 55 out of 100 (Harbor reward = 0.0).
-->

---

# Round 2 — Post-Riccardo (Superpowers + Evals)

<div class="sub">Fresh session in <span class="mono-pill">./round2-post-riccardo/</span> — separate <span class="mono-pill">SPEC.md</span> from Tech Stack, enable 3+ tricks &amp; loop to <span class="mono-pill">reward = 1.0</span>!</div>

<div class="prompt-box green">
agy -i "Read exercises/ex2-harness.md. Rebuild my Track &lt;0|1|2&gt; cleanly in ./round2-post-riccardo<br/>
using 3+ tricks + automated Evals until Harbor reward = 1.0. Run grader.py --compare,<br/>
write RETRO.md, and help me publish to GitHub + ping @palladius on an Issue!"
</div>

<div class="grid3">
  <div class="card green">
    <div class="card-title">/grill-me (Before Code)</div>
    <div class="card-body">Interview 1 question at a time until stack-agnostic <span class="mono-pill">SPEC.md</span> has zero ambiguity.</div>
  </div>
  <div class="card green">
    <div class="card-title">Superpowers</div>
    <div class="card-body">Enforce brainstorming, written plan, Red-Green TDD, and verification before done (<span class="mono-pill">obra/superpowers</span>).</div>
  </div>
  <div class="card green">
    <div class="card-title">Evals + /goal Harbor Loop</div>
    <div class="card-body">Run golden QA / <span class="mono-pill">dot -Tsvg</span> / state-machine evals + Ralph loop until Harbor <span class="mono-pill">reward = 1.0</span>!</div>
  </div>
  <div class="card blue">
    <div class="card-title">Conductor + Worktrees + HITL</div>
    <div class="card-body">Parallel branches via <span class="mono-pill">git worktree</span> + async GitHub Issues (<em>Crescendo of Agents Part 2</em>).</div>
  </div>
  <div class="card blue">
    <div class="card-title">/learn (Repo Memory)</div>
    <div class="card-body">Distill Round 1 blind-exam failures into <span class="mono-pill">AGENTS.md</span> or <span class="mono-pill">SKILL.md</span>.</div>
  </div>
  <div class="card amber">
    <div class="card-title">/swarm (Adversarial Review)</div>
    <div class="card-body">Builder agent vs. grumpy Swiss FINMA + SRE Reviewer blocking merge on any defect.</div>
  </div>
</div>

<!-- Speaker notes:
Notice how Evals are front and center in Round 2! Whether you pick Track 0, 1, or 2, you wire deterministic Evals into the agent's inner loop so Lusser's Law (0.95^20 = 35.8%) can never silently sink your release.
-->

---

# The 3-Tier Eval Chain: Proving PRE vs. POST Delta

<div class="sub">Tier 1 Local Unit/Golden &rarr; Tier 2 Harbor <span class="mono-pill">reward.txt = 1.0</span> &rarr; Tier 3 <span class="mono-pill">agents-cli</span> Quality Flywheel.</div>

<div class="grid2">
  <div class="card green">
    <div class="card-title">Portable /goal Harbor Loop + agents-cli Flywheel</div>
    <div class="prompt-box green" style="font-size:12.3px;padding:11px 14px;margin:8px 0 10px 0;">
      /goal: Do NOT stop until<br/>
      ./evals/harbor-task/tests/test.sh ./round2-post-riccardo &lt;rag|arch|guggu&gt;<br/>
      exits 0 and writes 1.0 to reward.txt (score &gt;= 95/100).<br/>
      Fix root cause on every failure (max 10 iterations).
    </div>
    <div class="card-body">
      <strong>Tier 3 (<span class="mono-pill">uv tool install google-agents-cli</span>):</strong><br/>
      <span class="mono-pill">agents-cli eval run</span> &rarr; <span class="mono-pill">eval analyze</span> &rarr; <span class="mono-pill">eval compare</span><br/>
      (LLM-as-Judge: <span class="mono-pill">grounding</span>, <span class="mono-pill">hallucination</span>, <span class="mono-pill">safety</span> + held-out cases).
    </div>
  </div>
  <div class="card blue">
    <div class="card-title">Zero-Friction Onboarding &amp; @palladius Hand-In</div>
    <ul class="bullet-sm">
      <li>Repo ships with <span class="mono-pill">AGENTS.md</span> (symlinked): <span class="mono-pill">git clone</span>, run <span class="mono-pill">agy -i "Start!"</span> (or <span class="mono-pill">gemini</span>/<span class="mono-pill">codex</span>/<span class="mono-pill">claude</span>), answer <strong>1 question</strong>.</li>
      <li>Verify <span class="mono-pill">secret_hygiene == 5/5</span>, push <span class="mono-pill">round1-pre-riccardo/</span> + <span class="mono-pill">round2-post-riccardo/</span> + <span class="mono-pill">RETRO.md</span> to GitHub.</li>
      <li>Open a GitHub Issue pinging <strong><span class="mono-pill">@palladius</span></strong> (or share your scoreboard on <strong>LinkedIn</strong>: <span class="mono-pill">linkedin.com/in/riccardocarlesso</span>).</li>
    </ul>
  </div>
</div>

<!-- Speaker notes:
This gives us real empirical telemetry across the whole class: every GitHub Issue pinging @palladius shows which track they chose, their tech stack, and their exact Pre-Riccardo vs Post-Riccardo score jump!
-->

---

# Launchpad: Scan Once, Ship Better Software

<div class="sub">Everything works live right now — 3 Tracks, 10 Swiss PDFs + golden_qa.json, Harbor eval &amp; 1-click Copy prompts.</div>

<div class="grid2-wide">
  <div>
    <ul class="link-list">
      <li>
        <strong>GitHub Starter Repo (Clone Offline: 10 Swiss PDFs · Grader · AGENTS.md)</strong>
        <a class="link-url" href="https://github.com/palladius/harness-hackathon">github.com/palladius/harness-hackathon</a>
      </li>
      <li>
        <strong>Live Web Hub (Browser Preview · 1-Click Copy Prompts · 6-Slide Deck)</strong>
        <a class="link-url" href="https://storage.googleapis.com/palladius-genai-storagify/hslu/2026-11-27-m3-v1.0.2/hackathon.html">storage.googleapis.com/.../hslu/2026-11-27-m3-v1.0.2/hackathon.html</a>
      </li>
      <li>
        <strong>Conductor + Worktrees + GitHub Issues + HITL Article</strong>
        <a class="link-url" href="https://ricc.rocks/en/posts/technology/2026-07-03-crescendo-of-agents-part-2/">ricc.rocks/en/posts/technology/2026-07-03-crescendo-of-agents-part-2/</a>
      </li>
      <li>
        <strong>Superpowers · Ralph Loop · Harbor · Public Skills</strong>
        <a class="link-url" href="https://github.com/obra/superpowers">github.com/obra/superpowers · ghuntley.com/ralph · harborframework.com</a>
      </li>
      <li>
        <strong>Hand-In (Optional): GitHub Issue pinging <span class="mono-pill">@palladius</span> or LinkedIn</strong>
        <div class="card-body">Share your Pre-Riccardo vs. Post-Riccardo scoreboard + 10-line <span class="mono-pill">RETRO.md</span>!</div>
      </li>
    </ul>
  </div>
  <div class="qr-card">
    <img src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4KPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0NTAiIGhlaWdodD0iNDUwIiBjbGFzcz0ic2Vnbm8iPjxnIHRyYW5zZm9ybT0ic2NhbGUoMTApIj48cGF0aCBmaWxsPSIjZmZmIiBkPSJNMCAwaDQ1djQ1aC00NXoiLz48cGF0aCBjbGFzcz0icXJsaW5lIiBzdHJva2U9IiMwZjE3MmEiIGQ9Ik0yIDIuNWg3bTMgMGgybTEgMGgzbTMgMGgxbTMgMGg0bTQgMGgxbTIgMGg3bS00MSAxaDFtNSAwaDFtMyAwaDJtNiAwaDFtMyAwaDFtNCAwaDJtMyAwaDFtMSAwaDFtNSAwaDFtLTQxIDFoMW0xIDBoM20xIDBoMW0xIDBoMm0zIDBoMW0xIDBoMW0zIDBoMm0yIDBoMW0zIDBoMm0xIDBoM20xIDBoMW0xIDBoM20xIDBoMW0tNDEgMWgxbTEgMGgzbTEgMGgxbTEgMGgzbTIgMGgxbTEgMGgybTEgMGgxbTEgMGgzbTEgMGgzbTIgMGgxbTEgMGgxbTIgMGgxbTEgMGgzbTEgMGgxbS00MSAxaDFtMSAwaDNtMSAwaDFtMSAwaDFtMyAwaDFtMiAwaDJtMiAwaDJtMiAwaDFtMiAwaDFtMyAwaDNtMSAwaDFtMSAwaDNtMSAwaDFtLTQxIDFoMW01IDBoMW0xIDBoMW05IDBoMW0xIDBoMW0xIDBoMW0yIDBoNm0zIDBoMW01IDBoMW0tNDEgMWg3bTEgMGgxbTEgMGgxbTEgMGgxbTEgMGgxbTEgMGgxbTEgMGgxbTEgMGgxbTEgMGgxbTEgMGgxbTEgMGgxbTEgMGgxbTEgMGgxbTEgMGgxbTEgMGg3bS0zMyAxaDJtMSAwaDFtMiAwaDNtMSAwaDVtMSAwaDFtMSAwaDFtNSAwaDFtLTMzIDFoMW0xIDBoNW00IDBoNG0xIDBoMm0xIDBoMm0xIDBoMW0xIDBoNG0xIDBoMW0xIDBoMm0xIDBoNW0tMzkgMWgxbTMgMGgxbTMgMGgybTMgMGgxbTEgMGgxbTIgMGgzbTIgMGgxbTEgMGgxbTIgMGgxbTIgMGgybTEgMGgzbTEgMGgxbTEgMGgxbS00MCAxaDJtMyAwaDFtMSAwaDNtMyAwaDVtMSAwaDJtNCAwaDNtMSAwaDFtMSAwaDJtMiAwaDFtMiAwaDFtLTM5IDFoMm0yIDBoMW0yIDBoNG0yIDBoMW0zIDBoMW0yIDBoM20yIDBoMm0zIDBoMm00IDBoMW0xIDBoMm0tMzggMWgybTEgMGgybTEgMGgxbTMgMGgybTEgMGgybTUgMGg1bTEgMGgxbTEgMGgybTIgMGgxbTEgMGgybTEgMGgxbS00MCAxaDNtNCAwaDJtMSAwaDZtMSAwaDFtMSAwaDFtMyAwaDFtMyAwaDFtMSAwaDdtMiAwaDJtLTM4IDFoMW0xIDBoNG0xIDBoMW0xIDBoM20zIDBoMm0xIDBoMm0xIDBoMW0yIDBoMW0xIDBoMm0xIDBoMm0xIDBoMW0xIDBoMm0tMzkgMWgxbTIgMGgxbTUgMGg1bTEgMGgybTIgMGg0bTEgMGgxbTEgMGgxbTEgMGgxbTEgMGgxbTMgMGgybTEgMGgxbS0zNiAxaDJtMSAwaDNtMiAwaDFtMyAwaDJtMSAwaDRtMSAwaDFtMiAwaDFtMyAwaDJtMiAwaDFtMSAwaDFtMiAwaDNtLTQxIDFoMW0xIDBoMm0zIDBoMm0xIDBoMm0xIDBoMm0xIDBoNm0xIDBoMm0xIDBoMW0yIDBoMW0xIDBoMW0yIDBoNG0xIDBoMm0tMzggMWgxbTEgMGg1bTMgMGgxbTEgMGgzbTIgMGgybTIgMGgxbTEgMGgybTIgMGgxbTEgMGgybTIgMGgxbTEgMGgxbS0zOSAxaDFtMSAwaDJtMSAwaDFtMiAwaDFtNCAwaDFtMyAwaDJtMSAwaDVtMyAwaDFtMSAwaDFtMSAwaDJtMiAwaDJtMSAwaDJtLTM5IDFoMW0yIDBoNW0yIDBoMm0xIDBoMm0yIDBoMW0xIDBoMW0yIDBoNm03IDBoMm0xIDBoMW0tMzkgMWgybTMgMGgzbTEgMGgxbTUgMGg3bTQgMGgxbTEgMGg3bTIgMGgybS00MSAxaDFtMyAwaDFtMSAwaDJtMiAwaDFtMiAwaDJtMSAwaDFtMSAwaDFtMyAwaDFtMSAwaDFtMSAwaDNtNCAwaDFtMiAwaDFtMSAwaDFtLTM4IDFoMW0xIDBoMm0zIDBoMW00IDBoMm01IDBoNG0yIDBoM20xIDBoMW0xIDBoMW0xIDBoMW0tMzIgMWg1bTcgMGgxbTEgMGgxbTQgMGg0bTEgMGgxbTEgMGgxbTEgMGgxbTYgMGgybS00MCAxaDFtMSAwaDFtMSAwaDFtMiAwaDJtMiAwaDFtMiAwaDFtMSAwaDFtMiAwaDJtMiAwaDFtNCAwaDFtMSAwaDJtMSAwaDVtMSAwaDJtLTQxIDFoMW0xIDBoNW0zIDBoMW00IDBoMW0yIDBoMW0xIDBoM20yIDBoM200IDBoMm0xIDBoMW0zIDBoMW0tMzcgMWgybTMgMGgxbTEgMGgxbTEgMGgxbTEgMGgxbTUgMGg0bTIgMGgxbTMgMGgzbTEgMGgybTEgMGgxbTEgMGgxbS00MCAxaDJtMSAwaDFtMiAwaDFtMSAwaDdtMSAwaDJtMiAwaDFtMSAwaDFtMSAwaDRtMSAwaDFtMSAwaDFtNSAwaDNtLTQwIDFoMm0yIDBoMW0zIDBoMW0yIDBoMm0xIDBoMW0xIDBoM20zIDBoMW0xIDBoMW01IDBoNW0xIDBoNW0tNDEgMWgxbTIgMGg1bTggMGgybTIgMGgzbTEgMGgxbTIgMGgxbTIgMGgxbTEgMGg3bS0zOSAxaDFtNyAwaDFtMyAwaDFtMSAwaDFtMSAwaDFtMSAwaDFtMiAwaDJtMyAwaDFtMSAwaDFtMSAwaDJtMSAwaDNtMSAwaDFtMiAwaDFtLTQxIDFoMW0zIDBoMW0xIDBoMW0xIDBoMW0xIDBoMm0xIDBoMm0yIDBoMm00IDBoMW0xIDBoMW0yIDBoOW0xIDBoMW0tMzEgMWgybTEgMGgxbTIgMGgybTMgMGgxbTIgMGg0bTMgMGgxbTEgMGgybTMgMGgxbTEgMGgzbS00MSAxaDdtNCAwaDRtMSAwaDFtMSAwaDFtMSAwaDFtMSAwaDFtMyAwaDJtMSAwaDFtMSAwaDJtMSAwaDFtMSAwaDJtMSAwaDFtLTQwIDFoMW01IDBoMW0xIDBoMm0zIDBoMW0yIDBoMW0yIDBoMW02IDBoMW00IDBoMm0zIDBoMW0zIDBoMW0tNDEgMWgxbTEgMGgzbTEgMGgxbTEgMGgxbTMgMGgybTEgMGgxbTIgMGgxbTEgMGgxMG0yIDBoNW0xIDBoMm0tNDAgMWgxbTEgMGgzbTEgMGgxbTEgMGgxbTMgMGgxbTQgMGgxbTEgMGgybTIgMGgxbTEgMGgxbTIgMGgzbTIgMGgxbTEgMGgxbTEgMGg0bS00MSAxaDFtMSAwaDNtMSAwaDFtMSAwaDFtMyAwaDNtNSAwaDNtMiAwaDVtMSAwaDhtLTM5IDFoMW01IDBoMW0yIDBoMW0xIDBoMW0xIDBoNG0yIDBoMW0xIDBoMW01IDBoMW00IDBoMm0yIDBoMm0xIDBoMW0tNDAgMWg3bTEgMGgxbTEgMGgybTUgMGgybTMgMGgxbTEgMGgzbTEgMGgybTEgMGgxbTMgMGgybTEgMGgxIi8+PC9nPjwvc3ZnPgo=" alt="QR Code to HSLU Harness Hackathon Hub" />
    <div class="qr-caption">Scan for All 3 Tracks, Prompts &amp; Evals</div>
  </div>
</div>

<!-- Speaker notes:
Scan once to launch the live Hackathon Hub with all 3 tracks (Starter Swiss RAG, Medium Cloud Arch Draw, Boss Mode Guggu-Gstaeltli), 10 downloadable Swiss PDFs, 1-click copy prompts, and the deterministic Pre vs Post grader!
-->
