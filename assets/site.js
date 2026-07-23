function setActiveNav(page){
  document.querySelectorAll('.global-nav a').forEach(a=>{
    a.classList.toggle('active', a.dataset.page === page);
  });
}

function renderStats(elId, stats){
  const el = document.getElementById(elId);
  el.innerHTML = stats.map(s=>`<div class="hstat"><div class="num">${s.value}</div><div class="label">${s.label}</div></div>`).join('');
}

function renderTags(barId, categories, active, onChange){
  const bar = document.getElementById(barId);
  bar.innerHTML = '';
  categories.slice().sort((a,b)=>a.localeCompare(b)).forEach(cat=>{
    const btn = document.createElement('button');
    btn.className = 'tag-btn' + (active.has(cat) ? ' active' : '');
    btn.textContent = cat;
    btn.onclick = ()=>{ if(active.has(cat)) active.delete(cat); else active.add(cat); onChange(); };
    bar.appendChild(btn);
  });
}

function renderSkillsGrid(gridId, skills, active){
  const grid = document.getElementById(gridId);
  grid.innerHTML = '';
  const visible = skills.filter(s => active.size === 0 || active.has(s.category))
    .sort((a,b) => a.category.localeCompare(b.category) || a.title.localeCompare(b.title));
  if(visible.length === 0){
    grid.innerHTML = `<div class="empty-state">No skills published here yet — check back soon.</div>`;
    return;
  }
  visible.forEach(s=>{
    const div = document.createElement('div');
    div.className = 'skill-card';
    div.innerHTML = `
      <div class="skill-card-cat">${s.category}</div>
      <h3>${s.title}</h3>
      <p class="summary">${s.summary}</p>
      <div class="perfect-label">Perfect for</div>
      <ul>${s.perfectFor.map(p=>`<li>${p}</li>`).join('')}</ul>
      ${(s.created || s.updated) ? `<div class="skill-card-dates">${s.updated ? `Updated ${s.updated}` : ''}${s.updated && s.created ? ' · ' : ''}${s.created ? `Added ${s.created}` : ''}</div>` : ''}
      <div class="actions">
        <button class="btn btn-ghost btn-sm" data-read="${s.slug}">Read</button>
        <a class="btn btn-ghost btn-sm" href="skills/${s.slug}/skill.md" download>↓ Download</a>
      </div>
    `;
    grid.appendChild(div);
  });
  grid.querySelectorAll('[data-read]').forEach(btn=>{
    btn.addEventListener('click', ()=> openSkill(btn.dataset.read));
  });
}

function renderPromptsGrid(gridId, prompts, active){
  const grid = document.getElementById(gridId);
  grid.innerHTML = '';
  const visible = prompts.filter(p => active.size === 0 || active.has(p.category));
  if(visible.length === 0){
    grid.innerHTML = `<div class="empty-state">No prompts published here yet — check back soon.</div>`;
    return;
  }
  visible.forEach(p=>{
    const div = document.createElement('div');
    div.className = 'skill-card';
    div.innerHTML = `
      <div class="skill-card-cat">${p.category}</div>
      <h3>${p.title}</h3>
      <p class="summary">${p.summary}</p>
      <div class="perfect-label">Perfect for</div>
      <ul>${p.perfectFor.map(x=>`<li>${x}</li>`).join('')}</ul>
      ${(p.created || p.updated) ? `<div class="skill-card-dates">${p.created ? `Added ${p.created}` : ''}${p.created && p.updated ? ' · ' : ''}${p.updated ? `Updated ${p.updated}` : ''}</div>` : ''}
      <div class="actions">
        <button class="btn btn-ghost btn-sm" data-read="${p.slug}">Read</button>
        <button class="btn btn-ghost btn-sm" data-copy="${p.slug}">Copy</button>
        <a class="btn btn-navy btn-sm" href="https://claude.ai/new" target="_blank" rel="noopener">Open Claude.ai</a>
      </div>
    `;
    grid.appendChild(div);
  });
  grid.querySelectorAll('[data-read]').forEach(btn=>{
    btn.addEventListener('click', ()=> openPrompt(btn.dataset.read));
  });
  grid.querySelectorAll('[data-copy]').forEach(btn=>{
    btn.addEventListener('click', ()=> copyPrompt(btn.dataset.copy, btn));
  });
}

function openPrompt(slug){
  fetch(`prompts/${slug}/prompt.md`).then(r=>r.text()).then(md=>{
    const fm = md.match(/^---([\s\S]*?)---/);
    let meta = '';
    if(fm){
      const cre = (fm[1].match(/^created:\s*(.+)$/m) || [])[1];
      const upd = (fm[1].match(/^updated:\s*(.+)$/m) || [])[1];
      if(cre || upd){
        meta = `<div class="modal-meta">${upd ? `Updated ${upd.trim()}` : ''}${upd && cre ? ' · ' : ''}${cre ? `Added ${cre.trim()}` : ''}</div>`;
      }
    }
    const body = md.replace(/^---[\s\S]*?---/, '').trim();
    document.getElementById('modalBody').innerHTML = meta + mdToHtml(body);
    document.getElementById('modalBackdrop').classList.add('show');
  });
}

function copyPrompt(slug, btn){
  fetch(`prompts/${slug}/prompt.md`).then(r=>r.text()).then(md=>{
    const fenced = md.match(/```[\w]*\n([\s\S]*?)```/);
    const text = fenced ? fenced[1].trim() : md.replace(/^---[\s\S]*?---/, '').trim();
    navigator.clipboard.writeText(text).then(()=>{
      const original = btn.textContent;
      btn.textContent = 'Copied ✓';
      setTimeout(()=>{ btn.textContent = original; }, 1800);
    });
  });
}

function openSkill(slug){
  fetch(`skills/${slug}/skill.md`).then(r=>r.text()).then(md=>{
    const fm = md.match(/^---([\s\S]*?)---/);
    let meta = '';
    if(fm){
      const cre = (fm[1].match(/^created:\s*(.+)$/m) || [])[1];
      const upd = (fm[1].match(/^updated:\s*(.+)$/m) || [])[1];
      if(cre || upd){
        meta = `<div class="modal-meta">${upd ? `Updated ${upd.trim()}` : ''}${upd && cre ? ' · ' : ''}${cre ? `Added ${cre.trim()}` : ''}</div>`;
      }
    }
    const body = md.replace(/^---[\s\S]*?---/, '').trim();
    document.getElementById('modalBody').innerHTML = meta + mdToHtml(body);
    document.getElementById('modalBackdrop').classList.add('show');
  });
}

function mdToHtml(md){
  return md
    .split(/\n\n+/).map(block=>{
      if(block.startsWith('## ')) return `<h2>${block.slice(3)}</h2>`;
      if(block.startsWith('# ')) return `<h1>${block.slice(2)}</h1>`;
      if(block.startsWith('> ')) return `<blockquote>${block.replace(/^> ?/gm,'')}</blockquote>`;
      if(block.startsWith('- ')) return `<ul>${block.split('\n').map(l=>`<li>${l.replace(/^- /,'')}</li>`).join('')}</ul>`;
      return `<p>${block}</p>`;
    }).join('\n');
}

function initModal(){
  document.getElementById('modalClose').addEventListener('click', ()=>{
    document.getElementById('modalBackdrop').classList.remove('show');
  });
  document.getElementById('modalBackdrop').addEventListener('click', (e)=>{
    if(e.target.id === 'modalBackdrop') document.getElementById('modalBackdrop').classList.remove('show');
  });
}
