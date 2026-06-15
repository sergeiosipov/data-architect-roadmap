/* Data Architect Study Tracker — vanilla JS, no backend.
   State in localStorage; timers survive app closure via timestamps.
   Optional cross-device sync via a private GitHub Gist (token with gist scope only). */
(function () {
  "use strict";
  const LS_KEY = "spt-v1";
  const SY_KEY = "spt-sync";
  const PLAN = window.PLAN;
  const QUIZ = window.QUIZ || {};
  let TOTAL_CARDS = 0; for (const _l in QUIZ) TOTAL_CARDS += QUIZ[_l].length;
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
    S.srs = S.srs || {};
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
  const fmtInline = (t) => esc(t).replace(/`([^`]+)`/g, "<code>$1</code>");

  // ---------- spaced repetition (SRS) ----------
  // cardId = "<lessonId>#<NNN>"; record: {due:"YYYY-MM-DD", ivl, ease, reps, lapses, last}
  const GRADES = ["Again", "Hard", "Good", "Easy"];
  const cid = (lid, i) => lid + "#" + String(i).padStart(3, "0");
  const todayStr = () => new Date().toISOString().slice(0, 10);
  function addDays(n) { const d = new Date(); d.setDate(d.getDate() + Math.round(n)); return d.toISOString().slice(0, 10); }
  function cardById(id) {
    const k = id.lastIndexOf("#"); if (k < 0) return null;
    const lid = id.slice(0, k), i = +id.slice(k + 1), arr = QUIZ[lid];
    return arr && arr[i - 1] ? { id, lid, i, q: arr[i - 1].q, a: arr[i - 1].a } : null;
  }
  function srsRec(id) {
    if (!S.srs[id]) S.srs[id] = { due: "", ivl: 0, ease: 2.5, reps: 0, lapses: 0, last: 0 };
    return S.srs[id];
  }
  // SM-2-lite spaced-repetition schedule. g: 0 Again, 1 Hard, 2 Good, 3 Easy.
  // ponytail: SM-2-lite (the Anki default family). Ceiling: scheduling uses only ease,
  // not full per-card difficulty modelling; upgrade path is FSRS if the data warrants it.
  function grade(id, g) {
    const c = srsRec(id);
    if (g === 0) { c.reps = 0; c.lapses++; c.ivl = 0; c.ease = Math.max(1.3, c.ease - 0.2); }
    else {
      c.ease = Math.max(1.3, c.ease + (g === 1 ? -0.15 : g === 3 ? 0.15 : 0));
      c.reps++;
      c.ivl = c.reps === 1 ? (g === 3 ? 2 : 1)
        : c.reps === 2 ? (g === 1 ? 3 : 6)
          : Math.max(1, Math.round(c.ivl * (g === 1 ? 1.2 : c.ease)));
    }
    c.due = addDays(c.ivl); c.last = Date.now();
    save(); autoSync();
  }
  function dueCount() {
    const t = todayStr(); let n = 0;
    for (const id in S.srs) { const r = S.srs[id]; if (r.due && r.due <= t && cardById(id)) n++; }
    return n;
  }
  // Build a study session: most-overdue reviews first (cap 30), topped up toward 20 with new
  // cards, preferring lessons you're actively studying (status doing/done) then plan order.
  function buildQueue() {
    const t = todayStr();
    const due = [];
    for (const id in S.srs) { const r = S.srs[id]; if (r.due && r.due <= t && cardById(id)) due.push(id); }
    due.sort((a, b) => (S.srs[a].due < S.srs[b].due ? -1 : S.srs[a].due > S.srs[b].due ? 1 : 0));
    due.splice(30);
    const need = Math.max(0, 20 - due.length), fresh = [];
    if (need > 0) {
      const act = (it) => { const r = S.items[it.key]; return r && (r.st === "doing" || r.st === "done") ? 0 : 1; };
      const lessons = PLAN.phases.flatMap((p) => p.items).filter((it) => it.qid).sort((a, b) => act(a) - act(b));
      outer: for (const it of lessons) for (const c of QUIZ[it.qid]) {
        const id = cid(it.qid, c.i);
        if (!S.srs[id]) { fresh.push(id); if (fresh.length >= need) break outer; }
      }
    }
    return [...due, ...fresh]; // overdue-first then new; no shuffle (the old one was a no-op that broke the sort)
  }

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
  function mergeSrs(local, remote) {
    const out = {};
    new Set([...Object.keys(local || {}), ...Object.keys(remote || {})]).forEach((k) => {
      const x = local && local[k], y = remote && remote[k];
      out[k] = (!x || !y) ? (x || y) : ((y.last || 0) > (x.last || 0) ? y : x);
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
      if (remote && remote.srs) S.srs = mergeSrs(S.srs, remote.srs);
      const payload = JSON.stringify({ items: S.items, srs: S.srs, synced: new Date().toISOString() });
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

  // ---------- quiz rendering (grade-on-reveal SRS) ----------
  function srsBadge(id) {
    const r = S.srs[id];
    if (!r || !r.last) return '<span class="srs new">new</span>';
    return r.due && r.due <= todayStr() ? '<span class="srs due">due</span>'
      : '<span class="srs ok" title="next review">' + esc(r.due) + "</span>";
  }
  // In-lesson self-test is REFERENCE only (question summary -> reveal answer). Grading happens
  // question-first in #/review, so the answer is never shown before recall (no fluency illusion).
  function quizBlockHtml(qid) {
    const cards = QUIZ[qid]; if (!cards) return "";
    const inner = cards.map((c) => {
      const id = cid(qid, c.i);
      return '<details class="q"><summary>' + srsBadge(id) + " <b>" + c.i + ".</b> " +
        fmtInline(c.q) + '</summary><div class="a">' + fmtInline(c.a) + "</div></details>";
    }).join("");
    return '<details class="quiz" open><summary>📝 Self-test — ' + cards.length +
      " questions (reference) · graded question-first in your " +
      '<a href="#/review" style="color:var(--accent)">spaced review ›</a></summary>' +
      '<div class="quizwrap">' + inner + "</div></details>";
  }

  // ---------- review session (spaced repetition queue) ----------
  let reviewQ = null, reviewPos = 0, reviewShown = false, reviewStats = null;
  function reviewStart() { reviewQ = buildQueue(); reviewPos = 0; reviewShown = false; reviewStats = { done: 0, again: 0 }; }
  function reviewView() {
    if (!reviewQ) reviewStart();
    const total = reviewQ.length;
    if (!total) return `<a class="back" href="#/">‹ Home</a><h1>🔁 Review</h1>
      <div class="card content"><p>Nothing due right now. 🎉</p>
      <p class="muted">New cards become reviews as you study lessons and grade their self-tests; scheduled reviews come back on their due date.</p></div>`;
    if (reviewPos >= total) {
      const s = reviewStats || { done: 0, again: 0 };
      return `<a class="back" href="#/">‹ Home</a><h1>Review complete</h1>
        <div class="card"><div class="timerbig">✅</div>
        <div class="muted" style="text-align:center">${s.done} cards reviewed · ${s.again} to relearn soon</div>
        <div class="btn-row"><button class="btn primary" id="rv-again">Review more</button><a class="btn" href="#/">Home</a></div></div>`;
    }
    const id = reviewQ[reviewPos], card = cardById(id);
    if (!card) { reviewPos++; return reviewView(); }
    const lt = (INDEX["e-" + card.lid] || {}).it, tag = lt ? lt.title : card.lid;
    let html = `<a class="back" href="#/">‹ Home</a>
      <div class="rvbar"><div class="bar"><i class="g" style="width:${Math.round((reviewPos / total) * 100)}%"></i></div>
      <div class="muted">card ${reviewPos + 1} / ${total} · <a href="#/i/e-${esc(card.lid)}" style="color:var(--accent)">${esc(String(tag).slice(0, 44))}</a></div></div>
      <div class="card rvcard"><div class="rvq">${fmtInline(card.q)}</div>`;
    if (!reviewShown) {
      html += `<div class="btn-row"><button class="btn primary" id="rv-show">Show answer</button></div>`;
    } else {
      html += `<div class="rva">${fmtInline(card.a)}</div>
        <div class="muted" style="text-align:center;margin:8px 0 4px">Rate recall — this sets the next interval:</div>
        <div class="grades wide" data-cid="${id}">${GRADES.map((g, i) => `<button class="gr g${i}" data-g="${i}">${g}</button>`).join("")}</div>`;
    }
    return html + "</div>";
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
    if (TOTAL_CARDS) {
      const due = dueCount();
      html += `<a class="row review-tile" href="#/review"><span class="st">↻</span>
        <div class="grow"><div class="title">Spaced review</div>
        <div class="sub">${due} due now · ${Object.keys(S.srs).length} of ${TOTAL_CARDS} questions scheduled</div></div>
        <span class="muted">›</span></a>`;
    }
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
    html += `<h2>Plan reference</h2>`;
    (PLAN.pages || []).forEach((pg) => {
      html += `<a class="row" href="#/doc/${pg.key}"><div class="grow"><div class="title">📖 ${esc(pg.title)}</div></div><span class="muted">›</span></a>`;
    });
    return html;
  }

  function docView(key) {
    const pg = (PLAN.pages || []).find((p) => p.key === key);
    if (!pg) return home();
    return `<a class="back" href="#/">‹ Home</a><h1>${esc(pg.title)}</h1><div class="card content">${pg.html}</div>`;
  }

  function phaseView(n) {
    const p = PLAN.phases.find((x) => x.n === n);
    if (!p) return home();
    const pa = agg(p.items);
    let html = `<a class="back" href="#/">‹ All phases</a>
      <h1>Phase ${p.n}: ${esc(p.title)}</h1>
      <div class="card"><div class="muted">months ${p.months} · ${h1(pa.spent)} h logged / ${pa.est.toFixed(0)} h estimated</div>
      <div class="bar"><i class="g" style="width:${Math.round(((pa.doneEst + pa.skipEst) / pa.est) * 100)}%"></i></div></div>`;
    if (p.intro) html += `<details class="card content"><summary><b>Phase goal, prerequisites & exit criteria</b></summary>${p.intro}</details>`;
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
      <div class="card content">${it.html}</div>
      ${it.qid ? quizBlockHtml(it.qid) : ""}`;
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
    if (hash !== "#/review") { reviewQ = null; reviewShown = false; }
    let html, m;
    if ((m = hash.match(/^#\/p\/(\d)/))) html = phaseView(+m[1]);
    else if ((m = hash.match(/^#\/i\/(.+)$/))) html = itemView(decodeURIComponent(m[1]));
    else if ((m = hash.match(/^#\/doc\/(\w+)/))) html = docView(m[1]);
    else if (hash === "#/sync") html = syncView();
    else if (hash === "#/review") html = reviewView();
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
    if (hash === "#/review") {
      on("#rv-show", () => { reviewShown = true; render(); });
      on("#rv-again", () => { reviewStart(); render(); });
      const g = $(".grades.wide");
      if (g) g.onclick = (ev) => {
        const btn = ev.target.closest("button.gr"); if (!btn) return;
        const gv = +btn.getAttribute("data-g");
        grade(g.getAttribute("data-cid"), gv);
        reviewStats.done++; if (gv === 0) reviewStats.again++;
        reviewPos++; reviewShown = false; render();
      };
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
          if (d.state.srs) S.srs = mergeSrs(S.srs, d.state.srs);
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
