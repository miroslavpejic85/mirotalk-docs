(() => {
  const paletteKey = '/.__palette';
  const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
  const palettes = {
    light: { index: 0, color: { scheme: 'default', primary: 'blue', accent: 'light-blue' } },
    dark: { index: 1, color: { scheme: 'slate', primary: 'black', accent: 'dark-blue' } },
  };

  const savedTheme = () => {
    try {
      const palette = JSON.parse(localStorage.getItem(paletteKey));
      return palette?.color?.scheme === 'slate' ? 'dark' : palette ? 'light' : null;
    } catch {
      return null;
    }
  };

  const applyTheme = (theme = savedTheme() ?? (mediaQuery.matches ? 'dark' : 'light')) => {
    document.documentElement.dataset.theme = theme;
    window.dispatchEvent(new CustomEvent('mirotalk-theme-change', { detail: { theme } }));
    return theme;
  };

  const setTheme = (theme) => {
    if (!(theme in palettes)) return applyTheme();
    localStorage.setItem(paletteKey, JSON.stringify(palettes[theme]));
    return applyTheme(theme);
  };

  window.MiroTalkTheme = Object.freeze({
    get: () => document.documentElement.dataset.theme,
    set: setTheme,
    toggle: () => setTheme(document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark'),
  });

  applyTheme();
  mediaQuery.addEventListener('change', () => {
    if (!savedTheme()) applyTheme();
  });
  window.addEventListener('storage', (event) => {
    if (event.key === paletteKey) applyTheme();
  });
})();