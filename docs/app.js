/* Data Architect Study Tracker — vanilla JS, no backend.
   State in localStorage; timers survive app closure via timestamps.
   Optional cross-device sync via a private GitHub Gist (token with gist scope only). */
(function () {
  "use strict";
  const LS_KEY = "spt-v1";
  const SY_KEY = "spt-sync";
  const PLAN = window.PLAN;
  const $ = (sel) => document.querySelector(sel);

  // ---------- state ----------
  let S, SY, syncStatus = "";
  function recalc(r) { r.min = Math.max(0, (r.sessions || []).reduce((n, s) => n + s[1], 0)); }
  function compact(r) {
    if (r.sessions.length > 400) {
      const head = r.sessions.splice(0, r.sessions.length - 300);
      r.sessions.unshift(["baseline-" + Date.now(), head.reduce((n, s) => n + s[1], 0)]);
    }
  }
  function load() {
    try { S = JSON.parse(localStorage.getItem(LS_KEY)) || {}; } catch { S = {}; }
    S.items = S.items || {};
    S.runner = S.runner || null;
    // migrate: min must equal the session sum (sync merges depend on it)
    let migrated = false;
    Object.values(S.items).forEach((r) => {
      r.sessions = r.sessions || [];
      const sum = r.sessions.reduce((n, s) => n + s[1], 0);
      if ((r.min || 0) > sum) { r.sessions.push(["baseline-mig", (r.min || 0) - sum]); migrated = true; }
      recalc(r);
    });
    if (migrated) save();
    try { SY = JSON.parse(localStorage.getItem(SY_KEY)) || {}; } catch { SY = {}; }
  }
  function save() { localStorage.setItem(LS_KEY, JSON.stringify(S)); }
  function saveSync() { localStorage.setItem(SY_KEY, JSON.stringify(SY)); }
  function rec(key) {
    if (!S.items[key]) S.items[key] = { st: "todo", min: 0, sessions: [], note: "", u: 0 };
    return S.items[key];
  }
  const touch = (r) => { r.u = Date.now(); };

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
  const now19 = () => new Date().toISOString().slice(0, 19);
  const STICON = { todo: "○", doing: "◐", done: "✅", skip: "⏭" };
  const esc = (t) => (t || "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

  // ---------- timer ----------
  let tick = null;
  function startTimer(key) {
    if (S.runner && S.runner.key !== key) stopTimer(true);
    if (!S.runner) S.runner = { key, start: Date.now() };
    const r = rec(key);
    if (r.st === "todo") { r.st = "doing"; touch(r); }
    save(); render();
  }
  function stopTimer(silent) {
    if (!S.runner) return;
    const min = Math.max(1, Math.round((Date.now() - S.runner.start) / 60000));
    const r = rec(S.runner.key);
    r.sessions.push([new Date(S.runner.start).toISOString().slice(0, 19), min]);
    compact(r); recalc(r); touch(r);
    S.runner = null;
    save(); autoSync();
    if (!silent) render();
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

  // ---------- sync (GitHub Gist) ----------
  const GH = "https://api.github.com/gists";
  const FILE = "study-progress.json";
  const ghHeaders = () => ({ Authorization: "Bearer " + SY.token, Accept: "application/vnd.github+json", "Content-Type": "application/json" });
  function mergeItems(local, remote) {
    const out = {};
    new Set([...Object.keys(local || {}), ...Object.keys(remote || {})]).forEach((k) => {
      const x = local && local[k], y = remote && remote[k];
      if (!x || !y) { out[k] = x || y; return; }
      const newer = (y.u || 0) > (x.u || 0) ? y : x;
      const seen = new Set(), sessions = [];
      [...(x.sessions || []), ...(y.sessions || [])].forEach((s) => {
        const id = s[0] + "|" + s[1];
        if (!seen.has(id)) { seen.add(id); sessions.push(s); }
      });
      sessions.sort((p, q) => (p[0] < q[0] ? -1 : 1));
      const m = { st: newer.st, note: newer.note, u: Math.max(x.u || 0, y.u || 0), sessions, min: 0 };
      compact(m); recalc(m);
      out[k] = m;
    });
    return out;
  }
  function setSync(t) { syncStatus = t; const el = $("#sync-status"); if (el) el.textContent = t; const b = $("#btn-sync"); if (b) b.textContent = t.startsWith("sync failed") ? "⚠" : "⟳"; }
  async function syncNow(manual) {
    if (!SY.token) { if (manual) location.hash = "#/sync"; return; }
    setSync("syncing…");
    try {
      let remote = null;
      if (SY.gist) {
        const r = await fetch(GH + "/" + SY.gist, { headers: ghHeaders() });
        if (r.status === 404) { SY.gist = null; }
        else if (!r.ok) throw new Error("read " + r.status);
        else {
          const g = await r.json();
          const f = g.files && g.files[FILE];
          if (f && f.content) { try { remote = JSON.parse(f.content); } catch { remote = null; } }
        }
      }
      if (remote && remote.items) S.items = mergeItems(S.items, remote.items);
      const payload = JSON.stringify({ items: S.items, synced: new Date().toISOString() });
      const body = JSON.stringify({ description: "Data Architect study progress (tracker sync)", public: false, files: { [FILE]: { content: payload } } });
      const resp = SY.gist
        ? await fetch(GH + "/" + SY.gist, { method: "PATCH", headers: ghHeaders(), body })
        : await fetch(GH, { method: "POST", headers: ghHeaders(), body });
      if (!resp.ok) throw new Error("write " + resp.status);
      const g2 = await resp.json();
      SY.gist = g2.id;
      SY.last = new Date().toISOString();
      save(); saveSync();
      setSync("synced " + SY.last.slice(11, 16) + " UTC");
      if (manual) render();
    } catch (e) {
      setSync("sync failed: " + e.message + (String(e.message).includes("40") ? " (check token)" : ""));
    }
  }
  let syncT = null;
  function autoSync() { if (SY.token) { clearTimeout(syncT); syncT = setTimeout(() => syncNow(false), 4000); } }

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
        <div><b>${pct}%</b> complete · <b>${h1(a.spent)} h</b> logged${SY.token ? ` · <span class="muted">${esc(syncStatus || (SY.last ? "synced " + SY.last.slice(11, 16) + " UTC" : "sync on"))}</span>` : ""}</div>
        <div class="bar"><i class="g" style="width:${pct}%"></i></div>
        <div class="muted">done ${a.doneEst.toFixed(0)} h + skipped ${a.skipEst.toFixed(0)} h of ${a.est.toFixed(0)} h planned · budget ${PLAN.budgetH} h</div>
        <div class="muted">skip-test bank: ${a.skipEst.toFixed(0)} h returned to slack · <a href="#/sync" style="color:var(--accent)">${SY.token ? "sync settings" : "set up sync"}</a></div>
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
        <div style="margin-top:10px"><textarea id="t-note" placeholder="Journal: what I did, what surprised me, open question…">${esc(r.note)}</textarea></div>
        ${r.sessions.length ? `<div class="sessions">Recent: ${r.sessions.slice(-5).reverse().map((s) => `${esc(String(s[0]).replace("T", " ").slice(0, 16))} · ${hm(s[1])}`).join(" · ")}</div>` : ""}
      </div>
      <div class="card content">${it.html}</div>`;
  }

  function syncView() {
    return `<a class="back" href="#/">‹ Home</a>
      <h1>Cross-device sync</h1>
      <div class="card content">
        <p>Sync stores your progress in a <b>secret GitHub Gist</b> — free, no server. Devices merge:
        time sessions are combined, the newest status and notes win. The running timer itself stays on its device.</p>
        <p><b>Setup (once):</b> GitHub → Settings → Developer settings → Personal access tokens →
        <b>Tokens (classic)</b> → Generate new token with <b>only the <code>gist</code> scope</b>.
        Paste it below. The token stays in this browser; on a second device, paste the same token
        and the Gist ID shown after the first sync.</p>
        <div style="margin:10px 0"><input type="password" id="sy-token" placeholder="GitHub token (gist scope only)" value="${esc(SY.token || "")}" style="width:100%;background:var(--panel2);color:var(--text);border:1px solid #2d3640;border-radius:8px;padding:10px;font:inherit"></div>
        <div style="margin:10px 0"><input type="text" id="sy-gist" placeholder="Gist ID (leave empty on first device)" value="${esc(SY.gist || "")}" style="width:100%;background:var(--panel2);color:var(--text);border:1px solid #2d3640;border-radius:8px;padding:10px;font:inherit"></div>
        <div class="btn-row">
          <button class="btn primary" id="sy-save">Save & sync now</button>
          <button class="btn danger" id="sy-off">Disconnect</button>
        </div>
        <div class="muted" id="sync-status">${esc(syncStatus || (SY.last ? "last synced " + SY.last.replace("T", " ").slice(0, 16) + " UTC" : "not configured"))}</div>
        <p class="muted" style="margin-top:10px">Backup still works without sync: ⬇ exports a JSON file, ⬆ imports it.</p>
      </div>`;
  }

  // ---------- router / render ----------
  function render() {
    const hash = location.hash || "#/";
    let html, m;
    if ((m = hash.match(/^#\/p\/(\d)/))) html = phaseView(+m[1]);
    else if ((m = hash.match(/^#\/i\/(.+)$/))) html = itemView(decodeURIComponent(m[1]));
    else if (hash === "#/sync") html = syncView();
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
    const on = (sel, fn) => { const el = $(sel); if (el) el.onclick = fn; };
    if (hash === "#/sync") {
      on("#sy-save", () => {
        SY.token = $("#sy-token").value.trim();
        SY.gist = $("#sy-gist").value.trim() || SY.gist || null;
        saveSync(); syncNow(true);
      });
      on("#sy-off", () => { if (confirm("Disconnect sync? (progress stays on this device)")) { SY = {}; saveSync(); render(); } });
      return;
    }
    const m = hash.match(/^#\/i\/(.+)$/);
    if (!m) return;
    const key = decodeURIComponent(m[1]);
    const r = rec(key);
    on("#t-start", () => startTimer(key));
    on("#t-stop", () => stopTimer(false));
    on("#t-discard", () => { if (confirm("Discard running time?")) discardTimer(); });
    on("#t-manual", () => {
      const v = parseInt(prompt("Minutes to add (negative to correct):", "30"), 10);
      if (!isNaN(v) && v) { r.sessions.push([now19(), v]); compact(r); recalc(r); touch(r); save(); autoSync(); render(); }
    });
    const st = $("#t-status");
    if (st) st.onchange = () => { r.st = st.value; touch(r); save(); autoSync(); banner(); };
    const note = $("#t-note");
    if (note) note.onchange = () => { r.note = note.value; touch(r); save(); autoSync(); };
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
        if (confirm("Merge imported progress into this device?")) {
          S.items = mergeItems(S.items, d.state.items);
          save(); render();
        }
      } catch (e) { alert("Import failed: " + e.message); }
    });
    ev.target.value = "";
  };
  $("#btn-sync").onclick = () => (SY.token ? syncNow(true) : (location.hash = "#/sync"));

  // ---------- boot ----------
  load();
  window.addEventListener("hashchange", render);
  render();
  if (SY.token) syncNow(false);
  if (location.protocol.startsWith("http") && "serviceWorker" in navigator) {
    navigator.serviceWorker.register("sw.js").catch(() => {});
  }
})();
