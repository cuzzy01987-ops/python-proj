<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>My Phone Number Location</title>
  <meta name="description" content="Lookup a phone number's likely location (demo)." />
  <style>
    :root {
      --bg:#0f1724;
      --card:#0b1220;
      --accent:#06b6d4;
      --muted:#98a2b3;
      --glass: rgba(255,255,255,0.03);
    }

    * { box-sizing: border-box; }
    body {
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial;
      margin: 0;
      background: linear-gradient(180deg,#071024 0%,#081226 100%);
      color: #e6eef6;
      -webkit-font-smoothing: antialiased;
    }

    .container { max-width:980px; margin:48px auto; padding:24px; }

    header { display:flex; align-items:center; gap:16px; }
    .logo {
      width:64px; height:64px; border-radius:12px;
      background: linear-gradient(135deg,var(--accent),#7c3aed);
      display:flex; align-items:center; justify-content:center; font-weight:700;
    }
    h1 { margin:0; font-size:1.6rem; }
    p.lead { margin:8px 0 24px; color:var(--muted); }

    .card {
      background: linear-gradient(180deg,var(--card),#041126);
      padding:20px; border-radius:12px;
      box-shadow:0 6px 30px rgba(2,6,23,0.6);
    }

    form .row { display:flex; gap:12px; flex-wrap:wrap; }
    input[type="text"] {
      flex:1; padding:12px 14px; border-radius:10px;
      border:1px solid rgba(255,255,255,0.06);
      background: var(--glass);
      color: inherit; font-size:1rem;
    }
    button {
      padding:12px 16px; border-radius:10px; border:0;
      background: linear-gradient(90deg,var(--accent),#7c3aed);
      color:#012; cursor:pointer; font-weight:600;
    }
    button:disabled { opacity:0.6; cursor:not-allowed; }

    .result {
      margin-top:18px; padding:14px; border-radius:10px;
      background: linear-gradient(180deg,rgba(255,255,255,0.02),transparent);
      border:1px solid rgba(255,255,255,0.03);
    }
    .meta { color:var(--muted); font-size:0.9rem; }

    .grid { display:grid; grid-template-columns:1fr 320px; gap:18px; margin-top:18px; }
    @media (max-width:880px) { .grid{ grid-template-columns:1fr; } }

    .map-placeholder {
      height:200px; border-radius:8px;
      background: linear-gradient(180deg,#021427,#00121a);
      display:flex; align-items:center; justify-content:center;
      color:var(--muted); font-size:0.95rem;
    }

    footer { margin-top:18px; color:var(--muted); font-size:0.85rem; }
    .note {
      margin-top:12px; padding:10px; border-radius:8px;
      background: rgba(255,255,255,0.02);
      border:1px dashed rgba(255,255,255,0.03);
    }
    code {
      background: rgba(255,255,255,0.03);
      padding:2px 6px; border-radius:6px;
      font-family: monospace;
    }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div class="logo">MP</div>
      <div>
        <h1>My Phone Number Location</h1>
        <p class="lead">Enter a phone number to see a likely country, region, and carrier information.
          <strong>Demo-only</strong> — replace the lookup endpoint with a real API to get live results.</p>
      </div>
    </header>

    <main class="card" role="main">
      <form id="lookupForm" autocomplete="off">
        <div class="row">
          <input id="phoneInput" name="phone" type="text" placeholder="e.g. +254712345678" required />
          <button id="lookupBtn" type="submit">Lookup</button>
        </div>
        <div class="note">
          <strong>Privacy:</strong> This demo does <em>not</em> send numbers anywhere by default.
          When you connect it to a real API you will be transmitting the entered number to that service.
        </div>
      </form>

      <div class="grid">
        <section>
          <div id="output" class="result" aria-live="polite">
            <div class="meta">No lookup run yet. Enter a phone number and press <code>Lookup</code>.</div>
          </div>
        </section>

        <aside>
          <div class="result">
            <h3>Quick tips</h3>
            <ul>
              <li>Include the country code (<code>+254</code>, <code>+1</code>).</li>
              <li>Use a reputable phone-number lookup API.</li>
              <li>Don’t use this to track private individuals without consent.</li>
            </ul>
            <div class="map-placeholder" id="mapBox">Map preview will appear here after a lookup.</div>
          </div>
        </aside>
      </div>

      <footer>
        <div class="meta">Built with plain HTML/CSS/JS · Accessible & responsive</div>
      </footer>
    </main>
  </div>

  <script>
    const USE_FAKE = true;
    const form = document.getElementById('lookupForm');
    const phoneInput = document.getElementById('phoneInput');
    const lookupBtn = document.getElementById('lookupBtn');
    const output = document.getElementById('output');
    const mapBox = document.getElementById('mapBox');

    function sanitizeNumber(n){ return n.replace(/[^0-9+]/g,''); }

    function prettyPhone(n){
      return n.replace(/^(\\+?\\d{1,3})(\\d{3})(\\d{3})(\\d{0,})$/, 
        (_,a,b,c,d)=> [a,b,c,d].filter(Boolean).join(' '));
    }

    function escapeHtml(s){
      if(typeof s !== 'string') s = String(s||'');
      return s.replace(/[&<>\"']/g, c=>({ '&':'&amp;', '<':'&lt;', '>':'&gt;', '\"':'&quot;', \"'\":'&#39;' }[c]));
    }

    function renderResult(data){
      if(!data){
        output.innerHTML = '<div class="meta">No information available.</div>';
        return;
      }
      output.innerHTML = `
        <div><strong>${escapeHtml(data.international_format || data.number)}</strong></div>
        <div class="meta">${escapeHtml(data.country_name || 'Unknown')} · ${escapeHtml(data.carrier || '')}</div>
      `;
      mapBox.textContent = data.country_name ? `Try searching for ${data.country_name} in Maps.` : 'No map preview.';
    }

    form.addEventListener('submit', async (e)=>{
      e.preventDefault();
      const raw = phoneInput.value.trim();
      if(!raw) return;
      const cleaned = sanitizeNumber(raw);
      lookupBtn.disabled = true;
      output.innerHTML = '<div class="meta">Looking up…</div>';

      await new Promise(r=>setTimeout(r,700)); // simulate API

      const result = cleaned.startsWith('+254') ? {
        number: cleaned,
        international_format: prettyPhone(cleaned),
        country_name: 'Kenya',
        carrier: 'Safaricom (simulated)'
      } : {
        number: cleaned,
        international_format: prettyPhone(cleaned),
        country_name: 'Unknown',
        carrier: 'Unknown'
      };

      renderResult(result);
      lookupBtn.disabled = false;
    });
  </script>
</body>
</html>
