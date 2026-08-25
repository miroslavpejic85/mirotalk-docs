(() => {
  const paletteKey = '/.__palette';
  const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');

  const savedTheme = () => {
    try {
      const palette = JSON.parse(localStorage.getItem(paletteKey));
      return palette?.color?.scheme === 'slate' ? 'dark' : palette ? 'light' : null;
    } catch {
      return null;
    }
  };

  const applyTheme = () => {
    document.documentElement.dataset.theme = savedTheme() ?? (mediaQuery.matches ? 'dark' : 'light');
  };

  applyTheme();
  mediaQuery.addEventListener('change', () => {
    if (!savedTheme()) applyTheme();
  });
  window.addEventListener('storage', (event) => {
    if (event.key === paletteKey) applyTheme();
  });
})();