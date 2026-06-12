/* Data Architect Study Tracker — vanilla JS, no backend.
   State in localStorage; timers survive app closure via timestamps. */
(function () {
  "use strict";
  const LS_KEY = "spt-v1";
  const PLAN = window.PLAN;
  const $ = (sel) => document.querySelector(sel);

  // ---------- state ----------
  let S;
  function load() {
    try { S = JSON.parse(localStorage.getItem(LS_KEY)) || {}; } catch { S = {}; }
    S.items = S.items || {};
    S.runner = S.runner || null;
  }
  function save() { localStorage.setItem(LS_KEY, JSON.stringify(S)); }
  function rec(key) {
    if (!S.items[key]) S.items[key] = { st: "todo", min: 0, sessions: [], note: "" };
    return S.items[key];
  }

  // ---------- plan lookups ----------
  const INDEX = {};
  PLAN.phases.forEach((p) => p.items.forEach((it) => (INDEX[it.key] = { it, p })));

  // ---------- formatting ----------
  const h1 = (min) => (min / 60).toFixed(1);
  function hm(min) {
    const h = Math.floor(min / 60), m = Math.round(min % 60);
    return h ? `${h}h ${m.toString().padStart(2, "0")}m` : `${m}m`;
  }
  function clock(ms) {
    const s = Math.floor(ms / 1000);
    const p = (n) => String(n).padStart(2, "0");
    return `${p(Math.floor(s / 3600))}:${p(Math.floor((s % 3600) / 60))}:${p(s % 60)}`;
  }
  const STICON = { todo: "○", doing: "◐", done: "✅", skip: "⏭" };
  const esc = (t) => t.replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

  // ---------- timer ----------
  let tick = null;
  function startTimer(key) {
    if (S.runner && S.runner.key !== key) stopTimer(true);
    if (!S.runner) S.runner = { key, start: Date.now() };
    const r = rec(key);
    if (r.st === "todo") r.st = "doing";
    save(); render();
  }
  function stopTimer(silent) {
    if (!S.runner) return;
    const min = Math.max(1, Math.round((Date.now() - S.runner.start) / 60000));
    const r = rec(S.runner.key);
    r.min += min;
    r.sessions.push([new Date(S.runner.start).toISOString().slice(0, 16), min]);
    if (r.sessions.length > 200) r.sessions.shift();
    const k = S.runner.key;
    S.runner = null;
    save();
    if (!silent) render();
    return k;
  }
  function discardTimer() { S.runner = null; save(); render(); }
  function banner() {
    const b = $("#runner-banner");
    if (!S.runner) { b.classList.add("hidden"); return; }
    const e = INDEX[S.runner.key];
    b.classList.remove("hidden");
    b.innerHTML =
      `<span>⏱ <b>${clock(Date.now() - S.runner.start)}</b> · ` +
      `<a href="#/i/${S.runner.key}" style="color:var(--accent)">${esc(e ? e.it.title.slice(0, 34) : S.runner.key)}</a></span>` +
      `<button id="bn-stop">Stop</button>`;
    $("#bn-stop").onclick = () => stopTimer(false);
  }

  // ---------- aggregates ----------
  function agg(items) {
    let spent = 0, doneEst = 0, skipEst = 0, est = 0;
    items.forEach((it) => {
      const r = S.items[it.key];
      est += it.est;
      if (r) {
        spent += r.min;
        if (r.st === "done") doneEst += it.est;
        if (r.st === "skip") skipEst += it.est;
      }
    });
    return { spent, doneEst, skipEst, est };
  }

  // ---------- views ----------
  function home() {
    const all = PLAN.phases.flatMap((p) => p.items);
    const a = agg(all);
    const pct = Math.round(((a.doneEst + a.skipEst) / a.est) * 100);
    let html = `<h1>Fundamentals → Data Architect</h1>
      <div class="card">
        <div><b>${pct}%</b> complete · <b>${h1(a.spent)} h</b> logged</div>
        <div class="bar"><i class="g" style="width:${pct}%"></i></div>
        <div class="muted">done ${a.doneEst.toFixed(0)} h + skipped ${a.skipEst.toFixed(0)} h of ${a.est.toFixed(0)} h planned · budget ${PLAN.budgetH} h</div>
        <div class="muted">skip-test bank: ${a.skipEst.toFixed(0)} h returned to slack</div>
      </div>`;
    PLAN.phases.forEach((p) => {
      const pa = agg(p.items);
      const ppct = Math.round(((pa.doneEst + pa.skipEst) / pa.est) * 100);
      html += `<a class="row" href="#/p/${p.n}">
        <div class="grow">
          <div class="title">Phase ${p.n}: ${esc(p.title)}</div>
          <div class="bar"><i class="g" style="width:${ppct}%"></i></div>
          <div class="sub">months ${p.months} · ${h1(pa.spent)} h / ${pa.est.toFixed(0)} h est · ${ppct}%</div>
        </div><span class="muted">›</span></a>`;
    });
    return html;
  }

  function phaseView(n) {
    const p = PLAN.phases.find((x) => x.n === n);
    if (!p) return home();
    const pa = agg(p.items);
    let html = `<a class="back" href="#/">‹ All phases</a>
      <h1>Phase ${p.n}: ${esc(p.title)}</h1>
      <div class="card"><div class="muted">months ${p.months} · ${h1(pa.spent)} h logged / ${pa.est.toFixed(0)} h estimated</div>
      <div class="bar"><i class="g" style="width:${Math.round(((pa.doneEst + pa.skipEst) / pa.est) * 100)}%"></i></div></div>`;
    p.items.forEach((it) => {
      const r = S.items[it.key] || { st: "todo", min: 0 };
      html += `<a class="row" href="#/i/${it.key}">
        <span class="st">${STICON[r.st]}</span>
        <div class="grow">
          <div class="title">${esc(it.title)}</div>
          <div class="sub">${hm(r.min)} / ${it.est} h est</div>
        </div>
        <span class="chip ${it.tier.slice(0, 2) === "CA" ? "CAP" : it.tier.slice(0, 2)}">${it.tier}</span></a>`;
    });
    return html;
  }

  function itemView(key) {
    const e = INDEX[key];
    if (!e) return home();
    const { it, p } = e;
    const r = rec(key);
    const running = S.runner && S.runner.key === key;
    return `<a class="back" href="#/p/${p.n}">‹ Phase ${p.n}</a>
      <h1>${esc(it.title)} <span class="chip ${it.tier.slice(0, 2) === "CA" ? "CAP" : it.tier.slice(0, 2)}">${it.tier}</span></h1>
      <div class="card">
        <div class="timerbig" id="t-clock">${running ? clock(Date.now() - S.runner.start) : hm(r.min)}</div>
        <div class="muted" style="text-align:center">${running ? "running — total " + hm(r.min) + " booked" : "logged of " + it.est + " h estimated"}</div>
        <div class="btn-row">
          ${running
            ? `<button class="btn primary" id="t-stop">⏹ Stop & book</button><button class="btn danger" id="t-discard">Discard</button>`
            : `<button class="btn primary" id="t-start">▶ Start timer</button><button class="btn" id="t-manual">＋ minutes</button>`}
        </div>
        <select id="t-status">
          ${["todo", "doing", "done", "skip"].map((s) => `<option value="${s}" ${r.st === s ? "selected" : ""}>${STICON[s]} ${s === "skip" ? "skipped (skip test passed)" : s}</option>`).join("")}
        </select>
        <div style="margin-top:10px"><textarea id="t-note" placeholder="Journal: what I did, what surprised me, open question…">${esc(r.note || "")}</textarea></div>
        ${r.sessions.length ? `<div class="sessions">Recent: ${r.sessions.slice(-5).reverse().map((s) => `${s[0].replace("T", " ")} · ${hm(s[1])}`).join(" · ")}</div>` : ""}
      </div>
      <div class="card content">${it.html}</div>`;
  }

  // ---------- router / render ----------
  function render() {
    const hash = location.hash || "#/";
    let html;
    let m;
    if ((m = hash.match(/^#\/p\/(\d)/))) html = phaseView(+m[1]);
    else if ((m = hash.match(/^#\/i\/(.+)$/))) html = itemView(decodeURIComponent(m[1]));
    else html = home();
    $("#view").innerHTML = html;
    banner();
    bind(hash);
    clearInterval(tick);
    if (S.runner) {
      tick = setInterval(() => {
        banner();
        const c = $("#t-clock");
        if (c && location.hash === `#/i/${S.runner.key}`) c.textContent = clock(Date.now() - S.runner.start);
      }, 1000);
    }
  }

  function bind(hash) {
    const m = hash.match(/^#\/i\/(.+)$/);
    if (!m) return;
    const key = decodeURIComponent(m[1]);
    const r = rec(key);
    const on = (sel, fn) => { const el = $(sel); if (el) el.onclick = fn; };
    on("#t-start", () => startTimer(key));
    on("#t-stop", () => stopTimer(false));
    on("#t-discard", () => { if (confirm("Discard running time?")) discardTimer(); });
    on("#t-manual", () => {
      const v = parseInt(prompt("Minutes to add (negative to correct):", "30"), 10);
      if (!isNaN(v) && v) { r.min = Math.max(0, r.min + v); if (v > 0) r.sessions.push([new Date().toISOString().slice(0, 16), v]); save(); render(); }
    });
    const st = $("#t-status");
    if (st) st.onchange = () => { r.st = st.value; save(); banner(); };
    const note = $("#t-note");
    if (note) note.onchange = () => { r.note = note.value; save(); };
  }

  // ---------- export / import ----------
  $("#btn-export").onclick = () => {
    const blob = new Blob([JSON.stringify({ exported: new Date().toISOString(), state: S }, null, 1)], { type: "application/json" });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = `study-progress-${new Date().toISOString().slice(0, 10)}.json`;
    a.click();
  };
  $("#btn-import").onclick = () => $("#import-file").click();
  $("#import-file").onchange = (ev) => {
    const f = ev.target.files[0];
    if (!f) return;
    f.text().then((t) => {
      try {
        const d = JSON.parse(t);
        if (!d.state || !d.state.items) throw new Error("not a progress file");
        if (confirm("Replace current progress with imported file?")) { S = d.state; save(); render(); }
      } catch (e) { alert("Import failed: " + e.message); }
    });
    ev.target.value = "";
  };

  // ---------- boot ----------
  load();
  window.addEventListener("hashchange", render);
  render();
  if (location.protocol.startsWith("http") && "serviceWorker" in navigator) {
    navigator.serviceWorker.register("sw.js").catch(() => {});
  }
})();
