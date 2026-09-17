// Rasterise the SVGs handed over by build.py. Playwright's Chromium is the
// only rasteriser this environment has; it is invoked once for the whole set.
const path = require('path');
const fs = require('fs');

const CANDIDATES = [
  'playwright',
  '/opt/node22/lib/node_modules/playwright',
  '/usr/lib/node_modules/playwright',
];

function loadPlaywright() {
  for (const c of CANDIDATES) {
    try { return require(c); } catch (e) { /* try the next one */ }
  }
  throw new Error('playwright not found; install it or run build.py --svg-only');
}

(async () => {
  const { chromium } = loadPlaywright();
  const jobs = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const browser = await chromium.launch();
  for (const job of jobs) {
    const page = await browser.newPage({
      viewport: { width: job.px, height: job.px },
      deviceScaleFactor: 1,
    });
    await page.setContent(
      `<body style="margin:0;background:transparent">${job.svg}</body>`
    );
    await page.screenshot({ path: job.out, omitBackground: true });
    await page.close();
  }
  await browser.close();
})().catch((err) => { console.error(err); process.exit(1); });
