function setActiveNav(page){
  document.querySelectorAll('.page-nav a').forEach(a=>{
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
  categories.forEach(cat=>{
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
  const visible = skills.filter(s => active.size === 0 || active.has(s.category));
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
      <div class="actions">
        <button class="btn btn-ghost btn-sm" data-read="${s.slug}">Read</button>
        <a class="btn btn-ghost btn-sm" href="skills/${s.slug}/skill.md" download>↓ Download</a>
        <a class="btn btn-navy btn-sm" href="https://claude.ai/new" target="_blank" rel="noopener">Open Claude.ai</a>
      </div>
    `;
    grid.appendChild(div);
  });
  grid.querySelectorAll('[data-read]').forEach(btn=>{
    btn.addEventListener('click', ()=> openSkill(btn.dataset.read));
  });
}

function openSkill(slug){
  fetch(`skills/${slug}/skill.md`).then(r=>r.text()).then(md=>{
    const body = md.replace(/^---[\s\S]*?---/, '').trim();
    document.getElementById('modalBody').innerHTML = mdToHtml(body);
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
