/* Site search: no libraries, no outside requests. */
(function () {
  'use strict';

  var FOLD = { 'ç': 'c', 'ğ': 'g', 'ı': 'i', 'ö': 'o', 'ş': 's', 'ü': 'u', 'â': 'a', 'î': 'i', 'û': 'u' };

  function normalize(s) {
    s = String(s == null ? '' : s).toLocaleLowerCase('tr');
    s = s.replace(/[çğıöşüâîû]/g, function (c) { return FOLD[c]; });
    s = s.normalize('NFD').replace(/[̀-ͯ]/g, '');
    s = s.replace(/['’‘ʼ]/g, '');
    s = s.replace(/[^\p{L}\p{N}]+/gu, ' ');
    return s.replace(/\s+/g, ' ').trim();
  }

  function dateKey(d) {
    var m = /^(\d\d)\.(\d\d)\.(\d{4})$/.exec(d || '');
    return m ? +(m[3] + m[2] + m[1]) : 0;
  }

  // Adds normalised fields once, after loading the index. Fields are padded with a
  // leading space so a word-start match is indexOf(' ' + word).
  function prepare(entries) {
    return entries.map(function (e) {
      return {
        title: e.title, url: e.url, date: e.date, tags: e.tags, summary: e.summary,
        _t: ' ' + normalize(e.title), _g: ' ' + normalize(e.tags), _s: ' ' + normalize(e.summary),
        _x: null,
        _d: dateKey(e.date)
      };
    });
  }

  // Full text: normalises it in chunks (setTimeout 0) so typing never freezes, and attaches
  // it to the prepared index only when everything is done. `full` is [{url, text}].
  // Calls done() when finished. chunk defaults to 40 entries; pass sync=true to run at once.
  function mergeFull(index, full, done, chunk, sync) {
    var byUrl = {}, texts = new Array(full.length), n = chunk || 40, pos = 0;
    function step() {
      var end = Math.min(pos + n, full.length);
      for (; pos < end; pos++) texts[pos] = ' ' + normalize(full[pos].text);
      if (pos < full.length) {
        if (sync) step(); else setTimeout(step, 0);
        return;
      }
      for (var i = 0; i < full.length; i++) byUrl[full[i].url] = texts[i];
      for (var j = 0; j < index.length; j++) {
        if (byUrl[index[j].url] != null) index[j]._x = byUrl[index[j].url];
      }
      if (done) done();
    }
    step();
  }

  function words(query) {
    var n = normalize(query);
    return n ? n.split(' ') : [];
  }

  // Per query word: best field it starts a word in (title 100, tags 10, summary 2, full text 1).
  // Every word must match somewhere. Ties: newer first, pages (no date) after posts.
  function search(index, query) {
    var ws = words(query);
    if (normalize(query).length < 2) return [];
    var out = [];
    for (var i = 0; i < index.length; i++) {
      var e = index[i], score = 0, ok = true;
      for (var j = 0; j < ws.length; j++) {
        var w = ' ' + ws[j];
        if (e._t.indexOf(w) !== -1) score += 100;
        else if (e._g.indexOf(w) !== -1) score += 10;
        else if (e._s.indexOf(w) !== -1) score += 2;
        else if (e._x && e._x.indexOf(w) !== -1) score += 1;
        else { ok = false; break; }
      }
      if (ok) out.push({ e: e, score: score, i: i });
    }
    out.sort(function (a, b) {
      return (b.score - a.score) || (b.e._d - a.e._d) || (a.i - b.i);
    });
    return out.map(function (r) { return r.e; });
  }

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { normalize: normalize, prepare: prepare, mergeFull: mergeFull, search: search };
  }
  if (typeof document === 'undefined') return;

  /* ---- Browser part ---- */
  var indexPromise = null;
  function loadIndex(url) {
    if (!indexPromise) {
      indexPromise = fetch(url, { credentials: 'same-origin' })
        .then(function (r) { if (!r.ok) throw new Error('search index ' + r.status); return r.json(); })
        .then(prepare)
        .catch(function (err) { indexPromise = null; throw err; });
    }
    return indexPromise;
  }

  var fullPromise = null;
  // Starts the background load of the full text once the small index is ready. Never rejects
  // loudly: on failure the caller keeps using the small index. Resolves true when merged.
  function loadFull(indexUrl, fullUrl) {
    if (!fullPromise && fullUrl) {
      fullPromise = loadIndex(indexUrl).then(function (idx) {
        return fetch(fullUrl, { credentials: 'same-origin' })
          .then(function (r) { if (!r.ok) throw new Error('full index ' + r.status); return r.json(); })
          .then(function (full) {
            return new Promise(function (resolve) { mergeFull(idx, full, function () { resolve(idx); }); });
          });
      }).catch(function () { return null; });
    }
    return fullPromise || Promise.resolve(null);
  }

  function debounce(fn, ms) {
    var t;
    return function () { var a = arguments; clearTimeout(t); t = setTimeout(function () { fn.apply(null, a); }, ms); };
  }

  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text != null) n.textContent = text;
    return n;
  }

  function initHeader(form) {
    var input = form.querySelector('input[name="q"]');
    var drop = form.querySelector('.sh-search-drop');
    var status = form.querySelector('[role="status"]');
    var indexUrl = form.getAttribute('data-index');
    var fullUrl = form.getAttribute('data-index-full');
    var resultsUrl = form.getAttribute('data-results');
    var txtNone = form.getAttribute('data-none');
    var txtAll = form.getAttribute('data-all');
    var txtCount = form.getAttribute('data-count');
    var items = [], active = -1, seq = 0;

    input.setAttribute('role', 'combobox');
    input.setAttribute('aria-autocomplete', 'list');
    input.setAttribute('aria-controls', drop.id);
    input.setAttribute('aria-expanded', 'false');
    drop.setAttribute('role', 'listbox');

    function close() {
      drop.hidden = true;
      input.setAttribute('aria-expanded', 'false');
      input.removeAttribute('aria-activedescendant');
      active = -1;
      for (var i = 0; i < items.length; i++) items[i].classList.remove('is-active');
    }

    function highlight(n) {
      if (active >= 0 && items[active]) items[active].classList.remove('is-active');
      active = n;
      if (n >= 0 && items[n]) {
        items[n].classList.add('is-active');
        input.setAttribute('aria-activedescendant', items[n].id);
        if (items[n].scrollIntoView) items[n].scrollIntoView({ block: 'nearest' });
      } else {
        input.removeAttribute('aria-activedescendant');
      }
    }

    function render(results, query) {
      drop.textContent = '';
      items = [];
      active = -1;
      if (!results.length) {
        drop.appendChild(el('div', 'sr-none', txtNone));
        status.textContent = txtNone;
      } else {
        results.slice(0, 8).forEach(function (r, i) {
          var a = el('a');
          a.href = r.url;
          a.id = 'site-search-opt-' + i;
          a.setAttribute('role', 'option');
          a.appendChild(document.createTextNode(r.title));
          if (r.date) a.appendChild(el('span', 'sr-date', r.date));
          drop.appendChild(a);
          items.push(a);
        });
        var all = el('a', 'sr-all', txtAll + ' (' + results.length + ') →');
        all.href = resultsUrl + '?q=' + encodeURIComponent(query);
        all.id = 'site-search-opt-all';
        all.setAttribute('role', 'option');
        drop.appendChild(all);
        items.push(all);
        status.textContent = results.length + ' ' + txtCount;
      }
      drop.hidden = false;
      input.setAttribute('aria-expanded', 'true');
    }

    function update() {
      var q = input.value;
      var my = ++seq;
      if (normalize(q).length < 2) { close(); status.textContent = ''; return; }
      loadIndex(indexUrl).then(function (idx) {
        loadFull(indexUrl, fullUrl).then(refreshFull);
        if (my !== seq) return;
        render(search(idx, q), q);
      }, function () { /* index unavailable: the form still submits to the results page */ });
    }

    // Full text arrived: refresh an open dropdown, unless the user has moved the highlight
    // (then it is applied on the next keystroke).
    function refreshFull(idx) {
      if (!idx || drop.hidden || active >= 0) return;
      var q = input.value;
      if (normalize(q).length < 2) return;
      render(search(idx, q), q);
    }

    var delayed = debounce(update, 150);
    input.addEventListener('input', delayed);
    input.addEventListener('focus', function () {
      loadIndex(indexUrl).then(function () { loadFull(indexUrl, fullUrl).then(refreshFull); }, function () {});
      if (normalize(input.value).length >= 2 && drop.hidden) update();
    });
    input.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') {
        if (!drop.hidden) { close(); e.preventDefault(); }
      } else if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
        if (drop.hidden || !items.length) return;
        e.preventDefault();
        var n = active + (e.key === 'ArrowDown' ? 1 : -1);
        if (n >= items.length) n = 0;
        if (n < 0) n = items.length - 1;
        highlight(n);
      } else if (e.key === 'Enter') {
        if (!drop.hidden && active >= 0 && items[active]) {
          e.preventDefault();
          window.location.href = items[active].href;
        }
      }
    });
    document.addEventListener('click', function (e) {
      if (!form.contains(e.target)) close();
    });
    form.addEventListener('focusout', function (e) {
      if (e.relatedTarget && !form.contains(e.relatedTarget)) close();
    });
  }

  function initResults(form) {
    var input = form.querySelector('input[name="q"]');
    var count = document.getElementById('ara-count');
    var list = document.getElementById('ara-list');
    var q = '';
    try { q = new URLSearchParams(window.location.search).get('q') || ''; } catch (e) {}
    input.value = q;
    if (normalize(q).length < 2) return;
    count.textContent = '...';
    var hf = document.querySelector('form.sh-search');
    var url = hf ? hf.getAttribute('data-index') : '/search.json';
    var fullUrl = hf ? hf.getAttribute('data-index-full') : '/search-full.json';
    function show(idx, pending) {
      var res = search(idx, q);
      var n = res.length;
      count.textContent = (n ? n + ' sonuç' : 'Sonuç bulunamadı') + (pending ? ' (tam metin aranıyor…)' : '');
      list.textContent = '';
      res.forEach(function (r) {
        var li = el('li');
        var a = el('a', null, r.title);
        a.href = r.url;
        li.appendChild(a);
        if (r.date) li.appendChild(el('span', 'ara-date', r.date));
        if (r.summary) li.appendChild(el('p', 'ara-sum', r.summary));
        list.appendChild(li);
      });
    }
    loadIndex(url).then(function (idx) {
      show(idx, !!fullUrl);
      if (!fullUrl) return;
      loadFull(url, fullUrl).then(function (full) { show(idx, false); });
    }, function () {
      count.textContent = 'Arama dizini yüklenemedi.';
    });
  }

  function init() {
    var h = document.querySelector('form.sh-search');
    if (h) initHeader(h);
    var r = document.getElementById('ara-form');
    if (r) initResults(r);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
