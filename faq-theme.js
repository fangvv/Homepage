/*! 共用主题切换脚本：faq.html / faq2.html 引用 */
(function () {
    var root = document.documentElement;
    var btn = document.getElementById('themeToggle');
    if (!btn) return;
    var meta = document.querySelector('meta[name="theme-color"]');

    // 同步开关状态与浏览器地址栏颜色
    function sync(dark) {
        btn.setAttribute('aria-pressed', dark ? 'true' : 'false');
        if (meta) meta.setAttribute('content', dark ? '#0F1724' : '#F8FAFC');
    }

    // 初始 data-theme 与 theme-color 已由 <head> 中的内联防闪烁脚本确定，这里只需对齐按钮状态
    sync(root.getAttribute('data-theme') === 'dark');

    btn.addEventListener('click', function () {
        var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
        root.setAttribute('data-theme', next);
        try { localStorage.setItem('theme', next); } catch (e) { }
        sync(next === 'dark');
    });
})();
